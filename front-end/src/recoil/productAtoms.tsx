import { atom, selector, useRecoilState, useRecoilValue } from "recoil";
import ProductAPI from "../api/product-api";

export const productsAtom = atom({
  key: "products",
  default: selector({
    key: "products/default",
    get: async () => ProductAPI.getAll(),
  }),
});
