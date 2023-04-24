from flask import render_template, redirect, url_for, request, flash, abort
from diario.forms import Form_criar_conta, Form_login, Form_editar_perfil, Form_criar_post, Form_editar_post
from diario import app, database, bcrypt
from diario.models import Usuario, Post
from flask_login import login_user, logout_user, current_user
import secrets
import os
from PIL import Image

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    form_login = Form_login()
    if form_login.validate_on_submit() and 'btn_submit_login' in request.form:
        usuario = Usuario.query.filter_by(username=form_login.username.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            return redirect(url_for('perfil'))
        else:
            form_login.senha.errors.append('Usuário ou senha incorretos.')
    elif current_user.is_authenticated:
        
        return redirect(url_for('perfil'))
    else:
        return render_template('login.html', form_login=form_login)
    

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    form_criar_conta = Form_criar_conta()
    if form_criar_conta.validate_on_submit() and 'btn_submit' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        username = Usuario(username=form_criar_conta.username.data, senha=senha_cript)
        database.session.add(username)
        database.session.commit()
        flash('Conta criada com sucesso! Faça Login agora mesmo!', 'success')
        return redirect(url_for('cadastro'))
    elif current_user.is_authenticated:
        return redirect(url_for('perfil'))
    else:
        return render_template('cadastro.html', form_criar_conta=form_criar_conta)

@app.route('/perfil', methods=['POST', 'GET'])
def perfil():
    if current_user.is_authenticated:
        posts = Post.query.order_by(Post.id.desc())
        num_posts = Post.query.filter_by(autor=current_user).count()
        foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
        return render_template('perfil.html', foto_perfil=foto_perfil, posts=posts, num_posts=num_posts)
    else:
        abort(403)

@app.route('/sair')
def sair():
    logout_user()
    return redirect(url_for('index'))

@app.route('/criar-post', methods=['POST', 'GET'])
def criar_post():
    form = Form_criar_post()
    if form.validate_on_submit():
        
        post = Post(titulo=form.titulo.data, corpo=form.corpo.data, autor=current_user)
        database.session.add(post)
        database.session.commit()
        flash('Post Criado com Sucesso!', 'success')
        return redirect(url_for('criar_post'))
    else:
        print(form.errors)

    return render_template('criarpost.html', form=form)

@app.route('/contato')
def contato():
    return render_template('contato.html')


def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_completo = nome + codigo + extensao
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_completo)
    tamanho = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return nome_completo

@app.route('/editar-perfil', methods=['POST', 'GET'])
def editar_perfil():
    form = Form_editar_perfil()
    foto_perfil = url_for('static', filename=f'fotos_perfil/{current_user.foto_perfil}')
    if form.validate_on_submit():
        current_user.username = form.username.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        database.session.commit()
        flash('Perfil Alterado com Sucesso!', 'success')
        return redirect(url_for('editar_perfil'))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)

@app.route('/post/<post_id>', methods=['POST', 'GET'])
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor and current_user.is_authenticated:
        form = Form_editar_post()
        if request.method == 'GET':
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            database.session.commit()
            flash('Post editado com sucesso!', 'success')
            return redirect(url_for('exibir_post', post_id=post.id))
        return render_template('post.html', post=post, form=form)
    else:
        abort(403)


@app.route('/post/<post_id>/excluir', methods=['POST', 'GET'])
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor and current_user.is_authenticated:
        database.session.delete(post)
        database.session.commit()
        flash('Post Excluido com Sucesso!', 'success')
        return redirect(url_for('perfil'))
    else:
        abort(403)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

