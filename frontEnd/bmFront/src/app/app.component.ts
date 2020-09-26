import { Component } from '@angular/core';
import { Storage } from '@ionic/storage';
import { Platform } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { ApiDjangoService } from '../app/services/api-django.service'


@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})


export class AppComponent {
  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    public apiService: ApiDjangoService,
    public storage : Storage
  ) {
    this.initializeApp();
  }
  accessAuthorizedWithUrl() {
    //Aks list of users
    this.apiService.getUsers().subscribe((list)=>{
      console.log(JSON.stringify(list))
    })
  }
  getToken() {
    console.log("Didn't find a token, friend ")
    this.apiService.checkOauthToken().then((token) => {
      if (token) {
        console.log("Got a token: "+token+" Saving token locally: "+token)
        this.accessAuthorizedWithUrl()
      }
      else {
        // Get token
        this.apiService.getOAuthToken().then((token) => {
          if (token) {
            console.log("Got a token: "+token+" Saving token locally: "+token)
            this.accessAuthorizedWithUrl()
          }
          else {
              console.log("Token error!"); 
          }
        });
      }
    });
  }
  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
      // check if we have a token to use API
      this.apiService.checkOauthToken().then((result) => {
        if (result) {
          console.log("Token found and approved! " + result);
          this.accessAuthorizedWithUrl()
        }
        else {
          console.log("No token found! Go get it!")
          this.getToken()
        }
      });
    });
  }
  
}