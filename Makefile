.venv: requirements.txt
	virtualenv -p python3.6 .venv
	source .venv/bin/activate; pip install -r requirements.txt; \
	jupyter-nbextension install rise --py --sys-prefix; \
	jupyter-nbextension enable rise --py --sys-prefix
	touch .venv

.PHONY: notebook
notebook: .venv
	source .venv/bin/activate; \
	jupyter-nbextension install rise --py --sys-prefix; \
	jupyter-nbextension enable rise --py --sys-prefix; \
	PYTYONPATH=.:$(PYTHONPATH) DJANGO_SETTINGS_MODULE=app.settings ./manage.py shell_plus --notebook

.PHONY: slides
slides: .venv
	source .venv/bin/activate; \
	jupyter-nbextension install rise --py --sys-prefix; \
	jupyter-nbextension enable rise --py --sys-prefix; \
	jupyter nbconvert ./presentation.ipynb --to slides --post serve


.PHONY: setup
setup: .venv
	source .venv/bin/activate; \
	rm -f db.sqlite3; \
	PYTYONPATH=.:$(PYTHONPATH) ./manage.py makemigrations --settings=app.settings app; \
	PYTYONPATH=.:$(PYTHONPATH) ./manage.py migrate --settings=app.settings