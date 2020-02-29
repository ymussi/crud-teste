from flask_restplus import Resource
from flask import request, jsonify
from crud.api import api
from crud.api.cadastro.schemas import schemaCadastro, schemaConsulta, schemaDelete, schemaUpdate
from crud.api.cadastro.cad import Cadastro
import logging
import json


log = logging.getLogger(__name__)

ns = api.namespace(
    'cadastro', description='CRUD no MySQL')


@ns.route('/cadastrar')
class Create(Resource):
    @ns.response(code=400, description="Bad Request")
    @ns.expect(schemaCadastro, validate=True)
    def post(self):
        """
        Faz um cadastro simples na base de dados
        """

        dados = request.json
        r = Cadastro()
        r.dados_cadastro(dados)
        res = r.cadastrar_usuarios()

        return res

@ns.route('/consultar')
class Read(Resource):
    @ns.response(code=400, description="Bad Request")
    @ns.expect(schemaConsulta, validate=True)
    def post(self):
        """
        Consulta o cadastro de um usuario na base a partir de um idUsuario.
        """
        id_usuario = request.json
        r = Cadastro()
        res = r.consulta_usuario(id_usuario)

        return res

@ns.route('/listar')
class List(Resource):
    @ns.response(code=400, description="Bad Request")
    def get(self):
        """
        Lista todos os cadastros na base.
        """
        r = Cadastro()
        res = r.consulta_usuarios_cadastrados()

        return res

@ns.route('/atualizar')
class Update(Resource):
    @ns.response(code=400, description="Bad Request")
    @ns.expect(schemaUpdate, validate=True)
    def put(self):
        """
        Atualiza um cadastro a partir de um idUsuario.
        """
        dados_cadastro = request.json
        r = Cadastro()
        res = r.atualiza_cadastro(dados_cadastro)

        return res

@ns.route('/deletar')
class Delete(Resource):
    @ns.response(code=400, description="Bad Request")
    @ns.expect(schemaDelete, validate=True)
    def delete(self):
        """
        Deleta um cadastro referente ao idUsuario informado.
        """
        id_usuario = request.json
        r = Cadastro()
        res = r.deleta_cadastro(id_usuario)

        return res

