import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Observable} from "rxjs";

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

export interface Player {
  name: string;
  decision: string;
  id: number;
}

export interface RequestResponse {
  player1: Player;
  player2: Player;
  result: string;
  message: string;
}

@Injectable()
export class HomeService {

  constructor(private http: HttpClient) { }

  getTopFiveWinners(): any {
    return this.http.get('http://localhost:5000/top-five-winners');
  }

  startGame(params: RequestResponse): Observable<RequestResponse> {
    return this.http.post<RequestResponse>('http://localhost:5000/play-game', params, httpOptions);
  }
}
