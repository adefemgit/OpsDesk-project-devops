from flask import Flask

app = Flask(__name__)


@app.get("/health/live")
def health_live():
    return {"status": "ok"}, 200
