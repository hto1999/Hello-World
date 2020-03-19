build:  clean
	python3 setup.py sdist bdist_wheel

clean:
	rm -f -r dist build *.egg-info