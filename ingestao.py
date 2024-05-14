from cassandra.cluster import Cluster
import json
import uuid

# Criando a conexão com o Cassandra rodando localmente
try:
    cluster = Cluster(['4fbd167bef7f'], port=9042)
    session = cluster.connect('teste_diretor')

    # Ler o arquivo JSON
    with open('C:\\Users\\jess1\\Desktop\\Apache-Cassandra\\dados\\cf_diretor.json', 'r') as file:
        dados_json = json.load(file)

    # Verificar se a tabela existe e criar se não existir
    session.execute("""
        CREATE TABLE IF NOT EXISTS cf_diretor (
            id_diretor UUID PRIMARY KEY,
            nome_diretor text
        )
    """)

    # Iterar sobre os dados e inseri-los no banco de dados
    for dado in dados_json:
        # Supondo que o JSON tenha uma estrutura específica
        query = "INSERT INTO cf_diretor (id_diretor, nome_diretor) VALUES (?, ?)"
        session.execute(query, (uuid.uuid4(), dado['valor_coluna1']))

except Exception as e:
    print(e)
finally:
    # Fechar a conexão
    cluster.shutdown()

