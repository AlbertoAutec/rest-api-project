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

## 📌 Cosa devi fare ogni volta che lavori

Ecco lo schema universitario/didattico con i comandi essenziali e il flusso tipico:

### ✨ Fase 1 – Aggiorna il tuo locale con eventuali modifiche fatte online
Se hai modificato file direttamente su GitHub (web o altro computer), prima di lavorare localmente scarica gli aggiornamenti:

```sh
cd ~/Desktop/rest-Api-project
# Aggiorna dal remote Mingardi
git pull mingardi master
# (Opzionale) Aggiorna da altro remote
# git pull autec master
```

### ✨ Fase 2 – Lavora localmente
Modifica i file, aggiungi/rimuovi/sposta contenuti. Quando hai finito:

```sh
git add .
git commit -m "Descrizione chiara delle modifiche"
```

### ✨ Fase 3 – Aggiorna entrambe le repo online
Fai push su entrambi i remoti:

```sh
# Push su Mingardi
git push mingardi master
# Push su Autec
git push origin master
```

---

## ✅ Riepilogo comandi tipici

| Azione                      | Comando                        |
|-----------------------------|--------------------------------|
| Vai nella cartella locale   | cd ~/Desktop/rest-Api-project  |
| Aggiorna locale da Mingardi | git pull mingardi master       |
| Stagia modifiche            | git add .                      |
| Fai commit                  | git commit -m "Messaggio commit" |
| Aggiorna repo Mingardi      | git push mingardi master       |
| Aggiorna repo Autec         | git push autec master          |
