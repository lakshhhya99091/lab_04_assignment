class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

flights = [
    Flight("AI161E90", "BLR", "BOM", 5600),
    Flight("BR161F91", "BOM", "BBI", 6750),
    Flight("AI161F99", "BBI", "BLR", 8210),
    Flight("VS171E20", "JLR", "BBI", 5500),
    Flight("AS171G30", "HYD", "JLR", 4400),
    Flight("AI131F49", "HYD", "BOM", 3499)
]

def search_flights_by_city(city):
    result = [flight for flight in flights if flight.destination == city]
    return result

def search_flights_from_city(source):
    result = [flight for flight in flights if flight.source == source]
    return result

def search_flights_between_cities(source, destination):
    result = [flight for flight in flights if flight.source == source and flight.destination == destination]
    return result
ch="y"
while ch=="y" or ch=="Y":

    print("Choose search option:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        city = input("Enter city: ")
        result = search_flights_by_city(city)
    
    elif choice == 2:
        source = input("Enter source city: ")
        result = search_flights_from_city(source)
    
    elif choice == 3:
        source = input("Enter source city: ")
        destination = input("Enter destination city: ")
        result = search_flights_between_cities(source, destination)
    
    else:
        print("Invalid choice. Please choose a valid option.")
        result = []

    if result:
        print("Flight ID\tSource\tDestination\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")
    else:
        print("No flights found.")
    ch=input("Do you wish to continue?(Y/N)")
    if ch=="N" or ch=="n":
        print("Thank You!!")
