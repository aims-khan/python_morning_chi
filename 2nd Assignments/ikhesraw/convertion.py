CONVERTION_FACTOR = 0.621371

user_input = float(input('How many (KM)s you want to run/cycle today:.\n'))
# convert KM to Miles
miles = user_input * CONVERTION_FACTOR

print(f'Your {user_input} KM ride is equal to {miles} Miles!')
