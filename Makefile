LOCAL=heroku local:run


all: load run

.PHONY: clean
clean:
	rm -rf static/

load: static load_entries

.PHONY: static
static:
	$(LOCAL) python manage.py collectstatic --no-input --no-post-process

.PHONY: load_entries
load_entries:
	$(LOCAL) python manage.py load_entries

.PHONY: migrate
migrate:
	$(LOCAL) python manage.py makemigrations portfolio
	$(LOCAL) python manage.py migrate

.PHONY: run
run:
	heroku local

.PHONY: prod
prod:
	heroku run python manage.py load_entries
	heroku run python manage.py migrate
