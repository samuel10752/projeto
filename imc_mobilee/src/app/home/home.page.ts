import { Component, OnInit } from '@angular/core';
import { Guid } from 'guid-typescript'
import { Pessoa } from '../models/pesssoa.model';
import { PessoasService } from '../services/pessoas.service';


@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {
  private pessoa: Pessoa

  peso  : string
  altura : string
  escolha : string
  saida : string
  saida2 : string
  img : any = "assets/icon/favicon.png"
  
  constructor(
    private pessoaService: PessoasService
  ) {}


calcular(){
  var n1 = parseFloat(this.peso)
  var n2 = parseFloat(this.altura)
  var resultado = (n1/(n2**2)).toFixed(2)
  if (this.escolha == "Homem"){
    if (Number(resultado) <= 19){
      this.saida = resultado.toString()
      this.saida2 = "Abaixo do Peso"
      this.img =  "assets/icon/favicon.png"
    }
    if (Number(resultado) > 19 && Number(resultado) < 27.3){
      this.saida = resultado.toString()
      this.saida2 = "Peso Ideal"
      this.img =  "assets/icon/favicon.png"
    }
    if (Number(resultado) > 27.3){
      this.saida = resultado.toString()
      this.saida2 = "Acima do Peso"
      this.img =  "assets/icon/alerta.jpg"
    }
  }
  else{
    this.saida = resultado.toString()

  }
  var n1 = parseFloat(this.peso)
  var n2 = parseFloat(this.altura)
  var resultado = (n1/(n2**2)).toFixed(2)
  if (this.escolha == "Mulher"){
    if (Number(resultado) <= 19){
      this.saida = resultado.toString()
      this.saida2 = "Abaixo do Peso"
      this.img =  "assets/icon/favicon.png"
    }
    if (Number(resultado) > 19 && Number(resultado) < 27.3){
      this.saida = resultado.toString()
      this.saida2 = "Peso Ideal"
      this.img =  "assets/icon/favicon.png"
    }
    if (Number(resultado) > 27.3){
      this.saida = resultado.toString()
      this.saida2 = "Acima do Peso"
      this.img =  "assets/icon/alerta.jpg"
    }
  }
  else{
    this.saida = resultado.toString()

  }

  this.pessoa = {
    id: Guid.createEmpty(),
    peso : this.peso,
    altura : this.altura,
    sexo : this.escolha,
    saida: this.saida.toString(),
    saida2: this.saida2
    
  }
  
  
  this.pessoaService.inserir(this.pessoa)
  
}



ngOnInit(){
 
    //inicio da validação do formulario
    //this.pessoa = {id: Guid.createEmpty(), escolha:"", peso:"", altura:""}

    //this.pessoaForm = this.formBuilder.group
    //({
    //  id : [this.pessoa.id],
    //  nome : [this.pessoa.escolha,this.pessoa.altura,this.pessoa.peso, Validators.required]
    //})
    ////objeto service chama o metodo listarTodos()
    //this.pessoaService.listarTodos().then(arrayPessoa => {this.arrayPessoa = arrayPessoa})
}


}