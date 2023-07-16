import ascii_art
import os

print(ascii_art.logo)
print("Welcome to the secret auction program.")
game = "yes"

auction = {}
while game == 'yes':
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    game = input("Are there other bidders in the room? Type 'yes' or 'no': ").lower()
    while game != 'yes' and game != 'no':
        print("Invalid input!")
        game = input("Are there other bidders in the room? Type 'yes' or 'no': ").lower()

    auction[name] = bid
    os.system('cls')

maxbid = 0
maxbidder = "No one."
for key in auction:
    if auction[key] > maxbid:
        maxbid = auction[key]
        maxbidder = key

print(f"The winner is {maxbidder} with the bid of ${maxbid}.")
