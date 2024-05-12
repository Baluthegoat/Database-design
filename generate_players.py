# import random
# import json

# heros = []
# for i in range(10000):
#     heros = {
#         "id": i + 1,
#         "name": f"Heros {i + 1}",
#         "level":{
#             "introduction(the prophecy)": random.randint(100, 1000),
#             "cinematic(thrall's vision)": random.randint(100, 1000),
#             "chapter one(chasing vision)": random.randint(100, 1000),
#             "chapter two(departures)": random.randint(100, 1000),
#             "chapter three(riders on the storm)": random.randint(100, 1000),
#             "chapter four(the fires down below)": random.randint(100, 1000),
#             "chapter five(countdown to extinction)": random.randint(100, 1000),
#         },
#         "health point": random.randint(100, 1000),
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

import random
import json
import datetime

# Start from 1 for session IDs
start_id = 1

sessions = []
for i in range(start_id, 1001):  # Generating sessions up to 1000
    # Simulating random start time within the last 30 days
    start_time = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30), hours=random.randint(1, 24))
    
    # Simulating duration between 20 to 30 hours
    duration_hours = random.randint(20, 30)
    end_time = start_time + datetime.timedelta(hours=duration_hours)
    
    winner = random.choice(["Alliance", "Horde", "Neutral"])  # Selecting a random winner faction

    # Creating session data
    session = {
        "session_id": i,
        "start_time": start_time.strftime("%Y-%m-%d %H:%M:%S"),  # Formatting start time
        "end_time": end_time.strftime("%Y-%m-%d %H:%M:%S"),  # Formatting end time
        "duration_hours": duration_hours,
        "winner": winner
    }
    sessions.append(session)

# Attempting to load existing session data from file
try:
    with open("game_sessions.json", "r") as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    data = {"sessions": []}

# Appending new session data to existing data or creating new data if file not found
data["sessions"].extend(sessions)

# Writing data back to JSON file
with open("game_sessions.json", "w") as json_file:
    json.dump(data, json_file, indent=2)

print(f"JSON file 'game_sessions.json' updated successfully!")