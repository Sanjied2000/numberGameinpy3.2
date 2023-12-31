# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cs_Uzeai1ZWUu-QWYjrHW370eJve8p12
"""

#idea: Sanjied Ahamed.Aust CSE 45, 3.2 ai project
import random

def generate_random_number():
    return random.randint(21, 29)

def ai_move(numbers,opNumbers,rNUM):
    best_score = float("-inf")
    best_move = None

    for move in numbers:
        updated_rNUM = rNUM - move
        if updated_rNUM % 10 == 0:
            continue

        score = evaluate_move(updated_rNUM,opNumbers, move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def evaluate_move(updated_rNUM,opNumbers, move):
    score = 0
    if updated_rNUM % 10 == 5:
        score += 5
    if move == 3:
      score += 3
      for danger in opNumbers:
        newUpdated_num=updated_rNUM-danger;
        if newUpdated_num % 10 == 5:
         score=-1


    if move == 2:
        score += 2
        for danger in opNumbers:
          newUpdated_num=updated_rNUM-danger;
          if newUpdated_num % 10 == 5:
           score=-2
    if move == 1:
        score += 1
        for danger in opNumbers:
           newUpdated_num=updated_rNUM-danger;
           if newUpdated_num % 10 == 5:
            score=-3


    return score

def main():
    X = [1, 2, 3]
    Y = [1, 2, 3]
    Z = [1, 2, 3]
    rNUM = generate_random_number()

    human_moves = []
    ai_moves = []

    players = ["Human", "AI"]
    current_player = random.choice(players)
    skip_next_move = False
    prev_rNUM_mod_10 = False

    Human_Point = 0
    Ai_Point = 0

    while True:
        print("Current rNUM:", rNUM)
        if current_player == "Human":
            print("Numbers to choose from:", X)
        else:
            print("Numbers to choose from AI:", Z)

        # Check if rNUM % 10 == 0, and if so, declare the current player as the winner
        if rNUM % 10 == 0:
            print(current_player, "wins! Num has a Zero !!!.")
            break

        # Check if rNUM % 10 == 5, and if so, skip the next move
        if rNUM % 10 == 5 and not skip_next_move and not prev_rNUM_mod_10:
            print("Current player will skip the next move.")
            skip_next_move = True
        else:
            skip_next_move = False
            prev_rNUM_mod_10 = rNUM % 10 == 0

            # Ask the current player for their choice
            while True:
                try:
                    if current_player == "Human":
                        choice = int(input("Human, choose a number from the list (X): "))
                        if choice in X:
                            X = Y.copy()
                            X.remove(choice)
                            human_moves.append(choice)
                            Human_Point += choice
                            break
                        else:
                            print("Invalid choice. Please select a number from the list.")
                    else:
                        choice = ai_move(Z,X,rNUM)
                        Z = Y.copy()
                        Z.remove(choice)
                        ai_moves.append(choice)
                        print("AI choose:", choice)
                        Ai_Point += choice
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            rNUM -= choice


        print("Human Points:", Human_Point)
        print("AI Points:", Ai_Point)
        print("____________________________")

        # Switch to the other player for the next turn
        current_player = "Human" if current_player == "AI" else "AI"

        # Check if rNUM is negative, and if so, declare the winner based on points
        if rNUM < 0:
            print("Game Over. rNUM is now less than 0.")
            if Human_Point > Ai_Point:
                print("Human wins with", Human_Point, "points!")
            elif Ai_Point > Human_Point:
                print("AI wins with", Ai_Point, "points!")
            else:
                print("It's a tie! Both players have the same points.")
            break


main()