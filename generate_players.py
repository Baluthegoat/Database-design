import random
import json

heros = []
for i in range(1000):
    hero = {
        "id": i + 1,
        "name": f"Heros {i + 1}",
        "level":{
            "introduction(the prophecy)": random.randint(100, 1000),
            "cinematic(thrall's vision)": random.randint(100, 1000),
            "chapter one(chasing vision)": random.randint(100, 1000),
            "chapter two(departures)": random.randint(100, 1000),
            "chapter three(riders on the storm)": random.randint(100, 1000),
            "chapter four(the fires down below)": random.randint(100, 1000),
            "chapter five(countdown to extinction)": random.randint(100, 1000),
        },
        "health point": random.randint(100, 1000),
        "level": random.randint(1, 10),
        "abilities":{
            "brilliance aura": random.randint(1, 100),
            "siphon mana": random.randint(1, 100),
            "phoenix": random.randint(1, 100),
            "inner fire": random.randint(1, 100),
            "fan of knives": random.randint(1, 100),
        }
    }
    heros.append(hero)
data = {"heros": heros}
file_path = "heros_data.json"

# Write data to JSON file
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=2)

print(f"JSON file '{file_path}' created successfully!")
