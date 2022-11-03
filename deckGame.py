import random


def show_Decks():
    print('Este é o deck do jogador: \n ' + str(player)) 
    print('Este é o deck do oponente: \n ' + str(other )) 

def shuffle():
    random.shuffle(player)
    random.shuffle(other)

def show_shuff():
    print('The player last two cards are :\n' + str(player[12]) + ' ' + str(player[13]))
    print('The player last two cards are :\n' + str(other[12]) + ' ' + str(other[13]))

def convert_to_int(card):
    if card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14
    else:
        return int(card)

def sum(deck):
    sumTotal = 0
    for card in deck:
        sumTotal += convert_to_int(card)
    return sumTotal

def compare(deck1, deck2):
    sumPlayer = sum(deck1)
    sumNPC = sum(deck2)

    print('A soma da soma dos valores das duas ultimas cartas do jogador é : \n ' + str(sumPlayer))
    print('A soma da soma dos valores das duas ultimas cartas do adversário é : \n ' + str(sumNPC))

    if (sumPlayer > sumNPC):
        print(' O jogador ganhou! ')
    else:
        (sumPlayer < sumNPC)
        print(' O jogador perdeu! ')








def descartar():
    descart = input(' Quantas cartas pretende discaratar: \n ')
    if descart == ('0'):
        return
    elif descart == ('1'):
        descart1()
    elif descart == ('2'):
        descart2()



def descart1():
    random.shuffle(newcard)
    print('A nova carta é: ' + (newcard))



def descart2():
    random.shuffle(deck1)
    print('A nova carta é: ' + (newcard))



 

player = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
other = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
newcard = (player[12])


show_Decks()
shuffle()
show_shuff()


deck1 = (player[12], player[13])
deck2 = (other[12], other[13])

compare(deck1, deck2)
