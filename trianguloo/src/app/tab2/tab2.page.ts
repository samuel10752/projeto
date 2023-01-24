import { Component } from '@angular/core';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss','../explore-container/explore-container.component.scss']
})
export class Tab2Page {

  Base : string
  Altura : string
  img : any = "assets/icon/calculo.png"
  resultado : any

  constructor(private alertController: AlertController) {}
    
    async presentAlert(result) {
      const alert = await this.alertController.create({
        header: "Area",
        subHeader: '',
        message: result,
        buttons: ['FECHAR'],
  });
  await alert.present();
}

  analisar(){
    var b = parseFloat(this.Base)
    var h = parseFloat(this.Altura)
    if ((b != 0 && h != 0) && (b + h >= 0) || (b - h <= 0)){
      this.resultado = (b*h)/2
      var result = this.resultado
      this.img = "assets/icon/fogos-de-artificio.gif"
      this.presentAlert(result)
    }
    else{
      result = "Triangulo inexitente"
      this.presentAlert(result)
      this.img = "assets/icon/alerta.png"
    }
}
}