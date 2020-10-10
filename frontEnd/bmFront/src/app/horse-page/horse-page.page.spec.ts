import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { HorsePagePage } from './horse-page.page';

describe('HorsePagePage', () => {
  let component: HorsePagePage;
  let fixture: ComponentFixture<HorsePagePage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HorsePagePage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(HorsePagePage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
