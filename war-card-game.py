import random
import copy
import time
from collections import Counter
from enum import IntEnum

print("GRA KARCIANA WOJNA")

cards = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
strength = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
Game_type = IntEnum("Game_type", "simulation versus")

player1_life = 26
player2_life = 26

cards_temp = copy.deepcopy(cards)
random.shuffle(cards_temp)

player1 = [ cards_temp.pop()
            for i in range(1, 27)
]

player2 = cards_temp

while True:
    try:
        game_type = int(input("""Wybierz rodzaj gry:
1. Symulacja
2. Gra przeciwko komputerowi
"""))   
        if game_type in range(1, 3):
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie")
            print()
            continue
        break
    except:
        print("Nieprawidłowy wybór. Spróbuj ponownie")
        print()
        continue

if game_type == Game_type.simulation:
    print("Karty pierwszego gracza:", player1, ", życie pierwszego gracza: 26")
    print("Karty drugiego gracza;", player2, ", życie drugiego gracza: 26")
    turn = 1
    war = 1

    while player1_life > 0 and player2_life > 0:
        card1 = player1.pop()
        card2 = player2.pop()
        print()
        print("-------------------------------------------------------------------")
        print("Tura nr:", turn)
        print("Karta pierwszego gracza:", card1)
        print("Karta drugiego gracza:", card2)
        time.sleep(0)
        if strength[card1] > strength[card2]:
            player2_life -= 1
            print()
            print("Pierwszy gracz zabiera kartę")
            print()
            player1_life += 1
            player1.insert(0, card2)
            player1.insert(0, card1)
            print("Karty pierwszego gracza:", player1)
            print()
            print("Karty drugiego gracza;", player2)
            turn += 1
        elif strength[card1] < strength[card2]:
            player1_life -= 1
            print()
            print("Drugi gracz zabiera kartę")
            print()
            player2_life += 1
            player2.insert(0, card1)
            player2.insert(0, card2)
            print("Karty pierwszego gracza:", player1)
            print()
            print("Karty drugiego gracza;", player2)
            turn += 1
        else: #WOJNA
            print()
            print("WOJNA NR", war)
            print()
            lifes = 1
            player1_war_cards = [card1]
            player2_war_cards = [card2]
            player1_cards = player1_life - 1
            player2_cards = player2_life - 1
            while card1 == card2:
                lifes += 1
                if player1_cards == 0 or player2_cards == 0:
                    break
                else:
                    card1 = player1.pop()
                    card2 = player2.pop()
                    print("Karta wojenna pierwszego gracza:", card1)
                    print("Karta wojenna drugiego gracza:", card2)
                    player1_war_cards.append(card1)
                    player2_war_cards.append(card2)
                    if strength[card1] > strength[card2]:
                        player2_life -= lifes
                        player1_life += lifes
                        print("Pierwszy gracz wygrał wojnę!")
                        print()
                        for cards in player2_war_cards:
                            player1.insert(0, cards)
                        for cards in player1_war_cards:
                            player1.insert(0, cards)
                        print("Karty pierwszego gracza:", player1)
                        print()
                        print("Karty drugiego gracza;", player2)
                    elif strength[card1] < strength[card2]:
                        player1_life -= lifes
                        player2_life += lifes
                        print("Drugi gracz wygrał wojnę!")
                        print()
                        for cards in player1_war_cards:
                            player2.insert(0, cards)
                        for cards in player2_war_cards:
                            player2.insert(0, cards)
                        print("Karty pierwszego gracza:", player1)
                        print()
                        print("Karty drugiego gracza;", player2)
                    else:
                        print()
                        print("ZNOWU WOJNA!")
                        player1_cards -= 1
                        player2_cards -= 1
                        continue
                turn += 1
                war += 1
            if player1_cards == 0 or player2_cards == 0:
                break
            else:
                continue
        print()
        print("SUMA kart pierwszego gracza:", player1_life)
        print("Ilości kart gracz pierwszy:",dict(Counter(player1)))
        print()
        print("SUMA kart drugiego gracza:", player2_life)
        print("Ilości kart gracz drugi:",dict(Counter(player2)))

    print()
    print("-------------------------------------------------------------------")
    if player1_life > player2_life:
        print("Koniec gry! Po", turn - 1, "turach wygrał gracz nr 1")
    else:
        print("Koniec gry! Po", turn - 1, "turach wygrał gracz nr 2")

