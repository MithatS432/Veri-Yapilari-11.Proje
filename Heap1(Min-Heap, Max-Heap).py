import heapq

# Min-Heap örneği
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

print("Min-Heap olarak sıralı çıkış:")
while min_heap:
    print(heapq.heappop(min_heap), end=' ')  # Küçükten büyüğe çıkar

print("\n")

# Max-Heap için Python'da değerlerin negatifini kullanıyoruz
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)

print("Max-Heap olarak sıralı çıkış:")
while max_heap:
    print(-heapq.heappop(max_heap), end=' ')  # Büyükten küçüğe çıkar
