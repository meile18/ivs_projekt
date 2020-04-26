# Makefile for Calculator project

PYTHON=python3
SRC=standard_deviation.py
DATA_INPUT=data.txt
TESTS=tests.py
MATLIB=matlib.py
CALCULATOR=calculator.py
PROFILER=cProfile
PROFILER_OUTPUT=profile.txt

ARCHIVE=../../xmacha72_xpodha01_xkisst00
DOC=$(ARCHIVE)/doc
INSTALL=$(ARCHIVE)/install
REPO=$(ARCHIVE)/repo

.PHONY: doc clean test run profile

# project "compilation"
all:
	@echo "Python files don't need to be compiled."

# create .zip file
pack: doc
	mkdir $(ARCHIVE)
	mkdir $(DOC)
	mkdir $(INSTALL) 
	mkdir $(REPO)
	cp -r doc/html $(DOC)
	cp calculator_1.0_amd64.deb $(INSTALL)
	cp -r ../../ivs_projekt/. $(REPO)
	cd $(ARCHIVE) && cd .. && zip -r  xmacha72_xpodha01_xkisst00.zip ./xmacha72_xpodha01_xkisst00

# delete all temp files
clean:
	rm -r doc
	rm -rf ../../xmacha72_xpodha01_xkisst00

# run tests
test:
	$(PYTHON) $(TESTS)

# generate Doxygen documentation
doc:
	doxygen

# run the calculator
run:
	$(PYTHON) $(CALCULATOR)

# compute the standard deviation and profile the program
profile:
	$(PYTHON) -m $(PROFILER) -o $(PROFILER_OUTPUT) $(SRC) <$(DATA_INPUT)
