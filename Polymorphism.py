#Parent class
class Concert:
    bandName = "Unknown"
    venue = "Unknown"
    address = "Unknown"

    def getConcertInfo(self):
        band_entry = input("Enter the band name ")
        venue_entry = input ("Where are you going to see them? ")
        address_entry = input ("If you know the address, please enter it. ")
        if (band_entry == self.bandName and venue_entry == self.venue) :
            print ('Party on Dude!')
        else:
            print("The selected band is not playing at this venue.")

#Child class refreshments
class Refreshments(Concert):
    refreshments = "Popcorn"
    department = "Concessions"
    refreshment_id = "1000"

"""While using most of the same elements found in the method in the parent class, we're changing
venue_entry to refreshment_id, if this works it will teach me how to show that at a particular concert
we can find what's in the concession stand"""
def getConcertInfo(self):
        band_entry = input("Enter the band name ")
        entry_refreshmentId = input ("What is the refreshment ID? ")
        address_entry = input ("If you know the address, please enter it. ")
        if (band_entry == self.bandName and entry_refreshmentId == self.refreshment_id) :
            print ('Party on Dude!')
        else:
            print("This band doesn't serve that sort of refreshment.")

#Child class instruments
class Instruments(Concert):
    instruments = "guitar"
    accessories = "amp"
    sound = "loud"

# This time we're changing from venue_entry to account for instruments
    def getConcertInfo(self):
        band_entry = input("Enter the band name ")
        entry_instruments = input("What instruments do they play? ")
        address_entry = input ("If you know the address, please enter it. ")
        if (band_entry == self.bandName and entry_instruments == self.instruments) :
            print ('Party on Dude!')
        else:
            print("They don't play those instruments.")

#The following code hopefully invokes the methods inside each class for Concert, Refreshments, and Instruments

metallica = Concert()
metallica.getConcertInfo()

popcorn = Refreshments()
popcorn.getConcertInfo()

cello = Instruments()
cello.getConcertInfo()
        
