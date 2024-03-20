balance=100000
deposit=int(input())
print("deposit amount:",deposit)
Availablebalance=balance+deposit
print("Available Balance:",Availablebalance)
withdrawl=int (input())
if withdrawl>Availablebalance:
    print("Insufficient balance can't withdrawl")
else:
    print("withdrawl succesfully completed:")
    
    

        
