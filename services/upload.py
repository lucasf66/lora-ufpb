import os
from dotenv import load_dotenv
import requests
import json

def upload_csv(nameCsv):
    headers = {"Authorization": "Bearer "+f"{os.getenv('DRIVE_TOKEN')}"}
    #AUTORIZAÇÂO https://developers.google.com/oauthplayground/ >GOOGLE DRIVE API > ACESS TOKEN
    para = {
        "name":f"{nameCsv}.csv",
        "parents":["1JTyh2bONy9JUnaRagstYP03PSnnhMUSQ"] #LINK PASTA GOOGLE DRIVE 
        #EXEMPLO : https://drive.google.com/drive/folders/1JTyh2bONy9JUnaRagstYP03PSnnhMUSQ
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./"+f"{nameCsv}.csv", "rb") #SELECIONAR O ARQUIVO
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files)
    print("Upload concluido com sucesso!")