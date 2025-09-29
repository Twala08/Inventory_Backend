from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=True)  
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),  
            "name": self.name,
            "category": self.category,
            "price": self.price
        }
