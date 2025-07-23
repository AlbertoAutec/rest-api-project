from db import db  #qui importiamo il database dal file db.py

class StoreModel(db.Model):  #qui definiamo il modello per i negozi
    __tablename__ = 'stores'  #qui definiamo il nome della tabella nel database 

    id = db.Column(db.Integer, primary_key=True)  #qui definiamo il campo 'id' come chiave primaria
    name = db.Column(db.String(80), unique=True, nullable=False)  #qui definiamo il campo 'name' come stringa con una lunghezza massima di 80 caratteri e lo rendiamo obbligatorio  

    items = db.relationship('ItemModel', back_populates='store', lazy='dynamic', cascade='all, delete')  #qui definiamo una relazione tra il modello StoreModel e il modello ItemModel, permettendo di accedere agli articoli associati a un negozio
    #cosa fa lazy='dynamic'? Permette di caricare gli articoli in modo dinamico, cioè solo quando sono richiesti, migliorando le prestazioni in caso di grandi quantità di dati
    #inoltre lazy='dynamic' consente di utilizzare query per filtrare o ordinare gli articoli associati a un negozio senza caricarli tutti in memoria
    tags = db.relationship('TagModel', back_populates='store', lazy='dynamic', cascade='all, delete')  #qui definiamo una relazione tra il modello StoreModel e il modello TagModel, permettendo di accedere ai tag associati a un negozio
    #anche in questo caso, lazy='dynamic' consente di caricare i tag in modo dinamico, migliorando le prestazioni in caso di grandi quantità di dati
    