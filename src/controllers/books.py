from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'Title': 'War  and piece'},
    {'id': 1, 'Tiitle': 'Clean Code'}
]

@api.route('/books')
class Booklist(Resource):
    def get(self, ):
        return books_db

    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200
        