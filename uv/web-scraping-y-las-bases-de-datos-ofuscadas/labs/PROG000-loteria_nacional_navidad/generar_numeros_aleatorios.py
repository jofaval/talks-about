import argparse
import os
import random
import re
from typing import List

from pydantic import BaseModel

MAX_KNOWN_LOTTERY_NUMBER = 99_999
JUMP_LINE = "\n"
ENCODING = "utf-8"


BASE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_PATH, "data")
WINNERS_FILE = os.path.join(BASE_PATH, "numeros_ganadores.txt")

CSV_SEPARATOR = ";"
CSV_HEADERS = ["lottery_number", "quantity", "amount_per_participation"]


class CliArguments(BaseModel):
    quantity: int
    files: int


def get_args():
    parser = argparse.ArgumentParser(
        prog="Números de lotería",
        description="Genera ficheros para el laboratorio de web scraping con números de lotería",
        epilog="Cátedra de Universidad de Valencia con Capgemini"
    )

    parser.add_argument("-c", "--cantidad", default="100",
                        help="La cantidad de números de lotería a generar", required=False)

    parser.add_argument("-f", "--ficheros", default="5",
                        help="La cantidad de ficheros a generar", required=False)

    args = parser.parse_args()

    assert re.match(r"\d+", args.cantidad) is not None
    assert re.match(r"\d+", args.ficheros) is not None

    return CliArguments(
        quantity=int(args.cantidad),
        files=int(args.ficheros)
    )


def safe_guard():
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)


def get_winners() -> List[str]:
    lines: List[str] = []

    with open(WINNERS_FILE, "r", encoding=ENCODING) as file:
        lines = file.readlines()

    return lines


def write_numbers(numbers: List[str], index: int):
    filename = os.path.join(DATA_PATH, f"file-{str(index).zfill(3)}.csv")
    with open(filename, "w+", encoding=ENCODING) as file:
        file.write(JUMP_LINE.join(numbers))


def get_shuffled_numbers(winners: List[str], amount: int):
    numbers = [
        str(random.randint(0, MAX_KNOWN_LOTTERY_NUMBER))
        for _ in range(0, amount)
    ]
    numbers.extend((number.strip() for number in winners))

    random.shuffle(numbers)
    return numbers


MAX_QUANTITY = 10
MAX_AMOUNT_PER_PARTICIPATION = 20


def aggregate_details(numbers: List[str]):
    aux = numbers
    numbers = [CSV_SEPARATOR.join(CSV_HEADERS)]

    for number in aux:
        quantity = random.randint(1, MAX_QUANTITY)
        per_participation = random.randint(0, MAX_AMOUNT_PER_PARTICIPATION)

        numbers.append(CSV_SEPARATOR.join(
            [number, str(quantity), str(per_participation)]
        ))

    return numbers


def generate_random_numbers(args: CliArguments):
    winners = get_winners()
    amount = args.quantity - len(winners)

    for index in range(1, args.files+1):
        write_numbers(aggregate_details(
            get_shuffled_numbers(winners, amount)
        ), index)


def main():
    safe_guard()
    generate_random_numbers(args=get_args())


if __name__ == "__main__":
    main()
