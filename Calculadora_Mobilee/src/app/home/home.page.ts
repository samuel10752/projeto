import { Component } from '@angular/core';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {

  num1 : string
  num2 : string
  saida : string

  constructor(private alertController: AlertController) {}

  async presentAlert(op:string, nome: string) {
    const alert = await this.alertController.create({
      header: nome,
      subHeader: this.num1 + op + this.num2,
      message: this.saida,
      buttons: ['FECHAR'],
    });

    await alert.present();
  }

  somar(){
    var nome = "Soma"
    var op = " + "
    var n1 = parseFloat(this.num1)
    var n2 = parseFloat(this.num2)
    var soma = n1 + n2
    this.saida = soma.toString()
    this.presentAlert(op, nome)
  }
  

  subtrair(){
    var nome = "Subtração"
    var op = " - "
    var n1 = parseFloat(this.num1)
    var n2 = parseFloat(this.num2)
    var subtracao = n1 - n2
    this.saida = subtracao.toString()
    this.presentAlert(op, nome)
  }

  dividir(){
    var nome = "Divisão"
    var op = " / "
    var n1 = parseFloat(this.num1)
    var n2 = parseFloat(this.num2)
    if (n2!=0){
      var divisao = n1 / n2
      this.saida = divisao.toString()
      this.presentAlert(op, nome)
    }
      else{
        this.saida = "Não existe divisão por ZERO"
        this.presentAlert(op, nome)
    }
  }

  multiplicar(){
    var nome = "Multiplicação"
    var op = " * "
    var n1 = parseFloat(this.num1)
    var n2 = parseFloat(this.num2)
    var multiplicacao = n1 * n2
    this.saida = multiplicacao.toString()
    this.presentAlert(op, nome)
  }
  
}