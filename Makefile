LOCAL=heroku local:run


all: load run

.PHONY: clean
clean:
	rm -rf static/
	find . -name '.DS_Store' | xargs rm -v

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

.PHONY: prod_migrate
prod_migrate:
	heroku run python manage.py migrate

.PHONY: prod_load
prod_load:
	heroku run python manage.py load_entries

.PHONY: prod
prod: prod_migrate prod_load
