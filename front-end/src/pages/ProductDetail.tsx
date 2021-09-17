import React from "react";
import { Product } from "../entity";
import { useParams } from "react-router-dom";
import { mockProducts } from "./Products";

const ProductDetail: React.FunctionComponent = () => {
  let { sku } = useParams() as unknown as { sku: number };
  let product = mockProducts.find((p) => p.sku == sku);
  if (!product) return <p className="title">Product not found</p>;
  return (
    <section className="section">
      <div className="columns">
        <div className="column is-two-fifth">
          <img src={product.thumbnail_url} alt={product.name} />
        </div>
        <div className="column">
          <div className="is-flex is-justify-content-space-between">
            <span className="is-size-4 has-text-weight-bold">
              {product.name}
            </span>
            <span className="p-2 is-rounded has-text-weight-medium has-text-white has-background-info">
              Price: ${product.price}
            </span>
          </div>
          <div className="mt-4">
            <div>
              <span>Brand: </span> {product.brand}
            </div>
            <p>{product.description}</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProductDetail;
