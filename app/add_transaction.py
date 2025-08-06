import re
from datetime import datetime, timedelta

def parse_natural_input(msg):
    msg = msg.lower()

    # Basic rules
    amount = None
    txn_type = "expense"
    category = "other"
    date = datetime.today().strftime("%Y-%m-%d")

    # 🔍 Extract amount
    amt_match = re.search(r"(\d+(\.\d+)?)", msg)
    if amt_match:
        amount = float(amt_match.group(1))

    # 🔍 Determine type (income or expense)
    if any(word in msg for word in ["got", "earned", "received", "salary", "income"]):
        txn_type = "income"

    # 🔍 Guess category
    categories = ["food", "groceries", "rent", "electricity", "salary", "travel", "shopping", "entertainment"]
    for cat in categories:
        if cat in msg:
            category = cat
            break

    # 🔍 Parse date keywords
    if "yesterday" in msg:
        date = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    elif "today" in msg:
        date = datetime.today().strftime("%Y-%m-%d")

    return {
        "type": txn_type,
        "amount": amount,
        "category": category,
        "date": date,
        "note": msg  # store full message as note
    }
