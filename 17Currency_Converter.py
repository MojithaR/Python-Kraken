# Currency_Converter.py

import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = "your_api_key_here"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if data["result"] == "success":
        rate = data["conversion_rates"][to_currency]
        converted_amount = amount * rate
        return f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}"
    else:
        return "Error fetching exchange rate"

if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ")
    to_currency = input("To currency (e.g., EUR): ")
    print(convert_currency(amount, from_currency, to_currency))
