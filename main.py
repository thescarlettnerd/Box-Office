print("Welcome to the Box Office!")
movie = input("Today we are showing Princess Mononoke, The Princess Bride, and Die Hard. Which would you like to see?\n")

bill = 0

if movie == "The Princess Bride":
  print("The Princess Bride is showing at 3:00pm today.")
  pb_tickets = int(input("How many tickets would you like to purchase?\n"))
  bill = pb_tickets * 15

elif movie == "Princess Mononoke":
  print("Princess Mononoke is showing at 5:30pm today.")
  pm_tickets = int(input("How many tickets would you like to purchase?\n"))
  bill = pm_tickets * 15

elif movie == "Die Hard":
  print("Die Hard is showing at 8:00pm today.")
  dh_tickets = int(input("How many tickets would you like to purchase?\n"))
  bill = dh_tickets * 15

popcorn = input("Would you like popcorn?\nY or N: ")
drink = input("Would you like a drink?\nY or N: ")
if popcorn == "Y":
  bill += 7
if drink == "Y":
  bill += 5

print(f"Please pay ${bill}. Your tickets to {movie} will be available at the theatre box office. Thank you and enjoy the show!")

