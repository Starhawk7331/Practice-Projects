countSingers = int(input("Wie viele Sänger gibt es?"))

VotesSingers = []

for i in range(countSingers):
    print("Wahlen für Sänger", i)
    VotesSingers.append(int(input()))

sum = 0

for i in range(countSingers):
    sum = sum + VotesSingers[i]

VotePerc = []

for i in range(countSingers):
    VotePerc.append(int(100 * VotesSingers[i] / sum))

for i in range(countSingers):
    print("Sänger", i, ":", "*" * VotePerc[i], VotePerc[i], "%\n")
