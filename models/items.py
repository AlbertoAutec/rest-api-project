from sqlalchemy import ForeignKey  #qui importiamo ForeignKey per definire chiavi esterne
from db import db  #qui importiamo il database per gestire le operazioni sugli articoli

class ItemModel(db.Model):  #qui definiamo il modello per gli articoli
    __tablename__ = 'items'  #qui definiamo il nome della tabella nel database

    id = db.Column(db.Integer, primary_key=True)  #qui definiamo il campo 'id' come chiave primaria
    name = db.Column(db.String(80), unique=True, nullable=False)  #qui definiamo il campo 'name' come stringa con una lunghezza massima di 80 caratteri e lo rendiamo obbligatorio
    description = db.Column(db.String) #qui definiamo il campo 'description' come stringa con una lunghezza massima di 200 caratteri e lo rendiamo facoltativo
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)  #qui definiamo il campo 'price' come float e lo rendiamo obbligatorio
    store_id = db.Column(
        db.Integer, db.ForeignKey('stores.id'), unique=False, nullable=False
    )  #qui definiamo il campo 'store_id' come chiave esterna che fa riferimento alla tabella 'stores'
    store = db.relationship('StoreModel', back_populates='items')  #qui definiamo una relazione tra gli articoli e i negozi
#in questo modo, possiamo accedere agli articoli di un negozio tramite la relazione 'items' nel modello StoreModel
    tags = db.relationship(
        'TagModel',
        secondary='items_tags',
        back_populates='items'
    )  #qui definiamo una relazione molti-a-molti tra gli articoli e i tag
#in questo modo, possiamo accedere ai tag di un articolo tramite la relazione 'tags'
