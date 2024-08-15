start:
	python3 manage.py runserver --settings=config.settings.dev
dev-makem:
	python3 manage.py makemigrations --settings=config.settings.dev
dev-showm:
	python3 manage.py showmigrations --settings=config.settings.dev

dev-sqlm:
	python3 manage.py sqlmigrate $(A) $(m) --settings=config.settings.dev

dev-m:
	python3 manage.py migrate --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

dev-shell:
	python3 manage.py shell --settings=config.settings.dev

dev-dbshell:
	python3 manage.py dbshell --settings=config.settings.dev

# --------------------
# Test               |
# -------------------- 
test-start:
	python3 manage.py runserver --settings=config.settings.tests
test-makem:
	python3 manage.py makemigrations --settings=config.settings.tests
test-showm:
	python3 manage.py showmigrations --settings=config.settings.tests

test-sqlm:
	python3 manage.py sqlmigrate $(A) $(m) --settings=config.settings.tests

test-m:
	python3 manage.py migrate --settings=config.settings.tests

test-install:
	pip install -r requirements/dev.txt

test-shell:
	python3 manage.py shell --settings=config.settings.tests

test-dbshell:
	python3 manage.py dbshell --settings=config.settings.tests

