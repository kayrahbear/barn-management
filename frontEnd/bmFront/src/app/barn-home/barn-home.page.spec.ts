import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { BarnHomePage } from './barn-home.page';

describe('BarnHomePage', () => {
  let component: BarnHomePage;
  let fixture: ComponentFixture<BarnHomePage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BarnHomePage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(BarnHomePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
