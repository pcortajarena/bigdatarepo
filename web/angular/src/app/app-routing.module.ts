import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SearchInputComponent } from './components/search-input/search-input.component';
import { routeNames } from './route-names';


const routes: Routes = [
  { path: '', component: SearchInputComponent, pathMatch: 'full' },
  { path: '**', component: SearchInputComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
