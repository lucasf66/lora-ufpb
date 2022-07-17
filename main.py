from services.connector import Database
from services.dados_serial import dados
#---------RECEBENDO DADOS-------
data = dados() # a function dados() retorna um dicionario com
               # Temperatura,umidade,co,hora,dia

#---------INSERIR NO BANCO-------