from datetime import date, datetime
from .trips_model import Trip
from functools import lru_cache
from nest.core import Injectable

@Injectable
class TripsService:
    def __init__(self):
        self.database = []
        mock_trip = Trip(
            id="trip123",
            owner="owner1",
            label="Summer Vacation",
            type="Leisure",
            sub_type="Beach",
            destination="Hawaii",
            start_date=date(2025, 1, 1),
            num_of_days=7,
            created_at=date(2024, 8, 1),
            updated_at=date(2024, 8, 5),
            is_deleted=False
        )
        self.database.append(mock_trip)
        
    def get_trips(self):
        return self.database
    
    def add_trip(self, trip: Trip):
        self.database.append(trip)
        return self.database
        
    def update_trip(self, trip: Trip):
        for index, existing_trip in enumerate(self.database):
            if existing_trip.id == trip.id:
                self.database[index] = trip
                break
        return self.database
    
    def delete_trip(self, trip: Trip):
        self.database = [existing_trip for existing_trip in self.database if existing_trip.id != trip.id]
        return self.database