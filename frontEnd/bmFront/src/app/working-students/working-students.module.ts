import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { WorkingStudentsPageRoutingModule } from './working-students-routing.module';

import { WorkingStudentsPage } from './working-students.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    WorkingStudentsPageRoutingModule
  ],
  declarations: [WorkingStudentsPage]
})
export class WorkingStudentsPageModule {}
