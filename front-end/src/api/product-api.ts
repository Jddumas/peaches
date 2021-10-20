import axios from "axios";
import { Product } from "../entity";

class ProductAPI {
  client = axios.create({});

  async getAll(): Promise<{ [k: string]: Product }> {
    // may throw if network code is 4xx or 5xx
    const result = await this.client.get("/api/products");
    return await result.data;
  }
  getBySku() {}
  update() {}
  create() {}
  delete() {}
}

export default new ProductAPI();
