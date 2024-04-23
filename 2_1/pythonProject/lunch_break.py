import math

LUNCH_TIME = 1 / 8
REST_TIME = 1 / 4

series_name = input()
episode_length = int(input())
break_length = int(input())

time_for_lunch = break_length * LUNCH_TIME
time_for_rest = break_length * REST_TIME

remaining_time_for_episode = break_length - time_for_lunch - time_for_rest

if remaining_time_for_episode >= episode_length:
    remaining_time_for_rest = remaining_time_for_episode - episode_length
    remaining_time_for_rest = math.ceil(remaining_time_for_rest)
    print(f"You have enough time to watch {series_name} and left with {remaining_time_for_rest} minutes free time.")
else:
    time_needed = episode_length - remaining_time_for_episode
    time_needed = math.ceil(time_needed)
    print(f"You don't have enough time to watch {series_name}, you need {time_needed} more minutes.")
