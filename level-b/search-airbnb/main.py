from web_scraping import WebScraping


local = input("Destination: ")
local = local.strip().replace(" ", "")
guests = int(input("Number of guests: "))
check_in = input("Check-in (YYYY-MM-DD): ")
checkout = input("Chekout (YYYY-MM-DD): ")

url = f"https://www.airbnb.com.br/s/{local}/homes?adults={guests}&checkin={check_in}&checkout={checkout}"

web_scraping = WebScraping(url)
all_room = web_scraping.pick_all_room()

print("\nThe best Airbnb options:")

for airbnb in all_room:
    print(f"\nLocal: {airbnb['Title']}")
    print(f"Description: {airbnb['Subtitle']}")
    # print(f"Assessment: {airbnb['Assessment']}")
    print(f"Price: {airbnb['Total Price']}")