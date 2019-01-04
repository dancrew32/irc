build:
	docker-compose build # --no-cache

run:
	docker-compose up

remove:
	docker-compose rm -f bot
	docker-compose rm -f db
	rm -rf postgres

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