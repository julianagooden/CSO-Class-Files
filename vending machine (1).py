def vendingmachine (money, choice):
    drinks = ['pepsi', 'water', 'powerade']
    if money < 1.25:
        print "not enough"
    elif money >= 1.25:
            if choice.lower() in drinks:
                return (choice.lower(), 'your change is' + str(money - 1.25))
            else:
                    return (money, "choice unavailable")