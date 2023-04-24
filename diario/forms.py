from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from diario.models import Usuario
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class Form_criar_conta(FlaskForm):
    username = StringField('Nome de usuario:', validators=[DataRequired()])
    senha = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    confirm_senha = PasswordField('Confirme a senha:', validators=[DataRequired(), EqualTo('senha')])
    btn_submit = SubmitField('Criar conta')
    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError('Usuario já cadastrado.')

        
class Form_login(FlaskForm):
    username = StringField('Nome de usuario:', validators=[DataRequired()])
    senha = PasswordField('Senha:', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso?')
    btn_submit_login = SubmitField('Fazer login')

class Form_editar_perfil(FlaskForm):
    username = StringField('Nome de usuario:', validators=[DataRequired()])
    foto_perfil = FileField('Atualizar foto', validators=[FileAllowed(['jpg', 'png'])])
    btn_submit_edit_perfil = SubmitField('Salvar Edição')
    def validate_username(self, username):
        if current_user.username != username.data:
            usuario = Usuario.query.filter_by(username=username.data).first()
            if usuario:
                raise ValidationError('Usuario já cadastrado.')
            
class Form_criar_post(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    corpo = TextAreaField('Escreva aqui:', validators=[DataRequired()])
    btn_submit = SubmitField('Salvar')

class Form_editar_post(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    corpo = TextAreaField('Escreva aqui:', validators=[DataRequired()])
    btn_submit = SubmitField('Salvar')