import http from "../http-common";

class HorseDataService {
    getAll(){
        return http.get("/horses");
    }

    get(id) {
        return http.get(`horses/${id}`);
    }

    findByShortName(shortName) {
        return http.get(`/horses?short_name=${shortName}`);
      }

}

export default new HorseDataService();