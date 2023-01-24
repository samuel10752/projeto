import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DadosProdutosService } from 'src/app/services/dados-produtos.service';

@Component({
  selector: 'app-detalhes-produtos',
  templateUrl: './detalhes-produtos.page.html',
  styleUrls: ['./detalhes-produtos.page.scss'],
})
export class DetalhesProdutosPage implements OnInit {

  // img : any = "assets/icon/aliamento.gif"
  img_1 : any = "assets/icon/rodas.png"

  public produtoselecionado : any
  public modoDeEdicao = false
 

  constructor(
    private route : ActivatedRoute,
    private produto : DadosProdutosService
  ) { }

  iniciarEdicao() {
    this.modoDeEdicao = true
  }

  encerrarEdicao() {
    const id: number = Number (this.route.snapshot.paramMap.get('id'))
    if (id > 0 ){

      this.modoDeEdicao = false
    } else {
      this.produto.recebeDados(this.produtoselecionado)
      this.modoDeEdicao = false
    }
  }


  ngOnInit() {
    const id: number = Number (this.route.snapshot.paramMap.get('id'))
    if (id > 0 ){
       this.produtoselecionado = this.produto.enviardadosid(id)
    } else{

    this.produtoselecionado = {id , nome: "", valor: 0.0, garantia: 0}
    this.modoDeEdicao= true
    }
  }
 
  deletarServico(){
    this.produto.deletaDados(this.produtoselecionado)
  }

}