elif game_type == Game_type.versus:
    turn = 1
    war = 1
    print()
    print("Talia 52 kart została potasowana. Każdy gracz otrzymuje po 26 kart.")
    print("Celem gry jest zabranie wszystkich kart przeciwnikowi")
    while player1_life > 0 and player2_life > 0:
        card1 = player1.pop()
        card2 = player2.pop()
        print()
        print("-------------------------------------------------------------------")
        print("Tura nr:", turn)
        move = input("Kliknij ENTER aby odsłonić kartę")
        print("Twoja karta:", card1)
        time.sleep(1)
        print("Karta komputera:", card2)
        time.sleep(1.5)
        if strength[card1] > strength[card2]:
            player2_life -= 1
            print()
            print("Twoja karta ma większą wartość.")
            move = input("Kliknij ENTER aby zabrać kartę")
            player1_life += 1
            player1.insert(0, card2)
            player1.insert(0, card1)
            turn += 1
        elif strength[card1] < strength[card2]:
            player1_life -= 1
            print()
            print("Karta komputera ma większą wartość. Komputer zabiera kartę...")
            time.sleep(2)
            player2_life += 1
            player2.insert(0, card1)
            player2.insert(0, card2)
            turn += 1
        else: #WOJNA
            print()
            print("WOJNA NR", war)
            print()
            lifes = 1
            player1_war_cards = [card1]
            player2_war_cards = [card2]
            player1_cards = player1_life - 1
            player2_cards = player2_life - 1
            while card1 == card2:
                lifes += 1
                if player1_cards == 0 or player2_cards == 0:
                    break
                else:
                    card1 = player1.pop()
                    card2 = player2.pop()
                    move = input("Kliknij ENTER aby odsłonić kartę wojenną")
                    print("Twoja karta wojenna:", card1)
                    time.sleep(1)
                    print("Karta wojenna komputera:", card2)
                    player1_war_cards.append(card1)
                    player2_war_cards.append(card2)
                    time.sleep(1.5)
                    print()
                    if strength[card1] > strength[card2]:
                        player2_life -= lifes
                        player1_life += lifes
                        print("Wygrałeś wojnę!")
                        move = input("Kliknij ENTER aby zabrać karty")
                        print()
                        for cards in player2_war_cards:
                            player1.insert(0, cards)
                        for cards in player1_war_cards:
                            player1.insert(0, cards)
                    elif strength[card1] < strength[card2]:
                        player1_life -= lifes
                        player2_life += lifes
                        print("Komputer wygrał wojnę!")
                        print("Komputer zabiera karty...")
                        time.sleep(2)
                        for cards in player1_war_cards:
                            player2.insert(0, cards)
                        for cards in player2_war_cards:
                            player2.insert(0, cards)
                    else:
                        print()
                        print("ZNOWU WOJNA!")
                        time.sleep(2)
                        player1_cards -= 1
                        player2_cards -= 1
                        continue
                turn += 1
                war += 1
            if player1_cards == 0 or player2_cards == 0:
                break
            else:
                continue

        print()
        print("SUMA kart gracza:", player1_life)
        print("SUMA kart komputera:", player2_life)
        time.sleep(1)

    print()
    print("-------------------------------------------------------------------")
    if player1_life > player2_life:
        print("Koniec gry! Po", turn - 1, "turach wygrał gracz nr 1")
    else:
        print("Koniec gry! Po", turn - 1, "turach wygrał komputer")

