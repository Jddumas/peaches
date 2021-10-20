import React from "react";
import ProductTable from "../components/ProductTable";
import { useRecoilValueLoadable } from "recoil";
import { productsAtom } from "../recoil/productAtoms";
import { Product } from "../entity";

const ProductPage: React.FunctionComponent = () => {
  const getAllProductCall = useRecoilValueLoadable(productsAtom);
  const loadingState = getAllProductCall.state;
  if (loadingState === "loading") {
    return <div>Loading...</div>;
  } else if (loadingState === "hasError") {
    return (
      <div className="has-text-danger"> {getAllProductCall.contents} </div>
    );
  }
  const productListing = Object.values(getAllProductCall.contents);

  if (productListing.length < 1) {
    return (
      <section className="section">
        <p>No products</p>
      </section>
    );
  }

  const headers = Object.keys(productListing[0]) as Array<keyof Product>;
  return (
    <section className="section">
      <p className="title">This is product page</p>
      <p className="subtitle">Under construction, coming</p>

      <div>
        <ProductTable
          products={productListing}
          headers={headers}
          onActionClicked={(p) => alert(`You've clicked ${p.sku}`)}
        ></ProductTable>
      </div>
    </section>
  );
};
export default ProductPage;
