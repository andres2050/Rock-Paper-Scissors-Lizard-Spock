import {Component, Input, Output, OnInit, EventEmitter} from '@angular/core';


@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.scss']
})
export class GameComponent implements OnInit {
  @Input() name: string;
  @Output() takeDecision: EventEmitter<string> = new EventEmitter();

  constructor() { }

  ngOnInit(): void {
  }

  selection(decision: string): void {
    this.takeDecision.emit(decision);
  }

}
