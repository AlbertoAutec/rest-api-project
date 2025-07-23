from db import db  #qui importiamo il database dal file db.py

class UserModel(db.Model):  #qui definiamo il modello UserModel che rappresenta gli utenti nel database
    __tablename__ = "users"  #qui definiamo il nome della tabella nel database

    id = db.Column(db.Integer, primary_key=True)  #qui definiamo la colonna id come chiave primaria
    username = db.Column(db.String(80), unique=True, nullable=False)  #qui definiamo la colonna username come stringa unica e non nulla
    password = db.Column(db.String(200), nullable=False)  #qui definiamo la colonna password come stringa non nulla

    def __repr__(self):  #qui definiamo il metodo di rappresentazione dell'oggetto UserModel
        return f"<User {self.username}>"  #restituiamo una stringa che rappresenta l'utente
