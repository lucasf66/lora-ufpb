# Lora Communication

## Documentação para utilização do script de comuicação entre Lora e Raspberry

### Primeiramente faça o clone do repositório na sua máquina
    * Se não tiver o git instalado , faça a instalação *
        - sudo apt install git -y
    - git clone git@github.com:lucasf66/lora-ufpb.git lora-ufpb
    - cd lora-ufpb

### Faça a instalação das bibliotecas nescessárias do python
    
    *Já dentro do diretório lora-ufpb*
    - make install

### Agora a instalação do MARIADB e a criação do banco de dados
    
    - make database

### Criação de arquivo .env
    - Para a utilização da aplicação será nescessário criar um arquivo ".env" no diretório principal
    com os seguintes dados:
    -   SQL_HOST = localhost
        SQL_USER = root
        SQL_PASSWORD = pass <Pode ser qualquer pass. Exemplo = 1234>
        SQL_DATABASE = lora
        DRIVE_TOKEN = Token <Deverá seguir um processo *Opcionalg>


## Utilização da aplicação

### Execução
    - O modo execução recebe os dados do lora e faz a inserção no banco de dados.
    Para utilizar bastar executar :
    - python main.py -e

### Visualização
    - O modo de visualização recebe os dados do banco e mostram para o usuário.
    Para utilizar bastar executar :
    - python main.py -view

### Resetar o banco
    - O modo reset, faz o resete no banco excluindo todos os dados já inseridos
    Para utilizar bastar executar :
    - python main.py -reset

### Criação do CSV
    - Esse modo faz a criação de um arquivo csv contendo todos os dados obtidos pelos sensores.
    Para utilizar bastar executar :
    - python main.py -csv <nome do arquivo>
    - Exemplo: python main.py -csv medicao_01

### Upload no Drive
    - Serve para fazer o uploado do arquivo csv criado anteriormente no seu google drive.
    Para utilizar bastar executar :
    - python main.py -upload <nome do arquivo>
    - Exemplo: python main.py -upload medicao_01