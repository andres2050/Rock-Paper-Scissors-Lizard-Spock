import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class HomeService {

  constructor(private http: HttpClient) { }

  getTopFiveWinners(){
    return this.http.get('http://localhost:5000/top-five-winners');
  }
}
