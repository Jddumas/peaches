import React from "react";
import { Product } from "../entity";
import { Link } from "react-router-dom";

type ProductTileProps = { product: Product };
const ProductTile: React.VFC<ProductTileProps> = ({ product }) => (
  <div className="card">
    <div className="card-image">
      <figure className="image">
        <img src={product.thumbnail_url} alt="Placeholder image" />
      </figure>
    </div>
    <div className="card-content">
      <div className="level">
        <div className="level-left">
          <div className="level-item">
            <span className="has-text-weight-medium">{product.name}</span>
          </div>
        </div>
        <div className="level-right ml-4">
          <div className="level-item">
            <strong className="has-text-info">${product.price}</strong>
          </div>
        </div>
      </div>
      <p>
        <span className="has-text-weight-medium">Brand</span>: {product.brand}
      </p>
      <p>
        <span className="has-text-weight-medium">Sku</span>: {product.sku}
      </p>
      <p>
        <span className="has-text-weight-medium">Stock</span>: {product.stock}
      </p>
    </div>
    <div className="card-footer">
      <Link className="card-footer-item" to={`/products/${product.sku}`}>
        Config ⚙️
      </Link>
    </div>
  </div>
);

export default ProductTile;
