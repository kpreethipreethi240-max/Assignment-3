n = int(input("Enter number of cities: "))
m = int(input("Enter number of flights: "))

flights = []

print("Enter flight details (from, to, price):")
for i in range(m):
    u, v, price = map(int, input().split())
    flights.append([u, v, price])

src = int(input("Enter source city: "))
dst = int(input("Enter destination city: "))
k = int(input("Enter maximum stops: "))

INF = float('inf')

dist = [INF] * n
dist[src] = 0

for i in range(k + 1):
    temp = dist.copy()

    for u, v, price in flights:
        if dist[u] != INF:
            temp[v] = min(temp[v], dist[u] + price)

    dist = temp

if dist[dst] == INF:
    print("Cheapest price: -1")
else:
    print("Cheapest price:", dist[dst])