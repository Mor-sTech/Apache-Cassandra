# Apache-Cassandra
Repositório referente a utilização do Apache Cassandra no Projeto.

Instalação do Cassandra realizada via Docker:

Utilizar comandos:
- docker pull cassandra
- docker run 7000:7000 -p 7001:7001 -p 7199:7199 -p 9042:9042 -p 9160:9160 --name cassandra -d cassandra:latest

Verifique o funcionamento do container com esse comando:
- docker ps

##########################################################################################################

Gerenciador de Banco utilizado: [DevCenter](https://downloads.datastax.com/#devcenter)

Conexão utilizada:
	Connection name: localhost
	Contact hosts: localhost
	Native Protocol port: 9042
