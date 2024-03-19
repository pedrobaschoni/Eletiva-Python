create database trabalho;
use trabalho;
drop database trabalho;

create table cliente(
	idcliente int auto_increment,
    nome varchar(60),
    endereco varchar(65),
    telefone varchar(20),
    cidade varchar(45),
    uf varchar(2),
    cep varchar(9),
    primary key(idcliente)
); 

create table venda(
	idvenda int auto_increment,
    idcliente int,
    valortotal double,
    data date,
    foreign key venda (idcliente) references cliente(idcliente),
    primary key(idvenda)
);

create table produto(
	idproduto int auto_increment,
    nome varchar(60),
    qtde int,
    preco double,
    primary key(idproduto)
);

create table itenvenda(
	idvenda int,
    idproduto int,
    qtde int,
    valor double,
    foreign key itenvenda(idvenda) references venda(idvenda),
    foreign key itenvenda(idproduto) references produto(idproduto),
    primary key(idvenda, idproduto)
);

select * from cliente;
select * from produto;
select * from venda	;
select * from itenvenda;
insert into itenvenda (idvenda, idproduto, qtde, valor) values('5','2','10','2500.0')

