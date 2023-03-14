# print the proce of Coke
# insert coin, where accepts only 25; 10 and 5 coins.
# if insert coin is 50 no amount owed.
# if you insert 25, 10 or 5 five calculation how much do you owed 
# ignore any integer that isn’t an accepted denomination

amount_due = 50
print("Amount Due: ", amount_due)



while amount_due > 0:
    insert_coin = int(input("Insert Coin: "))
    match insert_coin:
        case 25 | 10 | 5:
            amount_due -= insert_coin 
            print("Amount Due: ",amount_due)
            continue
        case _:
            continue
print("Amount Due: ",amount_due)

    


