#!/bin/bash

function install_python ()
{
	echo "Installing and configuring python..."
	sudo add-apt-repository -y ppa:deadsnakes/ppa
	sudo apt-get update
	sudo apt-get install -y python3.7 python3.7-dev python3-pip

	PIPENV_VERSION="2021.5.29" # Chosen arbitarily
	echo 'alias pipenv="python3.7 -m pipenv"' >> $BASH_ENV
	python3.7 -m pip install pipenv==$PIPENV_VERSION

	echo 'alias i="pipenv install"' >> $BASH_ENV
	echo 'alias a="pipenv run invoke"' >> $BASH_ENV
}


function install_other_tools ()
{
	echo "Installing other tools..."
	sudo apt-get -y install tree
}


function bootstrap () {
	install_python
	install_other_tools
}


bootstrap
