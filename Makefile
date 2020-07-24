LOCAL=heroku local:run
APP=--app clayton-portfolio-website
WITH_PIPENV=pipenv run


all: load run

.PHONY: clean
clean:
	rm -rf static/
	find . -name '.DS_Store' -delete
	find . -name '*.pyc' -delete
	pipenv --rm

requirements:
	pipenv install

load: requirements static load_entries

.PHONY: static
static: requirements
	$(WITH_PIPENV) $(LOCAL) python manage.py collectstatic --no-input --no-post-process

.PHONY: load_entries
load_entries: requirements
	$(WITH_PIPENV) $(LOCAL) python manage.py load_entries

.PHONY: migrate
migrate: requirements
	$(WITH_PIPENV) $(LOCAL) python manage.py makemigrations portfolio
	$(WITH_PIPENV) $(LOCAL) python manage.py makemigrations website
	$(WITH_PIPENV) $(LOCAL) python manage.py migrate

.PHONY: run
run: requirements
	$(WITH_PIPENV) heroku local local

.PHONY: shell_plus
shell_plus:
	$(LOCAL) python manage.py shell_plus

.PHONY: prod_migrate
prod_migrate:
	heroku run $(APP) python manage.py migrate

.PHONY: prod_load
prod_load:
	heroku run $(APP) python manage.py load_entries

.PHONY: prod
prod: prod_migrate prod_load

.PHONY: prod_shell
prod_shell:
	heroku run $(APP) python manage.py shell
