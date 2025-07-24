import queue

# Priority Queue (öncelik sayısı küçük olan önce çıkar)
pq = queue.PriorityQueue()

pq.put((2, "Algoritmalar"))
pq.put((1, "Veri yapıları"))
pq.put((3, "Ağ programlama"))

print("Öncelik sırasına göre elemanlar:")
while not pq.empty():
    priority, task = pq.get()
    print(f"Öncelik: {priority}, Görev: {task}")
