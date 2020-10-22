import http from "../http-common";

class SingleHorseDataService {
    getAllHorses(){
        return http.get("/horses");
    }

    getHorse(id) {
        return http.get(`horses/${id}`);
    }

    findByShortName(shortName) {
        return http.get(`/horses?short_name=${shortName}`);
    }

    

}

export default new SingleHorseDataService();