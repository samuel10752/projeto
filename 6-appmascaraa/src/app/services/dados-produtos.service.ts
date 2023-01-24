import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DadosProdutosService {
  
  private produtos = [
    {id:1 , nome:'batoneira' , valor:5000.00 , quantidade: 10},
    {id:2 , nome:'capacete' , valor:110.00 , quantidade: 10},
    {id:3 , nome:'marreta' , valor:200.00 , quantidade: 5},
    {id:4 , nome:'serrote' , valor:40.00 , quantidade: 15},
  ]

  constructor() { }

  enviartodosdados() {
    return this.produtos
  }

  enviardadosid(id: number) {
    const produtoselecionado = this.produtos.filter(produto => produto.id === id)
    return  produtoselecionado[0]
  }
}
