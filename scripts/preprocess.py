import os
import pandas as pd

RAW_DIR = "data/raw"
OUTPUT_PATH = "data/processed/processed_transactions.csv"

def preprocess():
    df_list = []
    for file in os.listdir(RAW_DIR):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(RAW_DIR, file))
            df_list.append(df)
    
    full_df = pd.concat(df_list, ignore_index=True)
    
    # 🔧 Add any cleaning logic here
    full_df.dropna(inplace=True)
    
    os.makedirs("data/processed", exist_ok=True)
    full_df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Processed {len(df_list)} files -> {OUTPUT_PATH}")

if __name__ == "__main__":
    preprocess()
