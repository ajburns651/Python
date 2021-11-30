# Tells me whether It is my turn to do chores or my sisters to
import datetime
current_time = datetime.datetime.now() 

if current_time.day%2 == 0:
    print("It is your Sisters's day to do the chores")
else:
    print("It is your day to do the chores")
    