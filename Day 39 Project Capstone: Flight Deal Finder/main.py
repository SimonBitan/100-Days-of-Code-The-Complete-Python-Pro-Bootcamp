from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta
from monthdelta import monthdelta

# City to fly from. We'll use London for this example.
FLY_FROM = "LON"

# Constants for dates tomorrow and six months from tomorrow (our flight date range).
TOMORROW = str((datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"))
SIX_MONTHS = str((datetime.now() + timedelta(days=1) + monthdelta(6)).strftime("%d/%m/%Y"))

# Initiate DataManager class.
data_manager = DataManager()
sheet_data = data_manager["prices"]

# Initiate FlightSearch class.
flight_search = FlightSearch()

# Initiate FlightData class.
flight_data = FlightData()

# Initiate NotificationManager.
notification_manager = NotificationManager()

city_list = flight_search.get_iata_code()

################## Uncomment the code block below to update the IATA codes on the sheet. ############################
# city_count = 0
# for city in sheet_data:
#     city["iataCode"] = city_list[city_count]
#     parameters = {
#         "price": {
#             "iataCode": city_list[city_count]
#         }
#     }
#     row_id = city["id"]
#     data_manager.update_iata_codes(iata_code=parameters, row_id=row_id)
#     city_count += 1

# Get cheapest flights.
row = 0
for code in city_list:
    request_params = {
        "fly_to": code,
        "fly_from": FLY_FROM,
        "date_from": TOMORROW,
        "date_to": SIX_MONTHS,
        "adults": 1,
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "curr": "GBP"
    }

    # Find the cheapest price and it's location in the response ("flight_number").
    get_flight_price = flight_data.get_flight_price(request_params)
    price = get_flight_price[0]
    flight_number = get_flight_price[1]

    if price < sheet_data[row]["lowestPrice"]:
        sheet_data[row]["lowestPrice"] = price
        parameters = {
                    "price": {
                        "lowestPrice": price
                    }
                }
        row_id = sheet_data[row]["id"]
        data_manager.update_lowest_price(parameters, row_id)

        # Get the flight data and send it via SMS.
        data = flight_data.get_flight_data(request_params, flight_number)
        origin_city = data[0]
        origin_airport = data[1]
        dest_city = data[2]
        dest_airport = data[3]
        arrival_date = data[4]
        return_date = data[5]
        notification_manager.send_text(price=price,
                                       origin_city=origin_city,
                                       origin_airport=origin_airport,
                                       dest_city=dest_city,
                                       dest_airport=dest_airport,
                                       arrival_date=arrival_date,
                                       return_date=return_date)
    row += 1


print("Sheet updated with lowest prices found. Text sent with more info.")
