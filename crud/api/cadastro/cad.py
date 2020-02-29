from crud.database.orm_cadastro import Usuarios
from crud.utils.conector.mysql import CadastroDBContext
from crud.database import engine
import json


class Cadastro(object):

    def __init__(self):
        self.dados = None
        

    def dados_cadastro(self, dados):
        """
        Formata os dados recebidos
        """
        
        dict_ = {

        'nome': dados['nome'],
        'ddd': dados['ddd'],
        'telefone': dados['numeroTelefone'],
        'idade': dados['idade']
        }
        self.dados = dict_
        return dict_

    def consulta_usuarios_cadastrados(self):
        """
        Lista todos os usuarios cadastrados na base.
        """
        lista = []
        with CadastroDBContext(engine) as db:

            obj = db.session.query(Usuarios).all()
            for cad in obj:
                dict_ = {
                    'idUsuario': cad.idUsuario,
                    'nome': cad.nome,
                    'telefone': cad.telefone,
                    'ddd': cad.ddd,
                    'idade': cad.idade
                }
                lista.append(dict_)

            return lista
    
    def consulta_usuario(self, id_usuario):
        """
        Consulta na base um usuario cadastrados a partir de um idUsuario informado.
        """
        idUsuario = id_usuario["id_usuario"]
        try:
            with CadastroDBContext(engine) as db:
                obj = db.session.query(Usuarios).filter(Usuarios.idUsuario == idUsuario).first()
                dict_ = {
                    'idUsuario': obj.idUsuario,
                    'nome': obj.nome,
                    'telefone': obj.telefone,
                    'ddd': obj.ddd,
                    'idade': obj.idade
                }
            resposta = dict_
        except:
            resposta = {'status': False, "message": "idUsuario não encontrado.", 'status_code': 401}
        return resposta
    
    def cadastrar_usuarios(self):
        """
        Cadastra usuario na base.
        """
        dados = self.dados
        try:
            with CadastroDBContext(engine) as db:

                cad = Usuarios()
                cad.nome = dados['nome']
                cad.telefone = dados['telefone']
                cad.ddd = dados['ddd']
                cad.idade = dados['idade']
                db.session.add(cad)
                db.session.commit()

                return {
                    "status": True,
                    "msg": 'Cadastro Efetuado com sucesso.'
                }
        
        except Exception as e:
            return {
                "status": False,
                "erro": str(e),
                "msg": 'Cadastro não Efetuado.',
            }
    
    def atualiza_cadastro(self, json_data):
        """
        Atualiza cadastro do usuario referente ao idUsuario informado.
        """
        
        idUsuario = json_data["id_usuario"]
        print(json_data)
        del json_data["id_usuario"]
        try:
            with CadastroDBContext(engine) as db:
                db.session.query(Usuarios).filter(Usuarios.idUsuario == idUsuario).update(json_data)
                db.session.commit()
            resposta = {'status': True, "message": "Cadastro atulizado com sucesso.", 'status_code': 200}
        except:
            resposta = {'status': False, "message": "idUsuario não encontrado.", 'status_code': 401}
        return resposta

    def deleta_cadastro(self, id_usuario):
        """
        Deleta cadastro na base de dados a partir de um idUsuario.
        """
        idUsuario = id_usuario["id_usuario"]
        del id_usuario["id_usuario"]
        try:
            with CadastroDBContext(engine) as db:
                db.session.query(Usuarios).filter(Usuarios.idUsuario == idUsuario).delete()
                db.session.commit()
            resposta = {'status': True, "message": "Cadastro deletado com sucesso.", 'status_code': 200}
        except:
            resposta = {'status': False, "message": "idUsuario não encontrado.", 'status_code': 401}
        return resposta

