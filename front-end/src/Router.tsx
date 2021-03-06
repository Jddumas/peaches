import React from "react";
import { Switch, Route } from "react-router-dom";
import { HomePage, ProductPage, ItemPage, ProductDetail } from "./pages";
const AppRouter: React.FunctionComponent = () => (
  <Switch>
    <Route exact path="/">
      <HomePage />
    </Route>
    <Route
      path="/products/:sku"
      children={<ProductDetail></ProductDetail>}
    ></Route>
    <Route path="/products">
      <ProductPage></ProductPage>
    </Route>
    <Route path="/items">
      <ItemPage></ItemPage>
    </Route>
  </Switch>
);

export default AppRouter;
