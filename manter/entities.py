from datetime import datetime
from sqlalchemy import (Column, Integer, String, Boolean, Float)
import site
from webapp import db

Base = db.Model

class Fornecedor(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    site = Column(String(120), nullable=True)
    pedidos = Column(Integer, default=0)
    datetime = Column(String(120), default=datetime.now())

    def __repr__(self):
        return f"{self.id} - {self.nome} - {self.cnpj} - {self.site} - {self.pedidos} - {self.datetime}"

class Produto(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String(120), nullable=False)
    descricao = Column(String(120), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)
    datetime = Column(String(120), default=datetime.now())

    def __repr__(self):
        return f"{self.id} - {self.nome} - {self.descricao} - {self.preco} - {self.quantidade} - {self.datetime}"

class Cliente:
    def __init__(self, nome, cpf, email):
        """ init eh o construtor """
        self.nome = nome
        self.cpf = cpf
        self.email = email

    def exibir(self):
        print(self.nome, self.cpf, self.email)

class ProdutoOld:
    def __init__(self, nome, descricao, preco, quantidade):
        """ init eh o construtor """
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def exibir(self):
        print(self.nome, self.descricao, self.preco, self.quantidade)


if __name__ == '__main__':
    maria = Cliente("Maria", 4254242, "maria@gmail.com")
    julia = Cliente("Julia", 114524, "julia@org.com")
    print(maria.cpf)