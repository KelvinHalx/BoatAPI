# REST API With Flask & SQL Alchemy

> Products API using Python Flask, SQL Alchemy and Marshmallow

## Quick Start U

``` bash
# Create & Activate venv
$ python3 -m venv venv
$ . venv/bin/activate
```
```bash
# Install dependencies
$ pip3 install -r requirments.txt
```
```python
# Create DB
$ python3
>> from App import db
>> db.create_all()
>> exit()
```
```bash
# Run Server (http://localhst:5000)
python app.py
```

## Endpoints

* GET     /product
* GET     /product/:id
* POST    /product
* PUT     /product/:id
* DELETE  /product/:id
