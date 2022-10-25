
n = int(input())
a_cards = list(map(int, input().split()))
alice = []
bob = []
while True:
    card = max(a_cards)
    alice.append(card)
    a_cards.remove(card)
    if len(a_cards) == 0:
        break
    card = max(a_cards)
    bob.append(card)
    a_cards.remove(card)
    if len(a_cards) == 0:
        break
print(sum(alice) - sum(bob))

# recommend
# alice = a_cards[0::2]
# bob = a_cards[1::2]
