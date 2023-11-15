from currency import ConvertCurrency


api_key = "04c9f1029014eafd3814"  # Free API
conv_curr = ConvertCurrency(api_key)
conv_curr.show_currencies()
print("\n")

initial = input("Currency: ").upper()
amount = input("Amount: ")
end = input("Convert to: ").upper()

print(conv_curr.transform_currency(initial, amount, end))
