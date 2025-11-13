from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from flask import render_template

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="111111",
    host="localhost",
    port="5432"
)


# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for daily playback
@app.route('/api/playbacks')
def get_playbacks():
    singer_name = request.args.get('singer_name', 'Singer A')
    cur = conn.cursor()

    # Fetch last 7 days for this singer
    cur.execute("""
                SELECT playback_date, playback_count
                FROM daily_playback
                WHERE singer_name = %s
                ORDER BY playback_date LIMIT 7
                """, (singer_name,))

    rows = cur.fetchall()
    cur.close()

    if not rows:
        return jsonify({"error": "Singer not found"}), 404

    # Transform into arrays for frontend
    playback_dates = [row[0].isoformat() for row in rows]
    playback_counts = [row[1] for row in rows]

    data = {
        "singer_name": singer_name,
        "playback_dates": playback_dates,
        "playback_counts": playback_counts
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
