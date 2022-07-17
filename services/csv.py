from multiprocessing import connection
from services.connector import Database

def create_csv(name):
    connection = Database.received()
    received = connection.cursor()
    querry = "SELECT * FROM data"
    received.execute(querry)
    print(received)
    filename=str(name)+".csv"
    file = open(filename,"a")
    file.write("Umidade,Temperatura,CO,Horario,Dia\n")
    file.close()
    for(temperatura,umidade,co,hora,dia) in received:
        data = (f"{temperatura},{umidade},{co},{hora},{dia}")
        file = open(filename,"a")
        file.write(data+"\n")
        file.close()
    received.close
    print("Arquivo "+name+".csv criado com sucesso!!")