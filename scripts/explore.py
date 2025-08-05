import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/transactions.csv')

# Convert date and extract time features
df['date'] = pd.to_datetime(df['date'])
df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['weekday'] = df['date'].dt.day_name()

# Add category manually
def assign_category(desc):
    desc = desc.lower()
    if "starbucks" in desc:
        return "Food"
    elif "salary" in desc:
        return "Income"
    elif "uber" in desc:
        return "Transport"
    elif "grocery" in desc:
        return "Groceries"
    elif "bill" in desc:
        return "Utilities"
    else:
        return "Other"

df['category'] = df['description'].apply(assign_category)

# Optional: visualize
df[df['amount'] < 0].groupby('category')['amount'].sum().plot(kind='bar')
plt.title("Total Spending by Category")
plt.ylabel("Amount Spent")
plt.tight_layout()
plt.savefig("category_spending.png")

# Save processed CSV
df.to_csv("data/processed_transactions.csv", index=False)
