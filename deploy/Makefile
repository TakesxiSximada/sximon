# -*- coding: utf-8 -*-
# Need virtualenv
.PHONY: all clean build rebuild

all: env bin/buildout build
	echo "buildout finished..."

clean:
	rm -rf bin parts eggs develop-eggs .installed env

build: bin/buildout

	bin/buildout -c buildout.cfg

rebuild: clean build
	echo

bin/buildout: env
	touch buildout.cfg
	curl https://raw.githubusercontent.com/buildout/buildout/master/bootstrap/bootstrap.py | env/bin/python

env: env/bin/python
	virtualenv env
	env/bin/pip install -U setuptools
