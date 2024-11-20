from enum import Enum
from dataclasses import dataclass
from collections import defaultdict
from collections import Counter
from collections import namedtuple

class ParkingSlotType(Enum):  
        LARGE = ("van", "v")
        REGULAR = ("car", "c")
        SMALL = ("motorbike", "m")
        
@dataclass        
class ParkingLot():
    size: int
    large_spaces: int
    # regular spaces = size
    small_spaces: int
    total_available: int
    spaces_occupied: int = 0
    occupancy: Counter = None

    
    def __init__(self, parking_size):
        if parking_size > 0:
            self.size = parking_size
            self.total_available = parking_size
            self.large_spaces = self._get_large_spaces_available()
            self.small_spaces = self._get_small_spaces_available()
            self.occupancy = Counter()
        else:
            print("Parking lot requires a size greater than 0")
        
    def __is_full__(self) -> bool:
        return self.spaces_occupied == self.size
    
    def __is_empty__(self) -> bool:
        return self.spaces_occupied == 0
    
    def _get_large_spaces_available(self):
        self.large_spaces = int(self.total_available / 1.5)
        return self.large_spaces
    
    def _get_small_spaces_available(self):
        self.small_spaces = self.total_available * 3
        return self.small_spaces
    
    def get_parking_spaces_for_type(self, slot_type: ParkingSlotType):
        if slot_type == ParkingSlotType:
            return self._get_large_spaces_available()
        elif slot_type == ParkingSlotType.SMALL:
            return self._get_small_spaces_available()
        else:
            return self.size
    
    # def fill_parking_space(self, slot_type: ParkingSlotType):
    def fill_parking_space(self):
        self.occupancy['c']
        print(self.occupancy)