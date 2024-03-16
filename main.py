import random

from art import logo

import os

#Rules:
#hit = get 1 more card
#stand = do not get more cards
#your score is the sum of your cards
#cards that are 10 or higher all count as 10s, that's why 12,13,14 missing
#ace is 11 if your hand is under 21, but it transforms into 1 if 11 would bust the hand
#the one closer to 21 (but not higher) wins
#21 is blackjack (best hand)
#dealer(computer) draws untill their hand is atleast 17

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("Welcome to Blackjack!\n")

player = []
dealer = []


def card_deal(dealed_part):
  card = random.choice(cards)
  dealed_part.append(int(card))


def cards_sum(dealed_part):
  sum = 0
  for i in dealed_part:
    sum += i
  return sum


def ace_check(dealed_part):
  if cards_sum(dealed_part) > 21:
    for i in range(len(dealed_part)):
      if int(dealed_part[i]) == 11:
        dealed_part[i] = 1


end_of_game = False

while not end_of_game:
  os.system('clear')
  print(logo)
  player = []
  dealer = []
  card_deal(player)
  card_deal(player)
  card_deal(dealer)

  print(f"Your cards: {player}  | score: {cards_sum(player)}")
  print(f"Dealer cards: {dealer}  | score: {cards_sum(dealer)}")

  ace_check(player)

  player_deal_flag = True

  while player_deal_flag:

    if cards_sum(player) < 21:
      choice = input("\nType 'y' for hit or 'n' for stand: ")
      if choice == "y":
        card_deal(player)
        ace_check(player)
        print(f"\nYour cards: {player}  | score: {cards_sum(player)}")
      elif choice == "n":
        player_deal_flag = False
      else:
        print("Please pick a valid choice")
    else:
      player_deal_flag = False

  if cards_sum(player) < 21:
    while cards_sum(dealer) < 17:
      card_deal(dealer)
    print(f"\nDealer cards: {dealer}  | score: {cards_sum(dealer)}\n")

  if cards_sum(player) > 21:
    print("You lose. It's a bust.")
  elif cards_sum(player) == 21:
    print("You win! BLACKJACK!")
  elif cards_sum(player) == cards_sum(dealer):
    print("It's a draw.")
  else:
    if cards_sum(dealer) > 21 or cards_sum(dealer) < cards_sum(player):
      print("You win!")
    elif cards_sum(dealer) > cards_sum(player) and cards_sum(dealer) <= 21:
      print("You lose.")

  ace_check(dealer)

  replay_input_validation = False
  while not replay_input_validation:
    replay = input("\nType 'y' for a new game or 'n' if you want to stop: ")
    if replay == 'n':
      end_of_game = True
      print("\nThanks for playing!")
      replay_input_validation = True
    elif replay == 'y':
      print("Good luck!\n")
      replay_input_validation = True
    else:
      print("Please introduce valid input")
