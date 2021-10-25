import os
from flask import render_template, url_for, flash, redirect, request, abort
from App import app, db

# Create a Boat
@app.route("/boat",methods=['POST'])
def add_boat():
  name = request.json['name']
  boattype = request.json['boattype']
  length = request.json['length']

  new_boat = Boat(name,boattype,length)

  db.session.add(boat)
  db.session.commit()

  return boat_schema.jsonify(new_boat)

# Get All Boats
@app.route('/boat', methods=['GET'])
def get_boats():
  all_boats = Boat.query.all()
  result = boats_schema.dump(all_boats)
  return jsonify(result.data)

# Get Single Boat
@app.route('/boat/<id>', methods=['GET'])
def get_boatt(id):
  boat = Boat.query.get(id)
  return boat_schema.jsonify(boat)

# Update a Boat
@app.route("/boat/<id>",methods=['PUT'])
def update_boat():
  boat = Boat.query.get(id)

  name = request.json['name']
  boattype = request.json['boat_type']
  length = request.json['length']

  new_boat = Boat(name,boat_type,length)

  db.session.commit()

  return boat_schema.jsonify(boat)

# Delete a Boat
@app.route('/boat/<id>', methods=['DELETE'])
def delete_boat(id):
  boat = Boat.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(boat)
