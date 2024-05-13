# import random
# import json

# heros = []
# for i in range(20000):
#     hero = {
#         "id": i + 1,
#         "name": f"Heros {i + 1}",
#         "level":{
#             "introduction(the prophecy)": random.randint(100, 20000),
#             "cinematic(thrall's vision)": random.randint(100, 20000),
#             "chapter one(chasing vision)": random.randint(100, 20000),
#             "chapter two(departures)": random.randint(100, 20000),
#             "chapter three(riders on the storm)": random.randint(100, 20000),
#             "chapter four(the fires down below)": random.randint(100, 20000),
#             "chapter five(countdown to extinction)": random.randint(100, 20000),
#         },
#         "health point": random.randint(100, 20000),
#         "level": random.randint(1, 10),
#         "abilities":{
#             "brilliance aura": random.randint(1, 100),
#             "siphon mana": random.randint(1, 100),
#             "phoenix": random.randint(1, 100),
#             "inner fire": random.randint(1, 100),
#             "fan of knives": random.randint(1, 100),
#         }
#     }
#     heros.append(hero)
# data = {"heros": heros}
# file_path = "heros_data.json"

# # Write data to JSON file
# with open(file_path, "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file '{file_path}' created successfully!")

# import random
# import json
# import datetime

# # Start from 1 for session IDs
# start_id = 1

# sessions = []
# for i in range(20001):  # Generating sessions up to 1000
#     # Simulating random start time within the last 30 days
#     start_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30), hours=random.randint(1, 24))
    
#     # Simulating duration between 20 to 30 hours
#     duration_hours = random.randint(20, 30)
#     end_time = start_time + datetime.timedelta(hours=duration_hours)
    
#     winner = random.choice(["Alliance", "Horde", "Neutral"])  # Selecting a random winner faction

#     # Creating session data
#     session = {
#         "session_id": i,
#         "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),  # Formatting start time
#         "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),  # Formatting end time
#         "duration_hours": duration_hours,
#         "winner": winner
#     }
#     sessions.append(session)

# # Attempting to load existing session data from file
# try:
#     with open("game_sessions.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"sessions": []}

# # Appending new session data to existing data or creating new data if file not found
# data["sessions"].extend(sessions)

# # Writing data back to JSON file
# with open("game_sessions.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'game_sessions.json' updated successfully!")

# import random
# import json

# # Function to generate random faction data
# def generate_faction_data(num_factions):
#     factions = []

#     for i in range(1, num_factions + 1):
#         faction = {
#             "faction_id": i,
#             "name": f"Faction {i}",
#             "base_location": f"Location {i}",  # Random base location
#             "player_id": i  # Foreign key linking to player ID
#         }
#         factions.append(faction)

#     return factions

# # Specify the number of factions you want to generate
# num_factions = 20000  # Change this number as per your requirement

# # Generate faction data
# factions = generate_faction_data(num_factions)

# # Attempting to load existing player data from file
# try:
#     with open("faction_data.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"factions": []}

# # Appending new faction data to existing data or creating new data if file not found
# data["factions"].extend(factions)

# # Writing data back to JSON file
# with open("faction_data.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'faction_data.json' updated successfully!")

# import random
# import json

# # Function to generate random building data
# def generate_building_data(num_buildings):
#     buildings = []

#     for i in range(1, num_buildings + 1):
#         building = {
#             "building_id": i,
#             "name": f"Building {i}",
#             "damage": random.randint(10, 100),
#             "hp": random.randint(500, 2000),
#             "type": random.choice(["Town Hall", "Barracks", "Tower", "Farm"]),  # Sample types, adjust as needed
#             "base_id": random.randint(1, 20000)  # Foreign key linking to base ID
#         }
#         buildings.append(building)

#     return buildings

# # Specify the number of buildings you want to generate
# num_buildings = 20000 # Change this number as per your requirement

# # Generate building data
# buildings = generate_building_data(num_buildings)

# # Attempting to load existing building data from file
# try:
#     with open("building_data.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"buildings": []}

