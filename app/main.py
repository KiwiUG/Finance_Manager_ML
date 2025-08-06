import os
import pandas as pd
from datetime import datetime
from scripts.personal_train import train_personal_model
from scripts.preprocess import preprocess_user_data
from app.add_transaction import parse_natural_input

USER_ID = "user1"
USER_DATA_PATH = f"data/users/{USER_ID}.csv"
THRESHOLD_TO_TRAIN = 5

def load_user_data():
    if os.path.exists(USER_DATA_PATH):
        return pd.read_csv(USER_DATA_PATH)
    else:
        return pd.DataFrame(columns=["date", "type", "amount", "category", "note"])

def save_user_data(df):
    df.to_csv(USER_DATA_PATH, index=False)

def show_model_accuracy():
    acc_path = f"model/users/{USER_ID}_accuracy.txt"
    if os.path.exists(acc_path):
        with open(acc_path, "r") as f:
            print("📊 Your model accuracy:", f.read())
    else:
        print("ℹ️ Model has not been trained yet.")

def main():
    print("\n💰 Welcome to AI Finance Assistant")
    show_model_accuracy()

    df = load_user_data()

    while True:
        add_more = input("\nDo you want to add a new transaction? (y/n): ").lower()
        if add_more != 'y':
            break

        msg = input("💬 Say your transaction: ")
        new_txn = parse_natural_input(msg)

        print("🔍 Parsed transaction:")
        for k, v in new_txn.items():
            print(f"  {k}: {v}")

        confirm = input("✅ Save this transaction? (y/n): ").lower()
        if confirm != 'y':
            print("❌ Skipped.")
            continue

        df = pd.concat([df, pd.DataFrame([new_txn])], ignore_index=True)
        save_user_data(df)
        print("✅ Saved!")

        if len(df) >= THRESHOLD_TO_TRAIN:
            print("📈 Enough data! Training your personal model...")
            preprocess_user_data(USER_ID)
            train_personal_model(USER_ID)
            show_model_accuracy()

    print("\n👋 Exiting app. Have a great day!")

if __name__ == "__main__":
    main()
