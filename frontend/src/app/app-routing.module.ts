import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { ScrapyJobsComponent } from "./scrapy-jobs/scrapy-jobs.component";
import { SearchTextComponent } from "./search-text/search-text.component";

const appRoutes: Routes = [
  { path: "", redirectTo: "/datacollection", pathMatch: "full" },
  {
    path: "datacollection",
    component: ScrapyJobsComponent
  },
  {
    path: "search",
    component: SearchTextComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
