from flask import (
    Flask, render_template, request, redirect
)

from manter.database import Database
from manter.entities import Cliente, Fornecedor, Produto
from manter.dao import DaoCliente
from . import app, db

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/restore")
def restore():
    Database.create_db()
    db.drop_all()
    db.session.commit()
    db.create_all()
    fornecedores = []
    fornecedores.append(Fornecedor(
        nome="Lojas Americanas",
        cnpj="564513212118",
        site="www.americanas.com",
        pedidos=6))
    fornecedores.append(Fornecedor(
        nome="Amazon",
        cnpj="2345678905678",
        site="www.amazon.com",
        pedidos=1))
    fornecedores.append(Fornecedor(
        nome="Lar",
        cnpj="55512515151515151",
        site="www.lar.com",
        pedidos=0))

    for fornecedor in fornecedores:
        db.session.add(fornecedor)

    produtos = []
    produtos.append(Produto(
        nome="Aparelho 1",
        descricao="Aparelho legal.",
        preco=180.00,
        quantidade=2))
    produtos.append(Produto(
        nome="Aparelho 2 Melhor ainda",
        descricao="Faz até café",
        preco=650.00,
        quantidade=1))
    produtos.append(Produto(
        nome="Fone JBL",
        descricao="Fone BLE.",
        preco=140.00,
        quantidade=10))

    for produto in produtos:
        db.session.add(produto)

    db.session.commit()
    return redirect("/")

@app.route("/cliente/add/")
def cliente_add():
    return render_template("cadastro-cliente.html", cliente=None)

@app.route("/cliente/save", methods=["POST"])
def save():
    id = request.form.get("id")
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    cliente = Cliente(nome, cpf, email)
    dao = DaoCliente()
    if id:
        cliente.id = id
        dao.update(cliente)
    else:
        dao.save(cliente)
    return redirect("/cliente/findall/")

@app.route("/cliente/findall/")
def findall():
    dao = DaoCliente()
    clientes = dao.findall()
    return render_template("manter-cliente.html", clientes=clientes)

@app.route("/cliente/findbyname/", methods=["POST"])
def cliente_findbyname():
    nome = request.form.get("nome")
    dao = DaoCliente()
    cliente = dao.find_by_nome(nome)
    return render_template("findbyname-cliente.html", cliente=cliente)

@app.route("/cliente/edit/<id>")
def cliente_edit(id):
    dao = DaoCliente()
    cliente = dao.find_by_id(id)
    return render_template("cadastro-cliente.html", cliente=cliente)

@app.route("/delete/<id>")
def delete(id):
    dao = DaoCliente()
    dao.delete(id)
    return redirect("/cliente/findall/")

@app.route("/produto/add")
def produto_add():
    return render_template('cadastro-produto.html', produto=None)

@app.route("/produto/save", methods=["POST"])
def produto_save():
    id = request.form.get("id")
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    preco = float(request.form.get("preco"))
    quantidade = int(request.form.get("quantidade"))

    produto = Produto(
        nome=nome,
        descricao=descricao,
        preco=preco,
        quantidade=quantidade)

    produto.id = id
    db.session.merge(produto)
    db.session.commit()
    return redirect("/produto/findall/")

@app.route("/produto/findall/")
def produto_list():
    produtos = Produto.query.all()
    return render_template('manter-produto.html', produtos=produtos)

@app.route("/produto/findbyname/", methods=["POST"])
def produto_findbyname():
    nome = request.form.get("nome")
    produto = Produto.query.filter_by(nome=nome).first()
    return render_template("findbyname-produto.html", produto=produto)

@app.route("/produto/edit/<id>")
def produto_edit(id):
    produto = Produto.query.get(id)
    print(produto)
    return render_template('cadastro-produto.html', produto=produto)

@app.route("/produto/delete/<id>")
def produto_delete(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect("/produto/findall/")

@app.route("/fornecedor/add/")
def fornecedor_add():
    return render_template('cadastro-fornecedor.html', fornecedor=None)

@app.route("/fornecedor/save", methods=["POST"])
def fornecedor_save():
    id = request.form.get("id")
    nome = request.form.get("nome")
    cnpj = str(request.form.get("cnpj"))
    site = request.form.get("site")
    pedidos = int(request.form.get("pedidos"))
    f1 = Fornecedor(
        nome=nome,
        cnpj=cnpj,
        site=site,
        pedidos=pedidos)
    f1.id = id
    db.session.merge(f1)
    db.session.commit()
    return redirect("/fornecedor/findall/")

@app.route("/fornecedor/findall/")
def fornecedor_list():
    fornecedores = Fornecedor.query.all()
    return render_template("manter-fornecedor.html", fornecedores=fornecedores)

@app.route("/fornecedor/findbyid/", methods=["POST"])
def fornecedor_findbyid():
    id = request.form.get("id")
    fornecedor = Fornecedor.query.get(id)
    return render_template("findbyid-fornecedor.html", fornecedor=fornecedor)

@app.route("/fornecedor/edit/<id>")
def fornecedor_edit(id):
    fornecedor = Fornecedor.query.get(id)
    return render_template("cadastro-fornecedor.html", fornecedor=fornecedor)

@app.route("/fornecedor/delete/<id>")
def fornecedor_delete(id):
    fn = Fornecedor.query.get(id)
    db.session.delete(fn)
    db.session.commit()
    return redirect("/fornecedor/findall/")

