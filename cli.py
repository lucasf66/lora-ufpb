import argparse
import sys
from services.insert_mysql import insertMysql
from services.connector import Database
from services.csv import create_csv
from services.upload import upload_csv

def check_args():
    if len(sys.argv)<2:
       return True
    else:
        return False 

def checkArgv(argument):
    if (any(element in argument for element in sys.argv)):
        if((argument=='-csv') or (argument=='-upload')):
            cont=0
            global nameCsv
            for x in sys.argv:
                try:
                    if((argument=='-csv') or (argument=='-upload')): #CONFERE SE EXISTE CSV E UPLOAD
                        nameCsv=sys.argv[(cont)]
                        cont+=1
                except:
                    nameCsv="data"
    else:
        return False
    return True

def parse_args():
    parser = argparse.ArgumentParser(description="CLI para utilização do LoRa")
    parser.add_argument('-e',"-execute",nargs="?",
                        help="MODO EXECUÇÂO \n Recebe os dados e insere no banco de dados")
    parser.add_argument('-csv',"-csv",nargs="?",
                        help="Faz a conversão para .csv dos dados inseridos no banco")
    parser.add_argument("-r",'-reset', nargs="?",
                        help="Reseta o banco apagando todos os dados")

    parser.add_argument("-v",'-view', nargs="?",
                        help="Mostra todos os dados já inseridos")
    
    parser.add_argument("-up",'-upload', nargs="?",
                        help="Faz o upload para o Google Drive")
    if check_args():
        print('Error: Insira um argumento válido')
        parser.print_help()

    return parser, parser.parse_args()


def main():
    parser, args = parse_args()
    if(checkArgv('-e')):
        print("EM MODO DE EXECUÇÂO") 
        insertMysql()
    elif(checkArgv('-csv')):
        print("CRIANDO CSV")
        create_csv(nameCsv)
    elif(checkArgv('-reset')):
        Database.reset()
    elif(checkArgv('-view')):
        Database.view()
    elif(checkArgv('-upload')):
        upload_csv(nameCsv)