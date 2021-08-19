#Simple program to help me check the water levels on each building.

while True:
    print ("Enter a number")
    number = input()
    print('Enter a timeframe')
    days = input()
    result = (float(number) / float(days))
    print ('Average cost for ' + str(days) + ' days = $' + str(round(result, 2)))
    print ('')

