import React, { ReactElement } from "react";
import { Product } from "../entity";

interface ProductTableProps {
  products: Product[];
  headers?: Array<keyof Product>; //Array of keys in object typed Product
  headersFormatter?: (name: keyof Product) => string;
  cellFormatter?: (data: any, header: keyof Product) => ReactElement;
  onActionClicked?: (product: Product) => void;
}

const ProductTable: React.VFC<ProductTableProps> = ({
  products,
  headers = [],
  headersFormatter = (s) => s.replaceAll(/_/g, " "),
  cellFormatter = (data, header) => <span>{data}</span>,
  onActionClicked = (p) => p,
}) => {
  if (headers.length < 1) {
    return <div>No keys selected</div>;
  }
  if (products.length < 1) {
    return <div>Empty table</div>;
  }

  return (
    <div className="table-container">
      <table className="table is-narrow is-bordered">
        <thead>
          <tr className="has-text-capitalized">
            {headers.map((header) => (
              <th>{headersFormatter(header)}</th>
            ))}
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {products.map((p) => (
            <tr>
              {headers.map((header) => (
                <td>{cellFormatter(p[header], header)}</td>
              ))}
              <td>
                <button onClick={() => onActionClicked(p)} className="button">
                  ⚙️
                </button>
              </td>
            </tr>
          ))}
        </tbody>
        <tfoot></tfoot>
      </table>
    </div>
  );
};

export default ProductTable;
