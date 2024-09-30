# Class to represent a guest in a hotel
class Guest:
    # Initialize the attributes for the class guest
    def __init__(self, name, email, phone_number, address, guest_id, nationality, dob, loyalty_points=0, vip_status=False):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.guest_id = guest_id
        self.nationality = nationality
        self.dob = dob
        self.loyalty_points = loyalty_points
        self.vip_status = vip_status

    # Getter methods of class Guest to get the value of attributes
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_guest_id(self):
        return self.guest_id

    def get_nationality(self):
        return self.nationality

    def get_dob(self):
        return self.dob

    def get_loyalty_points(self):
        return self.loyalty_points

    def get_vip_status(self):
        return self.vip_status

    # Setter methods of class Guest to set the value of attributes
    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_address(self, address):
        self.address = address

    def set_guest_id(self, guest_id):
        self.guest_id = guest_id

    def set_nationality(self, nationality):
        self.nationality = nationality

    def set_dob(self, dob):
        self.dob = dob

    def set_loyalty_points(self, points):
        self.loyalty_points = points

    def set_vip_status(self, status):
        self.vip_status = status

    # Function to display guest details in a hotel
    def display_guest_info(self):
        print("Guest Name: " + self.name)
        print("Email: " + self.email)
        print("Phone Number: " + self.phone_number)
        print("Address: " + self.address)
        print("Guest ID: " + self.guest_id)
        print("Nationality: " + self.nationality)
        print("Date of Birth: " + self.dob)
        print("Loyalty Points: " + str(self.loyalty_points))
        print("VIP Status: " + str(self.vip_status))

    # Scenario 1: Guest Management
    # Use Case 1.1: Register a new guest
    def register_guest(self):
        pass 

    # Use Case 1.2: Update guest information
    def update_guest_info(self):
        pass 

# Class to represent a room in the hotel
class Room:
    def __init__(self, room_number, room_type, price_per_night, floor, availability=True, max_occupancy=2, smoking_allowed=False):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.floor = floor
        self.availability = availability
        self.max_occupancy = max_occupancy
        self.smoking_allowed = smoking_allowed
        self.occupied_by = None

    # Getter methods of class Room to get the value of attributes
    def get_room_number(self):
        return self.room_number

    def get_room_type(self):
        return self.room_type

    def get_price_per_night(self):
        return self.price_per_night

    def get_floor(self):
        return self.floor

    def get_availability(self):
        return self.availability

    def get_max_occupancy(self):
        return self.max_occupancy

    def get_smoking_allowed(self):
        return self.smoking_allowed

    def get_occupied_by(self):
        return self.occupied_by

    # Setter methods of class Room to set the value of attributes
    def set_room_number(self, room_number):
        self.room_number = room_number

    def set_room_type(self, room_type):
        self.room_type = room_type

    def set_price_per_night(self, price_per_night):
        self.price_per_night = price_per_night

    def set_floor(self, floor):
        self.floor = floor

    def set_availability(self, availability):
        self.availability = availability

    def set_max_occupancy(self, occupancy):
        self.max_occupancy = occupancy

    def set_smoking_allowed(self, allowed):
        self.smoking_allowed = allowed

    def set_occupied_by(self, occupied_by):
        self.occupied_by = occupied_by
  
    def is_available(self):  # Add the is_available method
        return self.availability

    # Function to display room details in a hotel
    def display_room_info(self):
        print("Room Number: " + str(self.room_number))
        print("Room Type: " + self.room_type)
        print("Price per Night: AED " + str(self.price_per_night))
        print("Floor: " + str(self.floor))
        print("Availability: " + ("Available" if self.availability else "Occupied"))

    # Scenario 2: Room Management
    # Use Case 2.1: Add a new room to the hotel
    def add_room(self):
        pass 

    # Use Case 2.2: Check room availability
    def check_availability(self):
        pass 

