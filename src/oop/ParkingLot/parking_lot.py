from parking_lot_model import ParkingLot, ParkingSlotType


n = 10
my_biz = ParkingLot(n)
my_biz.spaces_occupied = 0
print(my_biz.size)
car_type = ParkingSlotType.REGULAR.value
print(f'Requested {car_type} type')
regular_spots_total = my_biz.get_parking_spaces_for_type(car_type)
print(f'Regular spots: {regular_spots_total}')
print(f'Large spots {my_biz.get_parking_spaces_for_type(ParkingSlotType.LARGE)}')
print(f'Small spots {my_biz.small_spaces}')
my_biz.fill_parking_space()
print(my_biz.occupancy)