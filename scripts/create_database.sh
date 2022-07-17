#!/bin/bash
Red='\033[0;31m'
NC='\033[0m'
password=1234  #Inserir sua senha aqui
user='root'
echo -e "${Red}installing MARIADB${NC}"
sudo apt install mariadb-server -y
sudo apt autoremove -y
sudo mysql --password=$password -e "ALTER USER '${user}'@'localhost' \
IDENTIFIED BY '${password}';
FLUSH PRIVILEGES;"
echo -e "${Red}Creating database : lora${NC}"
sudo mysql --password=$password -e "create database lora"
echo -e "${Red}Creating table : data [temperatura,umidade,co,hora,dia]${NC}"
sudo mysql --password=$password -D "lora" -e "create table data( \
temperatura VARCHAR(20),\
umidade VARCHAR(20),\
co VARCHAR(20),\
hora VARCHAR(20),\
dia VARCHAR(20))"

echo -e "${Red}Database was create successfully!!${NC}"
echo -e "${Red}-------TABLE DATA---------!${NC}"
sudo mysql --password=$password -D "lora" -e "desc data"