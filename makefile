build:
	docker-compose build # --no-cache

run:
	docker-compose up

remove:
	docker-compose rm -f bot
	docker-compose rm -f db
	rm -rf postgres

bot:
	docker-compose exec bot bash

pep:
	pip install autopep8
	autopep8 -i app/bot.py app/app.py app/db.py

psql:
	docker-compose exec db psql -U ${IRC_DB_USER}

top_channels:
	docker-compose exec db psql -U ${IRC_DB_USER} \
	-c 'SELECT channel, COUNT(*) FROM message GROUP BY 1 ORDER BY 2 DESC;'

top_who:
	docker-compose exec db psql -U ${IRC_DB_USER} \
	-c 'SELECT who, COUNT(*) FROM message GROUP BY 1 ORDER BY 2 DESC LIMIT 100;'

dump_messages:
	docker-compose exec db pg_dump -U ${IRC_DB_USER} -d ${IRC_DB_NAME} -t message > sql/message.sql

load_messages:
	docker-compose exec db psql -U ${IRC_DB_USER} -d ${IRC_DB_NAME} -f sql/message.sql