# # Appending new building data to existing data or creating new data if file not found
# data["buildings"].extend(buildings)

# # Writing data back to JSON file
# with open("building_data.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'building_data.json' updated successfully!")

# import random
# import json

# # Function to generate random reward data
# def generate_reward_data(num_rewards):
#     rewards = []

#     for i in range(1, num_rewards + 1):
#         reward = {
#             "ID": i,
#             "name": f"Reward {i}",
#             "type": random.choice(["Gold", "Gem", "Item"]),  # Sample types, adjust as needed
#             "quantity": random.randint(1, 1000)
#         }
#         rewards.append(reward)

#     return rewards

# # Specify the number of rewards you want to generate
# num_rewards = 1000  # Change this number as per your requirement

# # Generate reward data
# rewards = generate_reward_data(num_rewards)

# # Attempting to load existing reward data from file
# try:
#     with open("rewards.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"rewards": []}

# # Appending new reward data to existing data or creating new data if file not found
# data["rewards"].extend(rewards)

# # Writing data back to JSON file
# with open("rewards.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'rewards.json' updated successfully!")

# import random
# import json

# # Function to generate random reward data
# def generate_reward_data(num_rewards, session_id):
#     rewards = []

#     for i in range(1, num_rewards + 1):
#         reward = {
#             "reward_id": i,
#             "name": f"Reward {i}",
#             "type": random.choice(["Gold", "Gem", "Item"]),
#             "quantity": random.randint(1, 20000),
#             "session_id": session_id  # Assigning the session_id as the foreign key
#         }
#         rewards.append(reward)

#     return rewards

# # Specify the number of rewards you want to generate
# num_rewards = 20000  # Change this number as per your requirement
# session_id = 1  # Assuming a single session with session_id = 1, change as needed

# # Generate reward data
# rewards = generate_reward_data(num_rewards, session_id)

# # Attempting to load existing reward data from file
# try:
#     with open("rewards.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"rewards": []}

# # Appending new reward data to existing data or creating new data if file not found
# data["rewards"].extend(rewards)

# # Writing data back to JSON file
# with open("rewards.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'rewards.json' updated successfully!")

# import random
# import json

# # Function to generate random objective data
# def generate_objective_data(num_objectives, num_acts):
#     objectives = []

#     objective_descriptions = [
#         "Secure the passage through the Dark Forest.",
#         "Defend the outpost against the Undead assault.",
#         "Gather resources to strengthen your army.",
#         "Rescue the captured villagers from the Orc encampment.",
#         "Destroy the enemy's stronghold to claim victory.",
#         "Escort the caravan safely to the Goblin Merchant.",
#         "Uncover the secrets hidden within the haunted ruins.",
#         "Defeat the powerful demon lord threatening the realm.",
#         "Discover the ancient artifacts scattered across the land.",
#         "Survive the night onslaught of the undead hordes.",
#     ]

#     for i in range(1, num_objectives + 1):
#         # Assign both act_id and objective_id to the current value of i
#         objective = {
#             "objective_id": i,
#             "name": f"Objective {i}",
#             "description": random.choice(objective_descriptions),
#             "act_id": i
#         }
#         objectives.append(objective)

#     return objectives

# # Specify the number of objectives and acts you want to generate
# num_objectives = 20000  # Change this number as per your requirement
# num_acts = 20000  # Start from act_id 1

# # Generate objective data
# objectives = generate_objective_data(num_objectives, num_acts)

# # Attempting to load existing objective data from file
# try:
#     with open("objective_data.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"objectives": []}

# # Appending new objective data to existing data or creating new data if file not found
# data["objectives"].extend(objectives)

# # Writing data back to JSON file
# with open("objective_data.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'objective_data.json' updated successfully!")

# import random
# import json

# # Function to generate random base data
# def generate_base_data(num_bases, num_players):
#     bases = []

#     locations = ["Forest", "Mountain", "Plains", "Desert", "Coast"]
#     resources = ["Gold", "Wood", "Stone", "Food"]

