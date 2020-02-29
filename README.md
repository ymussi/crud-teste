# crud
Exemplo de um CRUD em API REST com Python + MySQL

# Instalação

- pip install -r requirements.txt
- python setup.py develop

# Execução

- cd crud/
- python app.py
    a API será executada em localhost:5000

# OBS

- Tenha instalado o python3 e o mysql
- configure o schema e conexão ao seu banco de dados em: 
    - crud/utils/conector/conf/production/config.ini
    - crud/utils/conector/conf/staging/config.ini
    - crud/utils/conector/conf/development/config.ini

- a api está configurada para uma a estrutura:
 - schema: cadastro
    - tables: usuario
        - coluns: idUsuario
                  nome
                  telefone
                  ddd
                  idade

- as especificações das coluns estão em:
    - crud/database/orm_cadastro.py

- Estou tentando descobirir porque não está buidando no docker, acho que é algo relacionado ao gunicorn. Fique a vontade para ajudar na correção.