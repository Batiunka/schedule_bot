import datetime
schedule = {19:'L',20:'E',21:'M',22:'E',23:'L',24:'L'}
print(schedule.get(200,'hello world!'))
while True:
    user_command = input('''If you want to knot today's shift write 1
If you want to know tomorrow's shift write 2
if you want to download schedule write 3\n''')
    if user_command == '1':
        print(schedule.get(datetime.datetime.now().day, "I don't have a schedule!"))

    elif user_command == '2':
        print(schedule.get(datetime.datetime.now().day+1, "I don't have a schedule!"))
    elif user_command == '3':
        today = datetime.datetime.now().day
        for x,y in schedule.items():
            if x > today and y == 'L':
                print(x)
                break
    else:
        print('wrong command')

