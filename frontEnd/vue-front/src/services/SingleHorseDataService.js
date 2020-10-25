import http from "../http-common";

class SingleHorseDataService {
    getAllHorses(){
        return http.get("/horses");
    }

    getHorse(id) {
        return http.get(`horses/${id}`);
    }

    getFeed(id) {
        return http.get(`feeds/?horse_id=${id}`);
    }
    
    getSupps(id) {
        return http.get(`supplements/?horse_id=${id}`);
    }

    getTurnout(id) {
        return http.get(`turnouts/?horse_id=${id}`);
    }

    findByShortName(shortName) {
        return http.get(`/horses?short_name=${shortName}`);
    }
}

export default new SingleHorseDataService();