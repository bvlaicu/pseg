.PHONY: docs release clean build

clean:
	rm -rf pseg_env

build:
	virtualenv -p /usr/local/bin/python3 pseg_env && source pseg_env/bin/activate && \
		pip install -r requirements.txt

test: clean build
		source pseg_env/bin/activate && \
		coverage run --source=pseg setup.py test && \
		coverage html && \
		coverage report

release: test
	vim pseg/__init__.py
