#function to determine the shortest path
import math

def sort_destinations(destinations):
    
    sorted_list = [destinations[0]]
    remaining = destinations[1:]
    while remaining:
        current_x, current_y = sorted_list[-1]
        closest_index = 0
        closest_distance = float('inf')
        for i in range(len(remaining)):
            x, y = remaining[i]
            distance = math.sqrt((x - current_x)**2 + (y - current_y)**2)
            if distance < closest_distance:
            closest_distance = distance
            closest_index = i
        sorted_list.append(remaining[closest_index])
        remaining.pop(closest_index)
    
    return sorted_list
