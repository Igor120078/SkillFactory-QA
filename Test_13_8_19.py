# Test 13.8.19

SEP1 = '*' * 50
SEP2 = '=' * 50


def main():
    guests = get_guests_age(get_tickets_number())
    total_price = get_tickets_price(guests)
    print(SEP2)
    print(f"Your total price is: {round(total_price, 2)}$")


def get_tickets_number():
    print(SEP1, 'Welcome to our price-calculating system'.center(50), SEP1, sep='\n')
    try:
        tickets = int(input("Enter a number of tickets you want to buy: "))
        if tickets <= 0:
            wrong_input()
            exit()
        print(SEP2)
        return tickets
    except ValueError:
        wrong_input()
        exit()


def get_guests_age(num):
    guests = {}
    for n in range(1, num + 1):
        try:
            age_ = int(input(f'Enter the age of the guest #{n}: '))
            if age_ <= 0:
                wrong_input()
                exit()
            guests['guest_' + str(n)] = age_
        except ValueError:
            wrong_input()
            exit()

    return guests


def get_discount(guests):
    if len(guests) > 3:
        discount = 0.1
    else:
        discount = 0
    return discount


def get_tickets_price(guests):
    total_price = 0
    discount = get_discount(guests)
    for age in guests.values():
        if age < 18:
            continue
        elif 18 <= age <= 25:
            total_price += 990
        else:
            total_price += 1390
    total_price *= (1 - discount)
    return total_price


def wrong_input():
    print(SEP2, 'Sorry, but you have to enter a whole positive number.',
          'See you next time.', sep='\n')


if __name__ == '__main__':
    main()
