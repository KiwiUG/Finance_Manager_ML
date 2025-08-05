# 💰 AI Personal Finance Assistant

An intelligent machine learning system that classifies your expenses, predicts spending behavior, and helps you understand your personal finances — all powered by ML, Flask, and Podman.

> 🧠 Learn end-to-end ML development with modern tools like Flask, TF-IDF, Logistic Regression, and Podman (Docker alternative).

---

## 🚀 Project Goals

This project is designed to help you **learn while building**. You'll master:

- ✅ Data preprocessing & feature engineering
- ✅ Machine Learning (text classification)
- ✅ Model evaluation & saving
- ✅ API development using Flask
- ✅ Containerization using Podman
- ✅ (Optional) Frontend with Streamlit or React

---

## 🧠 Features (Now & Planned)

### ✅ Phase 1 (Implemented)

- [x] Load and process transaction data
- [x] Extract date features (day, month, weekday)
- [x] Assign manual categories (Food, Transport, etc.)
- [x] Visualize spending by category (matplotlib)
- [x] Train an ML model using TF-IDF + Logistic Regression
- [x] Build a Flask API to serve the model
- [x] Test the prediction endpoint using `curl` or Postman

### 🔄 Phase 2 (Next)

- [ ] Containerize Flask app with Podman
- [ ] Add more features to the model (`amount`, `weekday`, etc.)
- [ ] Add interactive charts (Plotly / Streamlit)
- [ ] Build a basic UI (Streamlit or React)
- [ ] Add real-time speech or OCR input
- [ ] Deploy on Render, Railway, or VPS

---

## ⚙️ Getting Started

### 1. 📥 Clone the Repo

```bash
git clone https://github.com/your-username/ai-finance-assistant.git
cd ai-finance-assistant
```

2. 🐍 Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

🧪 Run the ML Pipeline

4. 📊 Preprocess the Data
```bash
python scripts/explore.py
```
5. 🤖 Train the ML Model
```bash
python scripts/train_model.py
```
This saves:

```
model/model.pkl

model/vectorizer.pkl
```

🌐 Run the Flask API

6. 🚀 Start the API Server
```bash
python app/main.py
```
7. 🔄 Test the Prediction API
```bash

curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"description": "Paid Uber"}'
```
✅ Output:

```json

{
  "description": "Paid Uber",
  "predicted_category": "Transport"
}
```

## 📦 Podman (Coming Next)
We'll containerize the entire Flask app and model using Podman:
- Write a Containerfile
- Build image with podman build
- Run containerized API using podman run
- Optional: podman-compose for multi-container apps (e.g., add DB)

## 🧑‍💻 Author
Utsav Gautam  
GitHub: @KiwiUG  
📍 Kathmandu, Nepal


