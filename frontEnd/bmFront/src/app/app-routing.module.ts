import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', loadChildren: () => import('./pages/home/home.module').then( m => m.HomePageModule)},
  {
    path: 'login',
    loadChildren: () => import('./pages/login-page/login-page.module').then( m => m.LoginPagePageModule)
  },
  {
    path: 'registration',
    loadChildren: () => import('./pages/registration/registration.module').then( m => m.RegistrationPageModule)
  },
  {
    path: 'forgot-password',
    loadChildren: () => import('./pages/forgot-password/forgot-password.module').then( m => m.ForgotPasswordPageModule)
  },
  {
    path: 'user-landing',
    loadChildren: () => import('./user-landing/user-landing.module').then( m => m.UserLandingPageModule)
  },
  {
    path: 'barn-home',
    loadChildren: () => import('./barn-home/barn-home.module').then( m => m.BarnHomePageModule)
  },
  {
    path: 'horse-page',
    loadChildren: () => import('./horse-page/horse-page.module').then( m => m.HorsePagePageModule)
  },
  {
    path: 'working-students',
    loadChildren: () => import('./working-students/working-students.module').then( m => m.WorkingStudentsPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})

export class AppRoutingModule { }