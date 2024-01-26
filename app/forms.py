from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
import sqlalchemy as sa
from app import db
from app.models import User



class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar Me')
    submit = SubmitField('Login')
    
    
    
class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    password2 = PasswordField(
        'Confirme a senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Please use a different email address.')
        
        
        
# editor de perfil
class EditProfileForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    about_me = TextAreaField('Sobre mim', validators=[Length(min=0, max=140)])
    submit = SubmitField('Salvar')
    
    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == self.username.data))
            if user is not None:
                raise ValidationError('Please use a different username.')
            
            
class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')