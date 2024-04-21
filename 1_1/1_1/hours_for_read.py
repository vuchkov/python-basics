pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_to_read = pages // pages_per_hour // days
print(hours_to_read)
