import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DadosProdutosService {

  private produtos = [
    {id:1 , nome:'Alinhamento' , valor:150.00 , garantia: 12 },
    {id:2 , nome:'Balanceamento' , valor:180.00 , garantia: 10 },
    {id:3 , nome:'Revisão de freios' , valor:200.00, garantia: 3  },
    {id:4 , nome:'Revisão de Suspensão' , valor:220.00 , garantia: 3  },
  ]

  constructor() { }

  enviartodosdados() {
    return this.produtos
  }

  recebeDados(dadosRecebidos : any){
    dadosRecebidos.id = this.produtos.length + 1
    this.produtos.push(dadosRecebidos)
  }

  enviardadosid(id: number) {
    const produtoselecionado = this.produtos.filter(produto => produto.id === id)
    return  produtoselecionado[0]
  }

  deletaDados(dadosRecebidos : any){ 
    this.produtos.splice(this.produtos.indexOf(dadosRecebidos), 1)
  }
}