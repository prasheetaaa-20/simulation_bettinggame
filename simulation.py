import random

def play_round():
    deck=[]
    for rank in range(13):
     for cnt in range(4):
      deck.append(rank) #created the deck

    random.shuffle(deck)
    joker = deck.pop() #shuffled and picked a card
    for i, card in enumerate(deck):
        if card == joker:
            return "Bahar" if i % 2 == 0 else "Andar" #bahar is always dealt first (modulo helps deal the card into either bahar/andar)

def simulate(n=1000000): #simulating a million times
    results = {"Andar": 0, "Bahar": 0}
    for cnt in range(n):
        results[play_round()] += 1 #counter for winning pile
    return results

res = simulate(1000000)
print(f"Andar: {res['Andar'] / 1000000:.5f}") #displays result 
print(f"Bahar: {res['Bahar'] / 1000000:.5f}")
