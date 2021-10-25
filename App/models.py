from App import db, app


class Boat(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False,unique=False)
    boat_type = db.Column(db.String(40),nullable=False)
    length = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Boats(name = {name}, boat_type = {boat_type}, length = {lenght})"

# Boat Schema
class BoatSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'boat_type', 'length')

#Init Schema
boat_schema = BoatSchema()
boats_schema = BoatSchema(many=True)
