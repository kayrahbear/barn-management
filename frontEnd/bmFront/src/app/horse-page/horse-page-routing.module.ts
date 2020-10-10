import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HorsePagePage } from './horse-page.page';

const routes: Routes = [
  {
    path: '',
    component: HorsePagePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HorsePagePageRoutingModule {}
