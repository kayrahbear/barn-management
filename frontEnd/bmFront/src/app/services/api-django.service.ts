import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Storage } from '@ionic/storage';
import { Observable } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import {oAuth2ClientId, oAuth2ClientSecret, oAuth2Username, oAuth2Password, getOauthUrl, getUserUrl} from './var';

@Injectable({
  providedIn: 'root'
})

export class ApiDjangoService {
  tokenSSO: String = "";
  expireDate: any;
  networkConnected: boolean = true;
  virtualHostName: string = ''
  oAuth2ClientId = oAuth2ClientId;
  oAuth2ClientSecret = oAuth2ClientSecret;
  oAuth2Username = oAuth2Username; 
  oAuth2Password = oAuth2Password;
  appName: string = 'bm_back';
  apiPrefix = "/api";
  getOauthUrl = getOauthUrl;
  getUserUrl = getUserUrl;

  constructor(public http: HttpClient,
    public storage: Storage) {
  }

  getExpireDate() {
    return Observable.create(observer => {
      this.storage.get(this.appName + '_expireAccessToken').then((date) => {
        if (date) {
          this.expireDate = date;
          console.log("The token will expire on " + date);
          observer.next(this.expireDate);
          observer.complete();
        }
        else {
          observer.next();
          observer.complete();
        }
      })
        .catch(error => {
          observer.next();
          observer.complete();
        })
    });
  }
  checkOauthToken() {
    console.log("Lookin for a token!");
    return new Promise(resolve => {
      this.storage.get(this.appName + '_accessToken').then((result) => {
        console.log("Token found! Checkin it out" + result);
        if (result) {
          this.tokenSSO = result
          // Set expire date
          let expireFS = this.getExpireDate().subscribe((date) => {
            // check date expire
            expireFS.unsubscribe()
            let now = Date.now() / 1000;
            console.log("comparing token date:" + this.expireDate + " vs: " + now);
            if (Number(this.expireDate) < now) {
              console.log("Oh no! Expired Token! We'll look for a new one")
              resolve()
            }
            else {
              resolve(result)
            }
          })
        }
        else {
          resolve()
        }
      });
    });
  }
  getOAuthToken() {
    let url = this.getOauthUrl
    console.log("Calling for a token at: " + url);
    let body = 'client_id=' + this.oAuth2ClientId + '&client_secret=' + this.oAuth2ClientSecret + '&username=' + this.oAuth2Username + '&password=' + this.oAuth2Password + '&grant_type=password';
    const httpOptions = {
      headers: new HttpHeaders({
        'content-type': "application/x-www-form-urlencoded",
      })
    };
    return new Promise(resolve => {
      this.http.post(url, body, httpOptions)
        .pipe(
          retry(1)
        )
        .subscribe(res => {
          let token = res["access_token"];
          this.tokenSSO = token
          console.log("ok TOKEN " + token);
          let expireIn = res["expires_in"]; // Secondes
          this.expireDate = (Date.now() / 1000) + expireIn;
          // Save expireDate
          this.storage.set(this.appName + '_expireAccessToken', this.expireDate);
          this.storage.set(this.appName + '_accessToken', this.tokenSSO).then((result) => {
              resolve(token)
          })
        }, error => {
          console.log("ERROR: Couldn't get token");// Error getting the data
          console.log(error)
          resolve()
        });
    });
  }
  doSomeRequest() {
    this.http.get('https:///posts').subscribe((response) => {
      console.log(response);
    });
  }

  getUsers() {
    const options = {
      headers: new HttpHeaders({
        'Authorization': 'Bearer ' + this.tokenSSO,
        'Content-Type': 'application/json'
      })
    };
   let url = this.getUserUrl
    return Observable.create(observer => {
      // At this point make a request to your backend to make a real check!
      console.log("Getting user list from: " + url);
      this.http.get(url, options)
        .pipe(retry(1))
        .subscribe(res => {
          observer.next(res);
          observer.complete();
        }, error => {
          observer.next();
          observer.complete();
          console.log(error);// Error getting the data
        });
    });
  }
} 