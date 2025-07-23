# Stores REST API

Questa è una REST API sviluppata con Flask per la gestione di negozi, articoli, tag e utenti, con autenticazione JWT, validazione Marshmallow, persistenza su SQLite tramite SQLAlchemy e gestione delle migrazioni con Flask-Migrate/Alembic.

## Funzionalità principali
- CRUD per stores, items, tags, users
- Relazioni molti-a-molti tra items e tags
- Autenticazione JWT (login, logout, refresh, blocklist, ruoli)
- Validazione input con Marshmallow
- Migrazioni database con Flask-Migrate/Alembic
- Gestione ambiente virtuale (venv/.venv)
- Controllo versione con Git

## Avvio rapido
1. Crea e attiva la virtualenv:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Installa le dipendenze:
   ```sh
   pip install -r requirements.txt
   ```
3. Avvia l'app Flask:
   ```sh
   flask run
   ```

## Migrazioni database
- Inizializza le migrazioni:
  ```sh
  flask db init
  ```
- Genera una migration:
  ```sh
  flask db migrate -m "Messaggio"
  ```
- Applica la migration:
  ```sh
  flask db upgrade
  ```

## Test API
Puoi testare gli endpoint con strumenti come Insomnia o Postman.

## Note
- I file temporanei, database e virtualenv sono esclusi dal versionamento tramite `.gitignore`.
- Per il push su GitHub usa un Personal Access Token come password.

## Autore
Alberto Mingardi
