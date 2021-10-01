import React from "react";
import ProductTile from "../components/ProductTile";
import { mockProducts } from "../mocks/mock_data";
import { useRecoilValueLoadable } from "recoil";
import { productsAtom } from "../recoil/productAtoms";

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

  return (
    <section className="section">
      <p className="title">This is product page</p>
      <p className="subtitle">Under construction, coming</p>

      <div className="columns is-multiline">
        {productListing.map((p) => (
          <div className="column is-3">
            <ProductTile product={p} />
          </div>
        ))}
      </div>
    </section>
  );
};
export default ProductPage;
