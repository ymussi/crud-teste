from flask_restplus import fields
from crud.api import api


schemaCadastro = api.model('Cadastro', {
    'nome': fields.String(description='Nome Completo'),
    'numeroTelefone': fields.String(description='Número do telefone.'),
    'ddd': fields.String(description='DDD'),
    'idade': fields.String(description='Idade')
})

schemaUpdate = api.model('Update', {
    'id_usuario': fields.String(description='ID'),
    'nome': fields.String(description='Nome Completo'),
    'telefone': fields.String(description='Número do telefone.'),
    'ddd': fields.String(description='DDD'),
    'idade': fields.String(description='Idade')
})

schemaConsulta = api.model('Consulta', {
    'id_usuario': fields.String(description='ID')
})

schemaDelete = api.model('Delete', {
    'id_usuario': fields.String(description='ID')
})

