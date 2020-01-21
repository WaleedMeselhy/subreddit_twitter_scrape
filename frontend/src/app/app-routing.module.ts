import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { ScrapyJobsComponent } from './scrapy-jobs/scrapy-jobs.component';

const appRoutes: Routes = [
  { path: "", redirectTo: "/datacollection", pathMatch: "full" },
  {
    path: "datacollection",
    component: ScrapyJobsComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
