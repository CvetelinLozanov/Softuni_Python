from project.controller import Controller

c = Controller()
print(c.add_aquarium("FreshwaterAquarium", "aquafresh"))
print(c.add_aquarium("SaltwaterAquarium", "aquasalt"))
print(c.add_decoration("Ornament"))
print(c.add_decoration("Ornament"))
print(c.add_decoration("Ornament"))
print(c.add_decoration("Ornament11"))
print(c.add_decoration("Plant"))
print(c.add_decoration("Plant"))
print(c.add_decoration("Plant22"))
print(c.insert_decoration("aquafresh", "Plant"))
print(c.insert_decoration("aquasalt", "Ornament"))
print(c.insert_decoration("aquasalt", "Ornament"))
[print(a.decorations) for a in c.aquariums]
print(len(c.decorations_repository.decorations))
print(c.insert_decoration("aquafresh", "Plantaaa"))
print(c.add_fish("aquafresh", "dsada", "mech", "shark", 1000))
print(c.add_fish("aquafresh", "SaltwaterFish", "mech", "shark", 1000))
print(c.add_fish("aquasalt", "FreshwaterFish", "mech", "shark", 1000))

print(c.add_fish("aquafresh", "FreshwaterFish", "mech", "shark", 1000))
print(c.add_fish("aquafresh", "FreshwaterFish", "mech1", "shark", 1000))
print(c.add_fish("aquasalt", "SaltwaterFish", "kit", "whale", 10000))
print(c.add_fish("aquasalt", "SaltwaterFish", "sin_kit", "whale", 10000))
[print(f.size) for a in c.aquariums for f in a.fish]
print(c.feed_fish("aquafresh"))
[print(f.size) for a in c.aquariums for f in a.fish]
print(c.feed_fish("aquasalt"))
[print(f.size) for a in c.aquariums for f in a.fish]
print(c.calculate_value("aquafresh"))
print(c.calculate_value("aquasalt"))
print(c.report())
