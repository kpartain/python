road1 = ".X..X"
road2 = "X.XXXXX.X."
road3 = "XX.XXX.."
road4 = "XXXX"

def Fixin_potholes(road_string):
    sets_of_potholes_fixed = 0
    current_index = 0
    pothole_counter_in_loop = 0
    while current_index != len(road_string):
        if road_string[current_index] == ".":
            pothole_counter_in_loop = 0
        if road_string[current_index] == "X":
            if pothole_counter_in_loop < 3:
                pothole_counter_in_loop += 1
                if()
            elif pothole_counter_in_loop >= 3:
                pothole_counter_in_loop = 0
        current_index += 1
    return sets_of_potholes_fixed

print(Fixin_potholes(road1)) #2
print(Fixin_potholes(road2)) #3 5
print(Fixin_potholes(road3)) #2 5
print(Fixin_potholes(road4)) #2 3