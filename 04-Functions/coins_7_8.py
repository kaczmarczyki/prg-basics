def f(amount_to_pay):
    #coins = 1,2,5
    rest_of_five = amount_to_pay%5
    amount_of_fives = (amount_to_pay-rest_of_five)/5
    rest_of_two = rest_of_five % 2
    amount_of_twos = (rest_of_five-rest_of_two)/2
    amount_of_ones = rest_of_two 

    amount_of_coins = int(amount_of_fives + amount_of_twos + amount_of_ones)

    return amount_of_coins
def main():
    amount = int(input("Enter amount to pay: "))
    rest_without_fives = f(amount)
    print(rest_without_fives)


if __name__ == "__main__":
    main() 