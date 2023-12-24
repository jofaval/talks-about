import argparse
from typing import List, Optional

import cchardet
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

DEFAULT_AMOUNT_PER_PARTICIPATION = 20
DEFAULT_QUANTITY = 1
FALLBACK_WON_PER_TICKET = 0

ENCODING = "utf-8"
REQUEST_TIMEOUT = 3
CSV_SEPARATOR = ";"


class Lottery(BaseModel):
    lottery_number: int
    quantity: int
    amount_per_participation: Optional[int]
    total_invested: Optional[int]

    @staticmethod
    def get_lottery_number(values: List[str]):
        return values[0]

    @staticmethod
    def get_quantity(values: List[str]):
        quantity = values[1]
        if not quantity:
            return DEFAULT_QUANTITY

        return int(quantity)

    @staticmethod
    def get_amount_per_participation(values: List[str]):
        per_participation = values[2]
        if not per_participation or per_participation == "0":
            return DEFAULT_AMOUNT_PER_PARTICIPATION

        return int(per_participation)

    @staticmethod
    def parse(line: str):
        values = line.split(CSV_SEPARATOR)

        quantity = Lottery.get_quantity(values)
        per_participation = Lottery.get_amount_per_participation(values)

        return Lottery(
            amount_per_participation=per_participation,
            lottery_number=Lottery.get_lottery_number(values),
            quantity=quantity,
            total_invested=quantity * per_participation,
        )


class SolvedLottery(BaseModel):
    lottery: Lottery
    has_won: bool
    won_per_ticket: Optional[int]
    total_won: Optional[int]


class LotteryResult(BaseModel):
    won: int
    invested: int
    balance: int
    solved_lotteries: List[SolvedLottery]


class LotterySolver(BaseModel):
    lotteries: List[Lottery]

    def get_result_url(self, number: str):
        return f"https://www.nacionalloteria.es/loteria-navidad/Comprobar-Loteria-Navidad.php?numero={number}#comprobador"

    def get_result(self, number: str):
        response = requests.get(self.get_result_url(
            number), timeout=REQUEST_TIMEOUT)
        if not response.ok:
            return

        return BeautifulSoup(markup=response.text, features="lxml")

    def from_result_has_won(self, soup: BeautifulSoup):
        return soup.select_one(".alert-success") is not None

    def from_result_won_per_ticket(self, soup: BeautifulSoup):
        price = soup.select_one(".text-premio strong")
        if not price:
            return FALLBACK_WON_PER_TICKET

        raw_price = price.text.strip()
        cleaned_price = raw_price.split(" ")[0].replace(".", "")

        return int(cleaned_price)

    def get_total_won(self, lottery: Lottery, won_per_ticket: int):
        participation_percentage = lottery.amount_per_participation / \
            DEFAULT_AMOUNT_PER_PARTICIPATION

        return lottery.quantity * (won_per_ticket * participation_percentage)

    def solve(self):
        solved_lotteries: List[SolvedLottery] = []
        total = {"won": 0, "invested": 0, "balance": 0}

        for lottery in self.lotteries:
            raw_result = self.get_result(number=lottery.lottery_number)

            has_won = self.from_result_has_won(raw_result)
            won_per_ticket = self.from_result_has_won(raw_result)

            total_won = self.get_total_won(lottery, won_per_ticket)
            total["won"] += total_won
            total["invested"] += lottery.total_invested

            solved_lotteries.append(
                SolvedLottery(
                    has_won=has_won,
                    won_per_ticket=won_per_ticket,
                    lottery=lottery,
                    total_won=total_won
                )
            )

        total["balance"] = total["won"] - total["invested"]
        return LotteryResult(solved_lotteries=solved_lotteries, **total)


def parse_numbers(filename: str) -> LotterySolver:
    numbers = []

    with open(filename, encoding=ENCODING) as file:
        valid_lines = file.readlines()[1:3]
        numbers = [Lottery.parse(line.strip()) for line in valid_lines]

    return LotterySolver(lotteries=numbers)


def get_filename():
    parser = argparse.ArgumentParser(
        prog="Lotería Nacional Solver",
        description="Solver para el laboratorio de web scraping con números de lotería",
        epilog="Cátedra de Universidad de Valencia con Capgemini"
    )

    parser.add_argument(
        "filename",
        help="Indica la ruta (relativa o absoluta) al CSV que se quiere resolver"
    )

    args = parser.parse_args()
    return args.filename


def main():
    solver = parse_numbers(filename=get_filename())
    result = solver.solve()


if __name__ == "__main__":
    main()
