scores = [45, 102, 12, 56, 8, 120, 75, 99, 4, 62]
print("Batsman scores in 10 matches:", scores)

highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)

centuries = 0
half_centuries = 0
for s in scores:
    if s >= 100:
        centuries += 1
    elif s >= 50 and s <= 99:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)
