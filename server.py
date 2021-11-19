from datetime import datetime
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import backref


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    farm = db.relationship("Farm", backref='user')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    location = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    chicken_data = db.relationship("ChickenData", backref='farm')
    death_report = db.relationship("DeathReports", backref='farm')
    chicken_sales = db.relationship("ChickenSales", backref='farm')
    egg_sales = db.relationship("EggSales", backref='farm') 
    egg_data = db.relationship("EggData", backref='farm')
    feeds = db.relationship("Feeds", backref='farm')
    vaccines = db.relationship("Vaccines", backref='farm')
    additional_expenses = db.relationship("AdditionalExpenses", backref='farm')

class ChickenData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    price = db.Column(db.Integer)
    chicken_type = db.Column(db.String)
    date_purchased = db.Column(db.DateTime, default=datetime.utcnow)
    no_of_chicken_purchased = db.Column(db.Integer)

class DeathReports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    broilers = db.Column(db.Integer, default=0)
    layers=db.Column(db.Integer, default=0)
    date_of_death = db.Column(db.DateTime, default=datetime.utcnow)

class ChickenSales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    chicken_type = db.Column(db.String)
    sales_to = db.Column(db.String)
    chicken_sold = db.Column(db.Integer)
    price_per_chicken = db.Column(db.Integer)
    medium_of_sale = db.Column(db.String)
    date_of_sale = db.Column(db.DateTime, default=datetime.utcnow)

class EggSales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    eggs_sold = db.Column(db.Integer)
    sales_to = db.Column(db.String)
    date_of_sale = db.Column(db.DateTime, default=datetime.utcnow)

class EggData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    egg_type = db.Column(db.String)
    no_of_eggs_laid = db.Column(db.Integer)
    date_laid = db.Column(db.DateTime, default=datetime.utcnow)

class Feeds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    feed_type = db.Column(db.String)
    no_of_bags_purchased = db.Column(db.Numeric(10,2))
    price_per_bag = db.Column(db.Integer)
    medium_of_sale = db.Column(db.String)
    date_purchased = db.Column(db.DateTime, default=datetime.utcnow)

class Vaccines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    vaccine_name = db.Column(db.String)
    no_of_vaccines = db.Column(db.Numeric(10,2))
    price_per_unit = db.Column(db.Integer)
    medium_of_sale = db.Column(db.String)
    date_purchased = db.Column(db.DateTime, default=datetime.utcnow)

class AdditionalExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey("farm.id"))
    name_of_expense = db.Column(db.String)
    brief_description = db.Column(db.String)
    cost = db.Column(db.Integer)
    medium_of_sale = db.Column(db.String)
    
    
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class FarmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Farm

class ChickenDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ChickenData

class ChickenSalesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ChickenSales

class DeathReportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DeathReports

class EggSaleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EggSales

class EggDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EggData

class FeedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feeds

class VaccineSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vaccines

class AdditionalExpensesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdditionalExpenses




@app.route("/")
def index():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(users)
    return {'user': output}


@app.route('/users/signup', methods=['POST'])
def postUsers():
    user = User(email=request.json['email'], username=request.json['username'],password=request.json['password'])
    db.session.add(user)
    db.session.commit()
    logged_user = User.query.filter_by(email=request.json['email'], username=request.json['username'])
    user_schema = UserSchema(many=True)
    output = user_schema.dump(logged_user)
    return {'user': output}

@app.route("/users/login", methods=['POST'])
def login():
    exists = db.session.query(db.exists().where(User.username == request.json['username'])).scalar()
    if exists == True:
        logged_user = User.query.filter_by(email=request.json['email'])
        user_schema = UserSchema(many=True)
        output = user_schema.dump(logged_user)
        return {'user': output}

    else:
        return "Email or password is wrong"

@app.route('/dashboard/farms/<userid>', methods=['GET'])
def getFarms(userid):
    farms = Farm.query.filter_by(user_id=userid).all()
    farm_schema = FarmSchema(many=True)
    output = farm_schema.dump(farms)
    return {'farms': output}

