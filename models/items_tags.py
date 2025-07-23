from db import db  # Import the database instance from db.py

class ItemTagModel(db.Model):  # Define the model for item tags
    __tablename__ = 'items_tags'  # Define the name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Define the 'id' field as the primary key
    item_id = db.Column(
        db.Integer, db.ForeignKey('items.id'))  # Define the 'item_id' field as a foreign key that references the 'items' table
    tag_id = db.Column(
        db.Integer, db.ForeignKey('tags.id'))  # Define the 'tag_id' field as a foreign key that references the 'tags' table
    
