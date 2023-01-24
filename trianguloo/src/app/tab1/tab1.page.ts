import { Component } from '@angular/core';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss','../explore-container/explore-container.component.scss']
})
export class Tab1Page {
  num1 : string
  num2 : string
  num3 : string
  saida : string
  img : any = "assets/icon/calculadora.gif"
  constructor() {}

  analisa(){
  var a = parseFloat(this.num1)
  var b = parseFloat(this.num2)
  var c = parseFloat(this.num3)

  if ((a + b) > c && (a + c) > b && (b + c) > a){

    if ((a != b) && (a != c) && (b !=c)){
      this.saida = " Triangulo  Escaleno"
      this.img = "assets/icon/escaleno.png"
      }

    else if ((a == b) && (a == c) && (b == c)) {
      this.saida = " Triangulo Equilatero"
      this.img = "assets/icon/equilatero.png"  
    }

    else{
      this.saida = " Triangulo Isosceles"
      this.img = "assets/icon/isosceles.png"
    }
  }

  else{
    this.saida  = "Triangulo Não Existe"
    this.img = "assets/icon/alerta.png"
  }
}
}

