current_dir = $(shell pwd)

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

.PHONY: slides-html
slides-html: .venv
	source .venv/bin/activate; \
	jupyter-nbextension install rise --py --sys-prefix; \
	jupyter-nbextension enable rise --py --sys-prefix; \
	jupyter-nbconvert --to slides presentation.ipynb --reveal-prefix=file://$(current_dir)/.venv/share/jupyter/nbextensions/rise/reveal.js;
	open presentation.slides.html


.PHONY: slides
slides: .venv
	source .venv/bin/activate; \
	jupyter-nbextension install rise --py --sys-prefix; \
	jupyter-nbextension enable rise --py --sys-prefix; \
	jupyter-nbconvert --to slides presentation.ipynb --reveal-prefix=http://cdn.rawgit.com/hakimel/reveal.js/3.5.0/ --post serve


.PHONY: setup
setup: .venv
	source .venv/bin/activate; \
	rm -f db.sqlite3; \
	PYTYONPATH=.:$(PYTHONPATH) ./manage.py makemigrations --settings=app.settings app; \
	PYTYONPATH=.:$(PYTHONPATH) ./manage.py migrate --settings=app.settings