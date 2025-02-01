"""
Author: Brian Aldrin R.Pagsolingan
Assignment: Assignment 1
"""

gym_member = "Alex Alliton"    #string
preferred_weight_kg = 20.5     #float
highest_reps = 25              #int
membership_active = True       #boolean

#Dictionary with friend name as keys and tuples of workouts (yoga, running, weightlifting) as values
workout_stats = {
    "Alex" : (20,45,90),
    "Jamie" : (30,23,120),
    "Taylor" : (40,15,111),
}
workout_stats_copy = {
    "Alex" : (20,45,90),
    "Jamie" : (30,23,120),
    "Taylor" : (40,15,111),
}
for name in workout_stats_copy:# loop a copy of dictionary to avoid runtime error
    total = 0
    for minutes in workout_stats[name]:
        total += minutes
    workout_stats[f"{name}_total"] = total # add new key:value in original dictionary
print(workout_stats)

workout_list =[list(minutes) for minutes in workout_stats_copy.values()] # 2d array containing all minutes
total_yoga_running = 0
total_weightlifting = 0
for minutes in workout_list:
    total_yoga_running += sum(minutes[:2])
for minutes in workout_list[-2:]:
    total_weightlifting += sum(minutes[-1:])
print("Amount of minutes spent doing yoga and running: ", total_yoga_running)
print("Amount of minutes spent doing weightlifting by last 2 friends: ", total_weightlifting)

friend_totals = list(workout_stats.keys())[-3:] # last 3 keys already have totals
for friend in friend_totals:
    if workout_stats[friend] > 120:
        print(f"Great job staying active, {friend[:-6]}!") # slice the "_total"

friend_search = input("Enter a friend's name: ").strip().title() # remove white space and capitalize first letter
if friend_search in workout_stats:
    print(f"{friend_search}'s workout minutes: {workout_stats[friend_search]}")
    print(f"{friend_search} has worked out for a total of {sum(workout_stats[friend_search])}")
else:
    print(f"Sorry, {friend_search} was not found in the records.")

print("Workout Summary:")
total_minutes = dict(list(workout_stats.items())[-3:]) # Take the last 3 key:value pairs and put in separate dictionary

max_friend = max(total_minutes, key=total_minutes.get)
max_minutes = total_minutes[max_friend]

min_friend = min(total_minutes, key=total_minutes.get)
min_minutes = total_minutes[min_friend]

print(f"The person who worked out the most is {max_friend[:-6]}. with a total of {max_minutes} minutes.")
print(f"The person who worked out the least is {min_friend[:-6]}. with a total of {min_minutes} minutes.")
