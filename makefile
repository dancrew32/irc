make:
	vim makefile

venv:
	virtualenv -p python3 venv

deps:
	./venv/bin/pip3 install -r requirements.txt

pep:
	./venv/bin/autopep8 -i bot.py app.py

run:
	./venv/bin/python app.py
