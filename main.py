
# создать дикт со значениями тестовьіми
with open('nov.csv') as schedule:
    content = schedule.readlines()
    # print(type(content))
    print(content[0])

# def today_shift():
#     date = (input('write today is date:'))
#     if date in content:
#         print('true')
#
#
# print(today_shift())