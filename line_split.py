class CustomDataStructure:
    def __init__(self):
        self.data = {}

    def add_point(self, key, point):
        if key not in self.data:
            self.data[key] = [point]
        else:
            self.data[key].append(point)

    def get_points(self, key):
        return self.data.get(key, [])

    def iterate(self):
        for key, points in self.data.items():
            print(f"Key: {key}, Points: {points}")


def find_union(intervals):
    # Sort intervals based on starting point
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    # Initialize the result list with the first interval
    temp = [sorted_intervals[0]]

    for i in range(1, len(sorted_intervals)):
        current_interval = sorted_intervals[i]
        last_interval = temp[-1]

        # Check for overlap and merge intervals if needed
        if current_interval[0] <= last_interval[1]:
            # Overlapping intervals, update the end point of the last interval
            temp[-1] = (last_interval[0], max(last_interval[1], current_interval[1]))
        else:
            # Non-overlapping interval, add it to the result list
            temp.append(current_interval)

    return temp


def add_lines(room, horizontal_lines, vertical_lines):
    # Given a rectangle as a list of corners, add its unique line segments to the lines dictionary
    rectangle = room.corners
    for i in range(len(rectangle)):
        start_point = tuple(rectangle[i])
        end_point = tuple(rectangle[(i + 1) % len(rectangle)])
        if(start_point[0] == end_point[0]): # vertical line
            keypoint = start_point[0]
            if(start_point[1] < end_point[1]):
                vertical_lines.add_point(keypoint,(start_point[1],end_point[1]))
            else:
                vertical_lines.add_point(keypoint,(end_point[1],start_point[1]))              
        else :  # horizontal line
            keypoint = start_point[1]
            if(start_point[0] < end_point[0]):
                horizontal_lines.add_point(keypoint,(start_point[0],end_point[0]))
            else:
                horizontal_lines.add_point(keypoint,(end_point[0],start_point[0]))   


def arrange_lines(lines,horozintal_lines,vertical_lines):
    for key in vertical_lines.data.keys():
        data = []   
        for point in vertical_lines.get_points(key):
            data.append(point)
        finaldata = find_union(data)
        lines.extend(((key, point[0]), (key, point[1])) for point in finaldata)
    for key in horozintal_lines.data.keys():
        data = []   
        for point in horozintal_lines.get_points(key):
            data.append(point)
        finaldata = find_union(data)
        lines.extend(((point[0],key), (point[1],key)) for point in finaldata)

