
tmpdirbuild := temporary_test
venv_dir := $(tmpdirbuild)/venv
activate := $(venv_dir)/bin/activate
package_name := psbody_meshlite

.DEFAULT_GOAL := all

$(tmpdirbuild):
	mkdir -p $(tmpdirbuild)

$(tmpdirbuild)/package_creation: $(tmpdirbuild)
	@echo "********" $(package_name) ": Building the virtualenv for installation"
	@virtualenv --system-site-packages $(venv_dir)
	@ . $(activate) && pip install --upgrade pip virtualenv setuptools wheel
	@ . $(activate) && pip install numpy scipy pyopengl pyzmq

	@echo "******** [" ${package_name} "] Creating the source distribution"
	@ . $(activate) && python setup.py sdist

	@echo "******** [" ${package_name} "] Creating the wheel distribution"
	@ . $(activate) && python setup.py --verbose bdist_wheel

	####### Cleaning some artifacts
	@rm -rf psbody_meshlite.egg-info
	####### Touching the result
	@touch $@

all: $(tmpdirbuild)/package_creation

install:
	@echo "********" $(package_name) ": installation"
	@echo "** installing " $(package_name) && cd dist && pip install --verbose --no-cache-dir *.whl ;

clean:
	@rm -rf $(tmpdirbuild)
	@find . -name "*.pyc" -delete
	@rm -rf build
	@rm -rf dist
	@rm -rf psbody_meshlite.egg-info