@app.route('/dashboard/farm/chickendata/<farmid>', methods=['GET', 'POST'])
def chickenData(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.chicken_data.append(ChickenData(chicken_type=request.json['chicken_type'], 
        no_of_chicken_purchased=request.json['number'], price=request.json['price']))
        db.session.commit()
        inputdata = ChickenData.query.filter_by(farm_id=farmid).all()
        data_schema = ChickenDataSchema(many=True)
        output = data_schema.dump(inputdata)
        return {'chickendata' : output}
    else:
        data = ChickenData.query.filter_by(farm_id=farmid).all()
        data_schema = ChickenDataSchema(many=True)
        output = data_schema.dump(data)
        return {'chickendata' : output}


@app.route('/dashboard/farm/chickensales/<farmid>', methods=['GET', 'POST'])
def chickenSales(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.chicken_sales.append(ChickenSales(chicken_type=request.json['chicken_type'], 
        sales_to=request.json['sales_to'], chicken_sold=request.json['chicken_sold'],
        price_per_chicken=request.json['price_per_chicken'], medium_of_sale=request.json['medium_of_sale']
        ))
        db.session.commit()
        data = ChickenSales.query.filter_by(farm_id=farmid).all()
        data_schema = ChickenSalesSchema(many=True)
        output = data_schema.dump(data)
        return {'chickensales' : output}
    else:
        data = ChickenSales.query.filter_by(farm_id=farmid).all()
        data_schema = ChickenSalesSchema(many=True)
        output = data_schema.dump(data)
        return {'chickensales' : output}

@app.route('/dashboard/farm/deathreports/<farmid>', methods=['GET', 'POST'])
def deathReports(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.death_report.append(DeathReports(broilers=request.json['broilers'], 
        layers=request.json['layers']))
        db.session.commit()
        data = DeathReports.query.filter_by(farm_id=farmid).all()
        data_schema = DeathReportSchema(many=True)
        output = data_schema.dump(data)
        return {'deathreports' : output}
    else:
        data = DeathReports.query.filter_by(farm_id=farmid).all()
        data_schema = DeathReportSchema(many=True)
        output = data_schema.dump(data)
        return {'deathreports' : output}


@app.route('/dashboard/farm/eggdata/<farmid>', methods=['GET', 'POST'])
def eggData(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.egg_data.append(EggData(egg_type=request.json['egg_type'], 
        no_of_eggs_laid=request.json['no_of_eggs_laid']
        ))
        db.session.commit()
        data = EggData.query.filter_by(farm_id=farmid).all()
        data_schema = EggDataSchema(many=True)
        output = data_schema.dump(data)
        return {'eggdata' : output}
    
    else:
        data = EggData.query.filter_by(farm_id=farmid).all()
        data_schema = EggDataSchema(many=True)
        output = data_schema.dump(data)
        return {'eggdata' : output}

@app.route('/dashboard/farm/eggsales/<farmid>', methods=['GET', 'POST'])
def eggSales(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.egg_sales.append(EggSales(eggs_sold=request.json['eggs_sold'],
        sales_to=request.json['sales_to']
        ))
        db.session.commit()
        data = EggSales.query.filter_by(farm_id=farmid).all()
        data_schema = EggSaleSchema(many=True)
        output = data_schema.dump(data)
        return {'eggsales' : output}
    else:
        data = EggSales.query.filter_by(farm_id=farmid).all()
        data_schema = EggSaleSchema(many=True)
        output = data_schema.dump(data)
        return {'eggsales' : output}

@app.route('/dashboard/farm/feeds/<farmid>', methods=['GET', 'POST'])
def feedData(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.feeds.append(Feeds(feed_type=request.json['feed_type'], 
        no_of_bags_purchased=request.json['bags_purchased'], 
        price_per_bag=request.json['price_per_bag'],
        medium_of_sale=request.json['medium_of_sale']
        ))
        db.session.commit()
        data = Feeds.query.filter_by(farm_id=farmid).all()
        data_schema = FeedSchema(many=True)
        output = data_schema.dump(data)
        return {'feeds' : output}
    else:
        data = Feeds.query.filter_by(farm_id=farmid).all()
        data_schema = FeedSchema(many=True)
        output = data_schema.dump(data)
        return {'feeds' : output}

@app.route('/dashboard/farm/vaccines/<farmid>', methods=['GET', 'POST'])
def vaccineData(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.vaccines.append(Vaccines(vaccine_name=request.json['name'],
        no_of_vaccines=request.json['units'],
        price_per_unit=request.json['price_per_unit'],
        medium_of_sale=request.json['medium_of_sale']
        ))
        db.session.commit()
        data = Vaccines.query.filter_by(farm_id=farmid).all()
        data_schema = VaccineSchema(many=True)
        output = data_schema.dump(data)
        return {'vaccinedata' : output}
    else:
        data = Vaccines.query.filter_by(farm_id=farmid).all()
        data_schema = VaccineSchema(many=True)
        output = data_schema.dump(data)
        return {'vaccinedata' : output}

@app.route('/dashboard/farm/additionalexpenses/<farmid>', methods=['GET', 'POST'])
def additionalexpensesData(farmid):
    if request.method == 'POST':
        farm = Farm.query.get(farmid)
        farm.additional_expenses.append(AdditionalExpenses(name_of_expense=request.json['name'],
        brief_description=request.json['description'],
        cost=request.json['cost'],
        medium_of_sale=request.json['medium_of_sale']
        ))
        db.session.commit()
        data = AdditionalExpenses.query.filter_by(farm_id=farmid).all()
        data_schema = AdditionalExpensesSchema(many=True)
        output = data_schema.dump(data)
        return {'additionalexpenses' : output}
    else:
        data = AdditionalExpenses.query.filter_by(farm_id=farmid).all()
        data_schema = AdditionalExpensesSchema(many=True)
        output = data_schema.dump(data)
        return {'additionalexpenses' : output}
if __name__ == "__main__":
    app.run(debug=True)