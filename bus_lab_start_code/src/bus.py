class Bus: 

    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)
    
    def empty(self):
        self.passengers = []
    
    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.passengers.append(passenger)
        bus_stop.clear()
    
    def pick_up_from_stop_2(self, bus_stop):
        passenger_to_remove = []
        for passenger in bus_stop.queue:
            if self.destination == passenger.destination:
                self.passengers.append(passenger)
                passenger_to_remove.append(passenger)
        for passenger in passenger_to_remove:
            bus_stop.queue.remove(passenger)




                
            
