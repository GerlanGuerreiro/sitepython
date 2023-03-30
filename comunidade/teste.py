from comunidade import app, database
from models import Usuario, Post
#
# # if __name__ == '__main__':
# #     app.run(debug=True)
#
#
# # with app.app_context():
# #     database.create_all()
#
# usuario = Usuario()

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
#
# database = SQLAlchemy()
# app = Flask(__name__)
#
#
# import os
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
#
# database.init_app(app)
#
# class Usuario(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     username = database.Column(database.String, nullable=False)
#     email = database.Column(database.String, nullable=False, unique=True)
#     senha = database.Column(database.String, nullable=False)
#     foto_perfil = database.Column(database.String, default='default.jpg')
#     posts = database.relationship('Post', backref='autor', lazy=True)
#     cursos = database.Column(database.String, nullable=False, default='Não Informado')
#
#
# class Post(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     titulo = database.Column(database.String, nullable=False)
#     corpo = database.Column(database.Text, nullable=False)
#     data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
#     id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)

with app.app_context():
    # database.create_all()
    Usuario.query.all()
    users = Usuario.query.first()
    print(users.email)
    print(users.senha)
