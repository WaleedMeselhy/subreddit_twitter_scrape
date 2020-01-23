import { BrowserModule } from "@angular/platform-browser";
import { HttpClientModule } from "@angular/common/http";
import { NgModule } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { AppComponent } from "./app.component";
import { HeaderComponent } from "./header/header.component";
import { AppRoutingModule } from "./app-routing.module";
import { ScrapyJobsComponent } from "./scrapy-jobs/scrapy-jobs.component";
import { SearchTextComponent } from './search-text/search-text.component';
import { SearchResultItemComponent } from './search-text/search-result-item/search-result-item.component';

@NgModule({
  declarations: [AppComponent, HeaderComponent, ScrapyJobsComponent, SearchTextComponent, SearchResultItemComponent],
  imports: [BrowserModule, AppRoutingModule, FormsModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {}
