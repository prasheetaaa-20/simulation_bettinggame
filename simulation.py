import random

def play_round():
    deck=[]
    for rank in range(13):
     for cnt in range(4):
      deck.append(rank)

    random.shuffle(deck)
    joker = deck.pop()
    for i, card in enumerate(deck):
        if card == joker:
            return "Bahar" if i % 2 == 0 else "Andar"

def simulate(n=1000000):
    results = {"Andar": 0, "Bahar": 0}
    for cnt in range(n):
        results[play_round()] += 1
    return results

if __name__ == "__main__":
    n = 1000000
    res = simulate(n)
    for side, wins in res.items():
        print(f"{side}: {wins / n:.4f}")
