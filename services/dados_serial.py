import serial
import datetime

def dados():
    #Conexão serial
    #Timeout = Tempo de execução em Segundos
    dict_dados = {'temperatura':[],
                'umidade':[],
                'co':[],
                'hora':[],
                'dia':[]}

    #Exemplo de entrada de dados = b'60,30,200'
    ser = serial.Serial("/dev/ttyS0",timeout=1)#Timeout = Tempo de execução em Segundos
    if(ser.inWaiting()>0):
        timeAll=datetime.datetime.now()
        time=(str(timeAll.hour)+":"+str(timeAll.minute)+":"+str(timeAll.second))
        get_dados=((str(ser.readline())).split("'"))[1].split(",")
        dict_dados['hora'].append(time)
        dict_dados['dia'].append(datetime.date.today())
        dict_dados['temperatura'].append(get_dados[0])
        dict_dados['umidade'].append(get_dados[1])
        dict_dados['co'].append(get_dados[2])
    return dict_dados