# Class to represent a reservation
class Reservation:
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date, num_guests, special_requests=None, reservation_status="Confirmed", payment_status="Pending"):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.num_guests = num_guests
        self.special_requests = special_requests
        self.reservation_status = reservation_status
        self.payment_status = payment_status
        self.total_cost = 0

    # Getter methods of class Reservation to get the value of attributes
    def get_reservation_id(self):
        return self.reservation_id

    def get_guest(self):
        return self.guest

    def get_room(self):
        return self.room

    def get_check_in_date(self):
        return self.check_in_date

    def get_check_out_date(self):
        return self.check_out_date

    def get_num_guests(self):
        return self.num_guests

    def get_special_requests(self):
        return self.special_requests

    def get_reservation_status(self):
        return self.reservation_status

    def get_payment_status(self):
        return self.payment_status

    def get_total_cost(self):
        return self.total_cost

    # Setter methods of class Reservation to set the value of attributes
    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def set_guest(self, guest):
        self.guest = guest

    def set_room(self, room):
        self.room = room

    def set_check_in_date(self, check_in_date):
        self.check_in_date = check_in_date

    def set_check_out_date(self, check_out_date):
        self.check_out_date = check_out_date

    def set_num_guests(self, num):
        self.num_guests = num

    def set_special_requests(self, requests):
        self.special_requests = requests

    def set_reservation_status(self, status):
        self.reservation_status = status

    def set_payment_status(self, status):
        self.payment_status = status

    def set_total_cost(self, cost):
        self.total_cost = cost

    # Function to calculate total cost
    def calculate_total_cost(self):
        pass  # Logic to calculate the total reservation cost

    # Function to display reservation details in a hotel
    def display_reservation_info(self):
        print("Reservation ID: " + self.reservation_id)
        print("Guest Name: " + self.guest.name)
        print("Room Number: " + str(self.room.room_number))
        print("Check-in Date: " + self.check_in_date)
        print("Check-out Date: " + self.check_out_date)
        print("Number of Guests: " + str(self.num_guests))
        print("Reservation Status: " + self.reservation_status)

    # Scenario 3: Reservation Management
    # Use Case 3.1: Create a new reservation
    def create_reservation(self):
        pass 

    # Use Case 3.2: Cancel an existing reservation
    def cancel_reservation(self):
        pass

# Class to represent the hotel management system
class Hotel:
    def __init__(self, name, location, rating, total_rooms, available_rooms, star_rating, contact_info):
        self.name = name
        self.location = location
        self.rating = rating
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.star_rating = star_rating
        self.contact_info = contact_info
        self.rooms = []  # List to store Room objects
        self.reservations = []  # List to store Reservation objects

    # Getter methods of class Hotel to get the value of attributes
    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_rating(self):
        return self.rating

    def get_total_rooms(self):
        return self.total_rooms

    def get_available_rooms(self):
       return self.available_rooms

    def get_star_rating(self):
       return self.star_rating

    def get_contact_info(self):
       return self.contact_info

   # Setter methods of class Hotel to set the value of attributes
    def set_name(self, name):
       self.name = name

    def set_location(self, location):
       self.location = location

    def set_rating(self, rating):
       self.rating = rating

    def set_total_rooms(self, total):
       self.total_rooms = total

    def set_available_rooms(self, available):
       self.available_rooms = available

    def set_star_rating(self, star_rating):
       self.star_rating = star_rating

    def set_contact_info(self, contact_info):
       self.contact_info = contact_info

   # Function to add a new room to the hotel
    def add_room(self, room):
        self.rooms.append(room)
        self.total_rooms += 1
        if room.availability:  
            self.available_rooms += 1

    def make_reservation(self, reservation):
        if reservation.room.is_available():  # Call the is_available method
            self.reservations.append(reservation)
            reservation.room.set_availability(False)  # Mark room as not available using the setter method
            self.available_rooms -= 1
        else:
            print("Room " + str(reservation.room.room_number) + " is not available.")

    # Function to display all reservations
    def display_all_reservations(self):
        for reservation in self.reservations:
            reservation.display_reservation_info()

    # Function to display hotel details
    def display_hotel_info(self):
        print("Hotel Name: " + self.name)
        print("Location: " + self.location)
        print("Rating: " + str(self.rating) + " stars")
        print("Total Rooms: " + str(self.total_rooms))
        print("Star Rating: " + str(self.star_rating))
        print("Contact Info: " + self.contact_info)

# Example usage

# Creating guest object
print("Guest Information")
guest1 = Guest("Aisha", "aisha@gmail.com", "555-1234", "Abu Dhabi Street 5", "G001", "UAE", "1990-05-15")
guest1.display_guest_info()
print()

# Creating room objects
print("Room Information")
room1 = Room(101, "Single", 100, 1) 
room2 = Room(102, "Double", 150, 2) 

room1.display_room_info()
room2.display_room_info()
print()

# Creating a hotel object
print("Hotel Information")
hotel = Hotel("Grand Abu Dhabi Hotel", "Abu Dhabi", 5, 200, 150, 5, "+971 2 123 4567") 
hotel.display_hotel_info()
print()

# Adding rooms to the hotel
hotel.add_room(room1)
hotel.add_room(room2)

# Creating reservation object
reservation1 = Reservation("R001", guest1, room1, "2024-10-01", "2024-10-05", 2) 

# Making a reservation for a guest
print("Reservation Information")
hotel.make_reservation(reservation1)
print()

# Displaying all reservations
print("All Reservations")
hotel.display_all_reservations()

