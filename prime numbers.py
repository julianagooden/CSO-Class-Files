def primchecker (number):
    for x in range (2,number): 
        if x % number == 0:
            return 'not prime'
    