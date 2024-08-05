from nest.core import Controller, Get, Post, Put, Delete
from .trips_service import TripsService
from .trips_model import Trip

@Controller("/trips")
class TripsController:

    def __init__(self, trips_service: TripsService):
        self.trips_service = trips_service
    
    @Get("/get_trips")
    def get_trips(self):
        return self.trips_service.get_trips()
        
    @Post("/add_trip")
    def add_trip(self, trip: Trip):
        return self.trips_service.add_trips(trip)

    @Put("/update_trip")
    def update_trip(self, trip: Trip):
        return self.trips_service.update_trip(trip)

    @Delete("/delete_trip")
    def add_trip(self, trips: Trip):
        return self.trips_service.delete_trip(trips)
    
