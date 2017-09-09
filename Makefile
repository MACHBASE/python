#******************************************************************************
# Copyright of this product 2013-2023,
# InfiniFlux Corporation(or Inc.) or its subsidiaries.
# All Rights reserved.
#******************************************************************************

# $Id:$


PYPATH=$(MACHBASE_HOME)/webadmin/flask/Python/bin/python

all: build

build: make_data_file

run : run_sample1 run_sample2 run_sample3

make_data_file:
	$(PYPATH) MakeData.py

run_sample1:
	$(PYPATH) Sample1Connect.py

run_sample2:
	$(PYPATH) Sample2Simple.py

run_sample3:
	$(PYPATH) Sample3Append.py

clean:
	rm -rf *.pyc data.txt



