# Rocket launch details
mission_name = "Lunar Explorer"
fuel_capacity = 100  # fuel 100% full
fuel_used = 35  # fuel 35% used
distance_to_moon = 384400  #  in km

# Calculate remaining fuel
fuel_remaining = fuel_capacity - fuel_used

# Using f-string
print(f"Mission: {mission_name}")

# Using .format() method
print("Total Distance to Moon: {:,} km".format(distance_to_moon))  # Add along comma separators

# Using % formatting for fuel status
print("Fuel Capacity: %d%%, Fuel Used: %d%%, Fuel Remaining: %d%%" % (fuel_capacity, fuel_used, fuel_remaining))

# Using f-string for countdown
for i in range(5, 0, -1):
    print(f"T-{i} seconds...")

# Using comma separation for final launch message
print("\n", " Lift-off!", "Mission Started!", "Good Luck Astronauts!", sep=" | ")

'''
===OUTPUT===
Mission: Lunar Explorer
Total Distance to Moon: 384,400 km
Fuel Capacity: 100%, Fuel Used: 35%, Fuel Remaining: 65%
T-5 seconds...
T-4 seconds...
T-3 seconds...
T-2 seconds...
T-1 seconds...

 | 🚀 Lift-off! | Mission Started! | Good Luck Astronauts!
 '''
