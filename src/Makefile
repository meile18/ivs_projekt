# Součástí bude Makefile pro kompilaci projektu, který bude obsahovat alespoň tyto cíle:

#     all (přeloží projekt - včetně programu pro profiling)
#     pack (zabalí projekt tak, aby mohl být odevzdán)
#     clean (smaže všechny soubory, co nemají být odevzdány)
#     test (spustí testy matematické knihovny)
#     doc (spustí generování dokumentace)
#     run (spustí program)
#     profile (spustí překlad programu pro výpočet směrodatné odchylky na profiling)
#     Při spuštění make bez uvedení cíle se provede make all.

# Je-li projekt vytvořený v MS Visual Studio ve Windows a využití Make pro překlad a/nebo generování dokumentace je problematické, dané cíle nemusí být vytvořeny - v takovém případě Makefile bude mít min. následující cíle:

#     all (spustí progam)
#     pack (zabalí projekt tak, aby mohl být odevzdán)
#     clean (smaže všechny soubory, co nemají být odevzdány)
#     run (spustí program)
#     profile (spustí program pro výpočet směrodatné odchylky s ukázkovým testovacím vstupem)
#     help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)
#     Při spuštění make bez uvedení cíle se provede make all.

# Makefile bude v obou výše uvedených případech určen pro GNU Make (pro Windows např. zde). Makefile pro Windows tedy musí využívat GNU make, ale příkazovou řádku Windows (tedy např. del místo rm). Výjimky mohou v dobře odůvodněných případech předem povolit cvičící, ale neměl by k nim být důvod (z Makefile lze spouštět Maven i jiné nástroje).
# Pokud to není nezbytně nutné (např. instalační cesty jako je /usr/bin), Makefile nebude obsahovat absolutní cesty.
# Bude-li to možné, Makefile nebude obsahovat jméno ani jednoho ze zdrojových souborů.
# Na kalkulačce si povinně vyzkoušíte debugging - odevzdáte snímek obrazovky debuggeru v matematické knihovně.
# K programu bude vytvořen mockup uživatelského rozhraní další verze kalkulačky (plánované do budoucna), která bude podporovat vědecký mód, vykreslování grafů a nějakou další potenciálně užitečnou funkci (výpočet BMI, stopky, statistické funkce, …). Musí být jasné, jak bude nová verze vypadat a fungovat, v případě potřeby vytvořte mockupů více

PYTHON=python3
SRC=standard_deviation.py
DATA_INPUT=data.txt
TESTS=tests.py
MATLIB=matlib.py
CALCULATOR=calculator.py
PROFILER=cProfile
PROFILER_OUTPUT=profile.txt

ARCHIVE=../../xmacha72
DOC=$(ARCHIVE)/doc
INSTALL=$(ARCHIVE)/install
REPO=$(ARCHIVE)/repo

all: ## project "compilation"
	$(PYTHON) $(SRC) <$(DATA_INPUT)

pack: doc ## create .zip file
	mkdir $(ARCHIVE)
	mkdir $(DOC)
	mkdir $(INSTALL) 
	mkdir $(REPO)
	cp -r doc/html $(DOC)
	cp calculator_1.0_amd64.deb $(INSTALL)
	cp -r ../../ivs_projekt/. $(REPO)
	cd $(ARCHIVE) && zip -r xmacha72.zip . && mv xmacha72.zip ..

clean: ## delete all temp files
	rm -r doc
	rm -rf ../../xmacha72

test: ## run tests
	$(PYTHON) $(TESTS)

doc: ## generate Doxygen documentation
	doxygen

run: ## run the calculator
	$(PYTHON) $(CALCULATOR)

profile: ## compute the standard deviation and profile the program
	$(PYTHON) -m $(PROFILER) -o $(PROFILER_OUTPUT) $(SRC) <$(DATA_INPUT)
