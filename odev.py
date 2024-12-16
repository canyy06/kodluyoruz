import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Noktaların tanımlanması
points = [
    (1, 2),
    (4, 6),
    (5, 3),
    (7, 8),
    (2, 5)
]

# Mesafeleri hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Her çift sadece bir kez ele alınır
        distance = euclideanDistance(points[i], points[j])
        distances.append((points[i], points[j], distance))

# Minimum mesafeyi bulma
min_distance = min(distances, key=lambda x: x[2])

# Sonuçları yazdırma
print("Noktalar arasındaki mesafeler:")
for p1, p2, dist in distances:
    print(f"{p1} ve {p2} arasındaki mesafe: {dist:.2f}")

print(f"\nMinimum mesafe: {min_distance[2]:.2f}")
print(f"Bu mesafe {min_distance[0]} ve {min_distance[1]} noktaları arasındadır.")
