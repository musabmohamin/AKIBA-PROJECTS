#WEEK 1 TASK 7 TRAVEL PLANNER
destination=input("Enter your destination :")
distance_in_kilometer=float(input("Enter distance in kilometer :"))
average_speed=float(input("Enter average speed in kilometer per hour :"))
time=distance_in_kilometer/average_speed
minutes=time*60
print("Destination",destination,)
print("Distance",distance_in_kilometer,"KM")
print("Average speed",average_speed,"km/hr")
print("Estimated travel time in hour",time,"hour")
print("Estimated travel time in minutes",minutes,"minutes")