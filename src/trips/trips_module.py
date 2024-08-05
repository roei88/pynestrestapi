from nest.core import Module
from .trips_controller import TripsController
from .trips_service import TripsService


@Module(
    controllers=[TripsController],
    providers=[TripsService],
    imports=[]
)   
class TripsModule:
    pass

    