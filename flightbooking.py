class Flight:
   
    def __init__(self, flight_id, origin, destination, seats):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.booked_seats = 0   

   
    def book_seat(self):
        if self.booked_seats < self.seats:
            self.booked_seats += 1
            return True
        return False

    
    def __str__(self):
        return f"Flight ID: {self.flight_id}, Origin: {self.origin}, Destination: {self.destination}, Seats: {self.seats}, Available: {self.seats - self.booked_seats}"


class Flightbooking:
    def __init__(self):
        self.flights = {}

    def add_sample_flights(self):
        
        self.flights['F101'] = Flight('F101', 'Delhi', 'Patna', 10)
        
        self.flights['A102'] = Flight('A102', 'Lucknow', 'Patna', 9)
        
        self.flights['B103'] = Flight('B103', 'Canada', 'New Delhi', 7)
        
        self.flights['A107'] = Flight('A107', 'New Delhi', 'Russia', 40)

   
    def view_flights(self):
        if not self.flights:
            print("No flight available.")
            return

        print("\nAvailable Flights:")
        for flight in self.flights.values():
            print(flight)

   
    def book_flight(self, flight_id):
        if flight_id not in self.flights:
            print("Flight ID not found.")
            return

        flight = self.flights[flight_id]
        if flight.book_seat():
            print("Seat booked successfully!")
        else:
            print("No seats available on this flight")

   
    def search_flights(self, origin, destination):
        print(f"\nSearching for flights from {origin} to {destination}!")
        found = False

        for flight in self.flights.values():
            if (flight.origin.lower() == origin.lower() and
                flight.destination.lower() == destination.lower()):
                print(flight)
                found = True

        if not found:
            print("No flights found for the specific route.")

    
    def run(self):
        print("Welcome to the Flight Booking App!")
        self.add_sample_flights()

        while True:
            print("\n--- Main Menu ---")
           
            print("1. View Flights")
            
            print("2. Book a Flight")
            
            print("3. Search Flights")
            
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_flights()
            
            elif choice == "2":
                flight_id = input("Enter the flight ID to book: ")
                self.book_flight(flight_id)
            
            elif choice == "3":
                origin = input("Enter origin: ")
                destination = input("Enter destination: ")
                self.search_flights(origin, destination)
            
            elif choice == "4":
                print("Thank you for using the flight booking app. Have a great day!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = Flightbooking()
    app.run()   


    