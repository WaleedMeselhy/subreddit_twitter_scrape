import { Component, OnInit } from "@angular/core";
import { NgForm } from "@angular/forms";
import { HttpClient, HttpParams } from "@angular/common/http";

@Component({
  selector: "app-search-text",
  templateUrl: "./search-text.component.html",
  styleUrls: ["./search-text.component.css"]
})
export class SearchTextComponent implements OnInit {
  items: [];
  constructor(private http: HttpClient) {}

  ngOnInit() {}
  on_search(form: NgForm) {
    let text = form.value.text;
    let searchParams = new HttpParams();
    searchParams = searchParams.append("text", text);
    this.http
      .get("http://localhost:5000/search/", {
        params: searchParams
      })
      .subscribe(response => {
        this.items = response['hits']['hits']
      });
  }
}
