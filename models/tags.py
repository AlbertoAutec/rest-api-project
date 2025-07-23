from db import db  # Import the database instance from db.py

class TagModel(db.Model):  # Define the model for tags
    __tablename__ = 'tags'  # Define the name of the table in the database  

    id = db.Column(db.Integer, primary_key=True)  # Define the 'id' field as the primary key
    name = db.Column(db.String(80), unique=False, nullable=False)  # Define the 'name' field as a string with a maximum length of 80 characters and make it requiredù
    store_id = db.Column(
        db.Integer, db.ForeignKey('stores.id'), nullable=False
    )  # Define the 'store_id' field as a foreign key that references the 'stores' table
    store = db.relationship('StoreModel', back_populates='tags')  # Define a relationship between tags and stores
# This allows us to access the tags of a store through the 'tags' relationship in the StoreModel
    items = db.relationship(
        'ItemModel',
        secondary='items_tags',
        back_populates='tags'
    )  # Define a many-to-many relationship between tags and items
    