import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DadosProdutosService } from 'src/app/services/dados-produtos.service';

@Component({
  selector: 'app-detalhes-produtos',
  templateUrl: './detalhes-produtos.page.html',
  styleUrls: ['./detalhes-produtos.page.scss'],
})
export class DetalhesProdutosPage implements OnInit {

  public produtoselecionado : any

  constructor(
    private route : ActivatedRoute,
    private produto : DadosProdutosService
  ) { }

  ngOnInit() {
    const id: number = Number (this.route.snapshot.paramMap.get('id'))
    this.produtoselecionado = this.produto.enviardadosid(id)

  }

  

}
