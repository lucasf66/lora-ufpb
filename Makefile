TAG=3.2

install:
	pip install -r requirements.txt

lint:
	flake8 .

run:
	python main.py

database:
	sudo chmod 755 ./scripts/create_database.sh
	bash ./scripts/create_database.sh