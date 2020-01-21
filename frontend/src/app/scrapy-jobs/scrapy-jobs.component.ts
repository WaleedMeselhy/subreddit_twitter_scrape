import { Component, OnInit } from "@angular/core";
import { NgForm } from "@angular/forms";

@Component({
  selector: "app-scrapy-jobs",
  templateUrl: "./scrapy-jobs.component.html",
  styleUrls: ["./scrapy-jobs.component.css"]
})
export class ScrapyJobsComponent implements OnInit {
  constructor() {}

  ngOnInit() {}
  on_submit(form: NgForm) {
    let url = form.value.url;
    console.log(url)
    form.reset();
  }
}
