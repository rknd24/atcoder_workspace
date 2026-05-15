n = int(input())
cards = list(map(int,input().split()))

cards.sort(reverse=True)
Alice_score = 0
Bob_score = 0
for i in range(len(cards)):
    if i % 2 == 0:
        Alice_score += cards[i]
    else:
        Bob_score += cards[i]

score = Alice_score - Bob_score
print(score)


