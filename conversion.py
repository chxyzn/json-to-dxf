import json

class Room:
    def __init__(self, index, corners, width, height, area):
        self.index = index
        self.corners = corners
        self.width = width
        self.height = height
        self.area = area

def rooms_from_json(data):
    rooms = []
    for index, data in data.items():
        rect = Room(int(index), data['corners'], data['width'], data['height'], data['area'])
        rooms.append(rect)
    return rooms

def rooms_to_json(rooms):
    for room in rooms:
        room_data = {
            'index': room.index,
            'corners': room.corners,
            'width': room.width,
            'height': room.height,
            'area': room.area
        }
        print(json.dumps(room_data,indent=4))



