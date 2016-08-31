all: static load_entries

.PHONY: static
static:
	python manage.py collectstatic --no-input

.PHONY: load_entries
load_entries:
	python manage.py load_entries

.PHONY: migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate
