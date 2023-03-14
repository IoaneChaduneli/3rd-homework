
# print the proce of Coke
amount_due = 50
print("Amount Due: ", amount_due)



while amount_due > 0:
    insert_coin = int(input("Insert Coin: "))
    match insert_coin:
# insert coin, where accepts only 25; 10 and 5 coins.
        case 25 | 10 | 5:
            amount_due -= insert_coin 
            # if you insert 25, 10 or 5 five calculation how much do you owed 
            print("Amount Due: ",amount_due)
            continue
        # ignore any integer that isn’t an accepted denomination
        case _:
            continue
print("Amount Due: ",amount_due)

    


