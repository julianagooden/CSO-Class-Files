def fizzbuzz():
    for numbers in range(1,101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print 'fizzbuzz'
        if numbers % 3 == 0:
            print 'fizz'
        if numbers % 5 == 0:
            print 'buzz'
        else:
            print numbers
