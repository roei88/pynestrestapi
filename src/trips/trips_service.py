from datetime import datetime
from fastapi import HTTPException
from .trips_model import Trip
from nest.core import Injectable
from pymongo import MongoClient
from pymongo.collection import Collection

mongo_uri = "mongodb://localhost:27017/"
db_name = "trips_db"
collection_name = "trips"
    
@Injectable
class TripsService:
    def __init__(self):
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection: Collection = self.db[collection_name]
        self.init_mock()

    def init_mock(self):
        mock_trip = {
            "id": "trip123",
            "owner": "owner1",
            "label": "Summer Vacation",
            "type": "Leisure",
            "sub_type": "Beach",
            "destination": "Hawaii",
            "start_date": datetime(2025, 1, 1),
            "num_of_days": 7,
            "created_at": datetime(2024, 8, 1),
            "updated_at": datetime(2024, 8, 5),
            "is_deleted": False
        }
        existingMock = self.collection.find_one({"id": mock_trip["id"]})
        if existingMock:
            return
        self.collection.insert_one(mock_trip)

    def get_trips(self):
        trips = self.collection.find()
        return [self._trip_from_db(trip) for trip in trips]
    
    def add_trip(self, trip: Trip):
        if (self.collection.find_one({"id": trip.id})):
            return HTTPException(status_code=400, detail="Trip already exist") 
        
        trip.created_at = datetime.now()
        trip.updated_at = datetime.now()
        trip.is_deleted = False
        trip_dict = self._trip_to_dict(trip)
        self.collection.insert_one(trip_dict)
        return trip
    
    def update_trip(self, trip: Trip):
        if not (self.collection.find_one({"id": trip.id})):
            return HTTPException(status_code=404, detail="Trip not found")   

        trip_dict = self._trip_to_dict(trip, True)
        existing_trip: Trip = self._trip_from_db(self.collection.find_one({"id": trip.id}))

        if trip.owner and trip.owner is not None:
            existing_trip.owner = trip.owner

        if trip.label and trip.label is not None:
            existing_trip.label = trip.label
        
        if trip.type and trip.type is not None:
            existing_trip.type = trip.type
    
        if trip.sub_type and trip.sub_type is not None:
            existing_trip.sub_type = trip.sub_type

        if trip.destination and trip.destination is not None:
            existing_trip.destination = trip.destination

        if trip.start_date and trip.start_date is not None:
            existing_trip.start_date = trip.start_date
        
        if trip.num_of_days and trip.num_of_days is not None:
            existing_trip.num_of_days = trip.num_of_days

        if trip.is_deleted and trip.is_deleted is not None:
            existing_trip.is_deleted = trip.is_deleted

        existing_trip.updated_at = datetime.now()
        self.collection.update_one({"id": trip.id}, {"$set": trip_dict})
        return self.get_trips()
    
    def delete_trip(self, trip: Trip):
        if not (self.collection.find_one({"id": trip.id})):
            return HTTPException(status_code=404, detail="Trip not found")   

        self.collection.update_one({"id": trip.id}, {"$set": {"is_deleted": True}})
        return self.get_trips()
        
    def _trip_from_db(self, trip_doc):
        return Trip(
            id=trip_doc["id"],
            owner=trip_doc["owner"],
            label=trip_doc["label"],
            type=trip_doc["type"],
            sub_type=trip_doc["sub_type"],
            destination=trip_doc["destination"],
            start_date=trip_doc["start_date"],
            num_of_days=trip_doc["num_of_days"],
            created_at=trip_doc["created_at"],
            updated_at=trip_doc["updated_at"],
            is_deleted=trip_doc["is_deleted"]
        )

    def _trip_to_dict(self, trip, exclude_unset = False):
        trip_dict = trip.dict()
        if exclude_unset:
            trip_dict = trip.dict(exclude_unset=True)
        return trip_dict 
