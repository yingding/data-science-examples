# data-science-examples
this repository contains examples of ETL, ML pipeline, ML meta

## Run this project repo
You shall able to run this project repo using visio studio code:
1. Please following the following instruction to create a python virtual env
2. Select the python venv as python interpreter in visio studio code

## Python VENV

#### Create a VENV
```console
python3 -m venv /path/to/new/virtual/environment
```

#### Create a VENV by python version on MacOSX
```console
cd /usr/local/Cellar/python@3.8/3.8.13/bin
./python3.8 -m venv /path/to/new/virtual/environment
```



#### Activate a VENV in console
```console
source </path/to/new/virtual/environment>/bin/activate
```

#### Deactivate a VENV in console
```console
(/your/venv): deactivate
```

## Export and Import Libs
#### export libs from virtual env
```console
python3 -m pip install --upgrade pip
pip3 freeze > requirements.txt
```

#### import libs into the VENV
```console
pip3 install -r requirements.txt
``` 

## References
* find latest python package version on pypi.org: https://pypi.org/