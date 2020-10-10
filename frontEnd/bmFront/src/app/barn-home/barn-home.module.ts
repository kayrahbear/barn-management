import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { BarnHomePageRoutingModule } from './barn-home-routing.module';

import { BarnHomePage } from './barn-home.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    BarnHomePageRoutingModule
  ],
  declarations: [BarnHomePage]
})
export class BarnHomePageModule {}
