import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { WorkingStudentsPage } from './working-students.page';

describe('WorkingStudentsPage', () => {
  let component: WorkingStudentsPage;
  let fixture: ComponentFixture<WorkingStudentsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkingStudentsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(WorkingStudentsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
