# -*- coding: UTF-8 -*-
import random
import time

# 红桃，梅花，方片，黑桃
cardType = ("Heart  ", "Plum   ", "Diamond", "Spade  ")
cardNum = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")


def generatecards():
    cardPairs = []  # 牌存放列表
    # 两层嵌套循环，生成52张花色牌
    for type in cardType:
        for num in cardNum:
            cardPairs.append((type, num))

    # 添加大小王
    cardPairs.append(("Joker  ", "Red"))  # 大王
    cardPairs.append(("Joker  ", "Black"))  # 小王

    return cardPairs


def dispatchcards(cardPairs):
    # 洗牌 - 可以调用多次洗多次
    random.shuffle(cardPairs)
    random.shuffle(cardPairs)
    # 玩家手牌列表
    player1Cards = []
    player2Cards = []
    player3Cards = []
    coverCardNum = 3  # 底牌数
    print(cardPairs)
    for index in range(0, len(cardPairs) - coverCardNum):
        cardPair = cardPairs[index]
        if index % 3 == 0:  # 玩家1
            print(index)
            player1Cards.append(cardPair)
            print()  # 输出换行
        elif index % 3 == 1:  # 玩家2
            player2Cards.append(cardPair)
        else:  # 玩家3
            player3Cards.append(cardPair)

        print(' '.join(cardPair), end='\t')  # 输出当前发出的牌，模拟发牌效果)
        time.sleep(0.1)  # 每发一张牌停顿一下，便于展示
    print('\n')

    print("玩家1 手牌:", len(player1Cards))
    for cardPair in player1Cards:
        print(' '.join(cardPair))
    print()

    print("玩家2 手牌:", len(player2Cards))
    for cardPair in player2Cards:
        print(' '.join(cardPair))
    print()

    print("玩家3 手牌:", len(player3Cards))
    for cardPair in player3Cards:
        print(' '.join(cardPair))
    print()

    print("底牌:")
    rest_cards = cardPairs[-3:]  # 剩余3张底牌
    for card in rest_cards:
        print(' '.join(card))


# 生成牌
cardPairs = generatecards()
# 分配牌
dispatchcards(cardPairs)