import axios from "axios";

export default axios.create({
  baseURL: "https://bm-back-hvrl7rzdpq-uc.a.run.app/api",
  headers: {
    "Content-type": "application/json"
  }
});
