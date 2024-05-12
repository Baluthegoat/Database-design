# import random
# import json

# players = []
# for i in range(10000):
#     player = {
#         "id": i + 1,
#         "name": f"Player {i + 1}",
#         "resource":{
#             "gold": random.randint(100, 1000),
#             "wood": random.randint(100, 1000),
#             "stone": random.randint(100, 1000),
#             "food": random.randint(100, 1000),
#         },
#         "experience": random.randint(100, 1000),
#         "level": random.randint(1, 10),
#         "base_location":{
#             "x": random.randint(1, 100),
#             "y": random.randint(1, 100),
#         }
#     }
#     players.append(player)
# data = {"players": players}
# file_path = "players_data.json"

# # Write data to JSON file
# with open(file_path, "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file '{file_path}' created successfully!")
import random
import json

# Start from 125 as per your requirement
start_id = 501

players = []
for i in range(start_id, 1001):  # 501 is exclusive, so it will generate up to 500
    player = {
        "id": i,
        "name": f"Player {i}",
        "resource":{
            "gold": random.randint(100, 1000),
            "wood": random.randint(100, 1000),
            "stone": random.randint(100, 1000),
            "food": random.randint(100, 1000),
        },
        "experience": random.randint(100, 1000),
        "level": random.randint(1, 10),
        "base_location":{
            "x": random.randint(1, 100),
            "y": random.randint(1, 100),
        }
    }
    players.append(player)

# Load existing data
with open("players_data.json", "r") as json_file:
    data = json.load(json_file)

# Append new players to existing data
data["players"].extend(players)

# Write data back to JSON file
with open("players_data.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

print(f"JSON file 'players_data.json' updated successfully!")