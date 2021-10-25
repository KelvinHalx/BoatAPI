# REST API With Flask & SQL Alchemy

> Products API using Python Flask, SQL Alchemy and Marshmallow

## Quick Start U

``` bash
# Create & Activate venv
$ python3 -m venv venv
$ . venv/bin/activate
```
## Install dependencies
```bash
$ pip3 install -r requirments.txt
```
## Create DB
```python
$ python3
>> from App import db
>> db.create_all()
>> exit()
```
## Run Server (http://localhst:5000)
```bash

python app.py
```

## Endpoints

* GET     /boat
* GET     /boat/:id
* POST    /boat
* PUT     /boat/:id
* DELETE  /boat/:id
