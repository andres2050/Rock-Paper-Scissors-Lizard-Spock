import { Component, OnInit } from '@angular/core';
import { HomeService, RequestResponse } from './home.service';

@Component({
  selector: 'app-home',
  providers: [HomeService],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  public topFiveWinners;
  displayedColumns: string[] = ['name', 'wins'];
  step = 0;
  player1 = '';
  player2 = '';
  errorMessage = '';
  player1Decision: string;
  player2Decision: string;
  gameResult: RequestResponse;

  constructor(private homeService: HomeService) { }

  ngOnInit(): void {
    this.getTopFiveWinners();
  }

  getTopFiveWinners(): void {
    this.homeService.getTopFiveWinners().subscribe(
      data => {this.topFiveWinners = data; },
      err => console.error(err)
    );
  }

  play(): void {
    this.step = 1;
  }

  setPlayers(): void {
    this.errorMessage = '';
    this.player1 = this.player1.trim();
    this.player2 = this.player2.trim();
    if (this.player1 === '' || this.player2 === '') {
      this.errorMessage = 'Debes ingresar ambos nombres para continuar.';
      return;
    }

    if (this.player1.toLowerCase() === this.player2.toLowerCase()) {
      this.errorMessage = 'Los nombres deben ser diferentes.';
      return;
    }

    this.step = 2;
  }

  setPlayer1Decision(p1Decision: string): void {
    this.player1Decision = p1Decision;
    this.step = 3;
  }

  setPlayer2Decision(p2Decision: string): void {
    this.player2Decision = p2Decision;
    this.step = 4;

    let request: RequestResponse;
    request = {
      player1: {
        name: this.player1,
        decision: this.player1Decision,
        id: null
      },
      player2: {
        name: this.player2,
        decision: this.player2Decision,
        id: null
      },
      result: null,
      message: null
    };

    this.homeService.startGame(request).subscribe(
      data => {this.gameResult = data; },
      err => console.error(err)
    );
  }
}
