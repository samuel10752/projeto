import { Component } from '@angular/core';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss','../explore-container/explore-container.component.scss']
})
export class Tab3Page {

  num1 : string
  num2 : string
  num3 : string
  saida : any
  img : any = "assets/icon/alvo.gif"

  constructor() {}

  analisar(){
    var a = parseFloat(this.num1)
    var b = parseFloat(this.num2)
    var c = parseFloat(this.num3)

    if ((a + b) > c && (a + c) > b && (b + c) > a){
      
      var p = (a+b+c)/2
      var area = ((p*(p-a)*(p-b)*(p-c))**(0.5)).toFixed(2)
      
      this.saida = area
      this.img = "assets/icon/gostar.gif"
    }
    else{
      this.saida ="Triangulo não existe!!"
      this.img = "assets/icon/alerta.png"
    }
  }
}