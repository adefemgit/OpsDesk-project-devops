import os

import psycopg
from flask import Flask

app = Flask(__name__)


@app.get("/health/live")
def health_live():
    return {"status": "ok"}, 200


@app.get("/health/ready")
def health_ready():
    try:
        with psycopg.connect(
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            connect_timeout=3,
            options="-c statement_timeout=3000",
        ) as connection:
            connection.execute("SELECT 1").fetchone()
    except (psycopg.Error, KeyError):
        return {"status": "not ready"}, 503

    return {"status": "ready"}, 200