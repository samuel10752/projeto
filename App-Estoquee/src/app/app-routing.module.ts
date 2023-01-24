import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'cadastro',
    loadChildren: () => import('./Produtos/cadastro/cadastro.module').then( m => m.CadastroPageModule)
  },
  {
    path: 'historico',
    loadChildren: () => import('./Produtos/historico/historico.module').then( m => m.HistoricoPageModule)
  },

  {
    //Isso aqui é essencial para o router pegar o id e ir pra pagina certa
    path: 'detalhes/:id',
    loadChildren: () => import('./Produtos/detalhes/detalhes.module').then( m => m.DetalhesPageModule)
  },

];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
