from diario import database, login_manager
from datetime import datetime
from flask_login import UserMixin
from diario import app
app.app_context().push()


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, unique=True, nullable=False)
    senha = database.Column(database.String, nullable=False)
    posts = database.relationship('Post', backref='autor', lazy=True)
    foto_perfil = database.Column(database.String, default='default.jpg')

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.String, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False )

database.create_all()