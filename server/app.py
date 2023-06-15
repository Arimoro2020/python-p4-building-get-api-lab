#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()
    all = []
    for bakery in bakeries:
        all_dict = {
        "name": bakery.name,
        "id": bakery.id,
        "created_at":bakery.created_at
        }
        all.append(all_dict)

    res = make_response(all, 200, {'Content-Type': "application/json"})
    
    return res

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery_id = Bakery.query.filter(Bakery.id==id).first()
  
    all_dict = {
    "name": bakery_id.name,
    "id": bakery_id.id,
    "created_at":bakery_id.created_at
    }
       
    response = make_response(all_dict, 200)
    response.headers['Content-Type'] = "application/json"
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    by_price =BakedGood.query.order_by(BakedGood.price.desc()).all()
    all = []
    for good in by_price:
        all_dict = {
        "name":good.name,
        "price":good.price,
        "id":good.id,
        "bakery_id":good.bakery_id,
        "created_at":good.created_at
        }
        all.append(all_dict)

    response = make_response(all, 200, {'Content-Type': "application/json"})
    return response


@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    good =BakedGood.query.order_by(BakedGood.price.desc()).first()
  
    most_price_dict = {
    "name": good.name,
    "price": good.price,
    "id":good.id,
    "bakery_id":good.bakery_id,
    "created_at":good.created_at
    }
    

    response = make_response(most_price_dict, 200, {'Content-Type': "application/json"})

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
