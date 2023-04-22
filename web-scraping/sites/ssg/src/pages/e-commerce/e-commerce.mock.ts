import { ECommerceProduct } from "./e-commerce.type";

export const products: ECommerceProduct[] = Array(20 + 1)
  .slice(1)
  .map((index) => ({
    id: index,
    name: "",
    price: 20,
  }));
