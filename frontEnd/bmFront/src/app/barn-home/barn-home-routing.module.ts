import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BarnHomePage } from './barn-home.page';

const routes: Routes = [
  {
    path: '',
    component: BarnHomePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class BarnHomePageRoutingModule {}
