# Prints Leaf & Sprout's watering list with your code from plants.py, so you can see it at work. Ready to use.
# Run it with: python care_today.py
from datetime import date

from plants import CareLog, Cactus, Plant, plants_to_water

today = date(2026, 5, 10)
fern = Plant("Fern", 3, date(2026, 5, 7))
plants = [
    fern,
    Plant("Pothos", 7, date(2026, 5, 1)),
    Plant("Snake Plant", 14, date(2026, 5, 1)),
    Cactus("Barrel Cactus", date(2026, 4, 20)),
]

print("Leaf & Sprout: your plants on", today)
for plant in plants:
    print(plant)
print()
print("Water today:", plants_to_water(plants, today))

fern_log = CareLog("Fern", notes="likes the bathroom")
fern.water(today)
fern_log.record(today)
print()
print("After watering the fern:")
print(fern)
print(fern_log)

january = date(2026, 1, 20)
bunny = Cactus("Bunny Ears", date(2026, 1, 1))
print()
print("Does a cactus watered on January 1 need water on January 20?", bunny.needs_water(january))
