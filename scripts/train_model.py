import json
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import os

# Load config
with open("config/config.json") as f:
    config = json.load(f)

# Load data
df = pd.read_csv("data/processed/processed_transactions.csv")
label_col = config["label_column"]
X = df.drop(label_col, axis=1)
y = df[label_col]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=config["test_size"], random_state=config["random_state"]
)

# GridSearch
params = config["hyperparams"]
grid = GridSearchCV(RandomForestClassifier(), params, cv=5, n_jobs=-1, verbose=1)
grid.fit(X_train, y_train)

# Evaluate
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)

print("✅ Best Params:", grid.best_params_)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("✅ Report:\n", classification_report(y_test, y_pred))

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(best_model, "model/model.pkl")
print("✅ Model saved to model/model.pkl")
