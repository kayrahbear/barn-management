import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { HorsePagePageRoutingModule } from './horse-page-routing.module';

import { HorsePagePage } from './horse-page.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HorsePagePageRoutingModule
  ],
  declarations: [HorsePagePage]
})
export class HorsePagePageModule {}
