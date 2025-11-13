from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

# Load CSV once at startup
df = pd.read_csv("daily_playback.csv", parse_dates=["playback_date"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/playbacks')
def get_playbacks():
    singer_name = request.args.get('singer_name', 'Singer A')
    df_filtered = df[df["singer_name"] == singer_name].sort_values("playback_date").head(7)

    if df_filtered.empty:
        return jsonify({"error": "Singer not found"}), 404

    return jsonify({
        "singer_name": singer_name,
        "playback_dates": df_filtered["playback_date"].dt.strftime("%Y-%m-%d").tolist(),
        "playback_counts": df_filtered["playback_count"].tolist()
    })

if __name__ == "__main__":
    app.run(debug=True)

