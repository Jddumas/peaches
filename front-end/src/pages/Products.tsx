import React from "react";
import ProductTile from "../components/ProductTile";
import { Product } from "../entity";

export const mockProducts: Product[] = [
  {
    sku: 1,
    name: "Bandaid",
    brand: "J&J",
    category: "medical",
    description:
      "Quick, resilience bandaid by J&J. Waterproof and comfortable to use.",
    price: 3,
    weight: 0.2,
    stock: 100,
    thumbnail_url:
      "https://m.media-amazon.com/images/I/71IGAPIkkpS._AC_SX466_PIbundle-2,TopRight,0,0_SH20_.jpg",
    shelf_life: 1095,
  },
  {
    sku: 25,
    name: "Real-fit edible underwear",
    brand: "Edible arrangement",
    category: "snack",
    description: "Real fit edible male underwear, cherry flavor.",
    price: 3,
    weight: 1,
    stock: 2532,
    thumbnail_url:
      "https://d345p6ejtlhe1s.cloudfront.net/00036000509823/256_8968a85423e4857752e539d9bc36f06ee412fdbb.jpg",
    shelf_life: 1005,
  },
  {
    sku: 2,
    name: "Oranges",
    brand: "Fresh farm",
    category: "fruit",
    description: "Delicious oranges from local farm",
    price: 3,
    weight: 0.2,
    stock: 100,
    thumbnail_url:
      "https://cdn.shopify.com/s/files/1/0059/8835/2052/products/Lanes_Late_Navel_Orange_450_650x.jpg?v=1612444146",
    shelf_life: 15,
  },

  {
    sku: 20,
    name: "Trojan condom",
    brand: "Trojan",
    category: "adult health",
    description: "Fun stuff for homos",
    price: 10,
    weight: 0.1,
    stock: 1000,
    thumbnail_url:
      "https://d345p6ejtlhe1s.cloudfront.net/00022600973270/256_b84141feeba923ceb0a6375789f0e30abefff0f7.jpg",
    shelf_life: 15,
  },

  {
    sku: 21,
    name: "Gala Apples",
    brand: "Dole",
    category: "fruit",
    description: "Sweet, crispy apples from New England",
    price: 2,
    weight: 1,
    stock: 100,
    thumbnail_url:
      "https://s.cornershopapp.com/product-images/4167456.jpg?versionId=wfEMK_aaQ981an4Wzdsx8k_.LBEOOYN5",
    shelf_life: 15,
  },

  {
    sku: 22,
    name: "Oatnut Bread",
    brand: "Oroweat",
    category: "grains",
    description: "Freshly baked whole grain bread",
    price: 3,
    weight: 1,
    stock: 50,
    thumbnail_url: "https://images.heb.com/is/image/HEBGrocery/000402036",
    shelf_life: 7,
  },

  {
    sku: 23,
    name: "Whole Milk Yogurt",
    brand: "Dannon",
    category: "dairy",
    description: "Creamy plain yogurt from happy cows",
    price: 2.5,
    weight: 2,
    stock: 75,
    thumbnail_url: "https://images.heb.com/is/image/HEBGrocery/000313850",
    shelf_life: 30,
  },

  {
    sku: 23,
    name: "Whole Milk Yogurt",
    brand: "Dannon",
    category: "dairy",
    description: "Creamy plain yogurt",
    price: 2.5,
    weight: 2,
    stock: 75,
    thumbnail_url: "https://images.heb.com/is/image/HEBGrocery/000313850",
    shelf_life: 30,
  },

  {
    sku: 23,
    name: "Whole Milk",
    brand: "Borden",
    category: "dairy",
    description: "rbST free whole milk from happy cows",
    price: 3.5,
    weight: 1,
    stock: 200,
    thumbnail_url:
      "https://i5.walmartimages.com/asr/e7902a92-e10f-4a2a-8396-b1dd30316438.0c4283705821cf02c1bca800757f8139.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    shelf_life: 30,
  },

  {
    sku: 24,
    name: "Almonds",
    brand: "Blue Diamond",
    category: "nuts",
    description: "Whole natural raw snack nuts",
    price: 8,
    weight: 2,
    stock: 125,
    thumbnail_url:
      "https://m.media-amazon.com/images/I/81QwQ4qe4QL._SL1500_.jpg",
    shelf_life: 90,
  },
];

const ProductPage: React.FunctionComponent = () => (
  <section className="section">
    <p className="title">This is product page</p>
    <p className="subtitle">Under construction, coming</p>

    <div className="columns is-multiline">
      {mockProducts.map((p) => (
        <div className="column is-3">
          <ProductTile product={p} />
        </div>
      ))}
    </div>
  </section>
);

export default ProductPage;
