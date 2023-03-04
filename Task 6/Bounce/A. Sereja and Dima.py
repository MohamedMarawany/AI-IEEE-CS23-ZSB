n = int(input("Enter numbe of cards: "))
a = list(map(int, input("Enter Number on cards: ").strip().split()))[:n]

sereja_score = 0
dima_score = 0
leftmost = 0
rightmost = n - 1
is_sereja_turn = True

while leftmost <= rightmost:
    if is_sereja_turn:
        if a[leftmost] > a[rightmost]:
            sereja_score += a[leftmost]
            leftmost += 1
        else:
            sereja_score += a[rightmost]
            rightmost -= 1
    else:
        if a[leftmost] > a[rightmost]:
            dima_score += a[leftmost]
            leftmost += 1
        else:
            dima_score += a[rightmost]
            rightmost -= 1
    is_sereja_turn = not is_sereja_turn

print(sereja_score)
print(dima_score)

"""while leftmost <= rightmost:
    if is_sereja_turn:
        if a[leftmost] > a[rightmost]:
            sereja_score += a[leftmost]
            leftmost += 1
        else:
            sereja_score += a[rightmost]
            rightmost -= 1
    else:
        if a[leftmost] > a[rightmost]:
            dima_score += a[leftmost]
            leftmost += 1
        else:
            dima_score += a[rightmost]
            rightmost -= 1
    is_sereja_turn = not is_sereja_turn

print(sereja_score)
print(dima_score)"""
