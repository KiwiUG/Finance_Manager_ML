from flask import Flask, request, jsonify
import joblib

# Load model and vectorizer
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if not data or 'description' not in data:
        return jsonify({"error": "Missing 'description'"}), 400

    desc = data['description']
    vec = vectorizer.transform([desc])
    pred = model.predict(vec)[0]

    return jsonify({"description": desc, "predicted_category": pred})

if __name__ == "__main__":
    app.run(debug=True)
