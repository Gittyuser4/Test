from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database=os.environ.get("POSTGRES_DB"),
        user=os.environ.get("POSTGRES_USER"),
        password=os.environ.get("POSTGRES_PASSWORD"),
        port=5432
    )

@app.route("/")
def health():
    return jsonify({"status": "Backend is running"}), 200


@app.route("/db")
def db_check():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    cur.close()
    conn.close()
    return jsonify({"db": "connected"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

