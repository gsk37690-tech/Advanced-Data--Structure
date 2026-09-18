def min_eating_speed(piles,h):
    left = 1
    right = max(piles)
    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for i in piles:
            hours += ( i + mid - 1 ) // mid
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1
    return left
piles = list(map(int,input().split()))
h = int(input())
print("Monkey Eates",min_eating_speed(piles,h),"per hour to complete the pile in ",h," hours.")