#     for i in range(1, num_bases + 1):
#         base = {
#             "base_id": i,
#             "location": random.choice(locations),
#             "resources": {res: random.randint(100, 1000) for res in resources},  # Random resources
#             "player_id":  random.randint(1, num_players)
#         }
#         bases.append(base)

#     return bases

# # Specify the number of bases and players you want to generate
# num_bases = 20000  # Change this number as per your requirement
# num_players = 20000  # Change this number as per your requirement

# # Generate base data
# bases = generate_base_data(num_bases, num_players)

# # Attempting to load existing base data from file
# try:
#     with open("base.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"bases": []}

# # Appending new base data to existing data or creating new data if file not found
# data["bases"].extend(bases)

# # Writing data back to JSON file
# with open("base.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'base.json' updated successfully!")

# import random
# import json

# # Function to generate random item data
# def generate_item_data(num_items, num_players):
#     items = []

#     item_types = ["Weapon", "Armor", "Potion", "Scroll", "Artifact"]
#     rarities = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]

#     for i in range(1, num_items + 1):
#         item = {
#             "item_id": i,
#             "name": f"Item {i}",
#             "type": random.choice(item_types),
#             "effects": generate_item_effects(),  # Generate random effects
#             "rarity": random.choice(rarities),
#             "player_id": random.randint(1, num_players)  # Foreign key linking to player ID
#         }
#         items.append(item)

#     return items

# # Function to generate random item effects
# def generate_item_effects():
#     # List of possible effects
#     effects_list = [
#         "Increase attack damage by 10%",
#         "Restore 50 health points",
#         "Grant invisibility for 30 seconds",
#         "Summon a powerful ally to aid in battle",
#         "Inflict poison on the target for 5 turns",
#         "Grant temporary immunity to status effects",
#         "Double experience gain for the next battle",
#         "Teleport to a random location on the map",
#         "Create a protective shield around the player",
#         "Increase movement speed by 50%"
#     ]
#     # Randomly select and return effects
#     return random.sample(effects_list, random.randint(1, 3))  # Randomly select up to 3 effects

# # Specify the number of items and players you want to generate
# num_items = 20000  # Change this number as per your requirement
# num_players = 20000  # Change this number as per your requirement

# # Generate item data
# items = generate_item_data(num_items, num_players)

# # Attempting to load existing item data from file
# try:
#     with open("item.json", "r") as json_file:
#         data = json.load(json_file)
# except FileNotFoundError:
#     data = {"items": []}

# # Appending new item data to existing data or creating new data if file not found
# data["items"].extend(items)

# # Writing data back to JSON file
# with open("item.json", "w") as json_file:
#     json.dump(data, json_file, indent=2)

# print(f"JSON file 'item.json' updated successfully!")

import random
import json

# Function to generate random unit data
def generate_unit_data(num_units, num_players):
    units = []

    unit_types = ["Footman", "Archer", "Knight", "Mage", "Gryphon Rider"]
    max_hp_values = {"Footman": 100, "Archer": 80, "Knight": 150, "Mage": 70, "Gryphon Rider": 120}
    max_damage_values = {"Footman": 20, "Archer": 30, "Knight": 40, "Mage": 50, "Gryphon Rider": 60}

    for i in range(1, num_units + 1):
        unit_type = random.choice(unit_types)
        unit = {
            "unit_id": i,
            "name": f"{unit_type} {i}",
            "type": unit_type,
            "hp": random.randint(1, max_hp_values[unit_type]),
            "damage": random.randint(1, max_damage_values[unit_type]),
            "player_id": random.randint(1, num_players)  # Foreign key linking to player ID
        }
        units.append(unit)

    return units

# Specify the number of units and players you want to generate
num_units = 20000  # Change this number as per your requirement
num_players = 20000  # Change this number as per your requirement

# Generate unit data
units = generate_unit_data(num_units, num_players)

# Attempting to load existing unit data from file
try:
    with open("unit.json", "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {"units": []}

# Appending new unit data to existing data or creating new data if file not found
data["units"].extend(units)

# Writing data back to JSON file
with open("unit.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

print(f"JSON file 'unit.json' updated successfully!")