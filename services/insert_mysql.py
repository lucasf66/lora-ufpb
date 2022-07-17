from services.dados_serial import dados
from services.connector import Database
def insertMysql():
    cont = 0
    try:
        print("Dados recebidos:")
        print("Umidade , Temperatura , CO , Hora , Dia ")
        while (cont<=5):
            cont+=1
            data = dados()
            insert_coluna = ""
            insert_dado = ""
            for key,value in data.items():
                insert_coluna+=str(key)+","
                insert_dado+='"'+str(value[0])+'",'
            sql='INSERT INTO data ('+insert_coluna[:-1]+') VALUES ('+insert_dado[:-1]+')'
            print(sql)
            Database.insert(sql)
    except KeyboardInterrupt:
        print("PROCESSO INTERROMPIDO")