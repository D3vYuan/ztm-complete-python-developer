from character import PlayerCharacter

if __name__ == "__main__":
    player1 = PlayerCharacter('Cindy', 44)
    player2 = PlayerCharacter('Tom', 34)

    player1.shout()
    print(f"{player1.name} is {player1.age} years old - {player1.membership}")
    # print(player1.adding_things(3, 3))

    player2.shout()
    print(f"{player2.name} is {player2.age} years old - {player2.membership}")
    # print(player2.adding_things(1, 3))

    player3 = PlayerCharacter.adding_things(1, 3)
    print(f"{player3.name} is {player3.age} years old - {player3.membership}")