import os

from art import logo

bidders={}
print (logo)
bidder = input("What is your name?: ").lower()
sum=int(input("Whats your bid?: $"))
bidders.update({bidder:sum})
while input("Are there any other bidders? Type 'Y' or 'N'") in ['Y','y']:
    os.system('cls')
    print("Welcom to the secret auction program.")
    bidder = input("What is your name?: ")
    if bidder in bidders:
        print(f"{bidder} already bid!")
        continue
    sum = int(input("Whats your bid?: $"))
    bidders.update({bidder: sum})

print (sorted(bidders,key=lambda x:x[1],reverse=True)[0].capitalize())
