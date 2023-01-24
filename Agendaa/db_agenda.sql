create database agenda;
use agenda;

create table Contatos(
id int auto_increment,
nome varchar(70) not null,
telefone varchar(12) not null,
email varchar(35),
primary key (id)
);