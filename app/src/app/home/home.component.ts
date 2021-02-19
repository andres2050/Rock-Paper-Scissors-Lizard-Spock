import { Component, OnInit } from '@angular/core';
import { HomeService } from './home.service';

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
    console.log(this.player1, this.player2);
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
}
