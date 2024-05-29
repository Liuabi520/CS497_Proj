import pandas as pd
import numpy as np

# Example data
players = [
    {'name': 'Lionel Messi', 'main_foot': 'Left', 'goal_prob': 0.85},
    {'name': 'Cristiano Ronaldo', 'main_foot': 'Right', 'goal_prob': 0.80},
    {'name': 'Neymar Jr', 'main_foot': 'Right', 'goal_prob': 0.78},
    {'name': 'Kylian Mbappe', 'main_foot': 'Right', 'goal_prob': 0.76},
    # Add more players as needed
]

num_entries = 1000  # Total number of penalty kicks in the dataset

# Prepare the lists to populate the dataframe
names = []
main_feet = []
directions = []
results = []

for _ in range(num_entries):
    player = np.random.choice(players, p=[player['goal_prob'] / sum(p['goal_prob'] for p in players) for player in players])
    names.append(player['name'])
    main_feet.append(player['main_foot'])
    directions.append(np.random.randint(1, 10))
    results.append('Goal' if np.random.rand() < player['goal_prob'] else 'Missed')

# Create DataFrame
df = pd.DataFrame({
    'Player Name': names,
    'Main Foot': main_feet,
    'Penalty Shoot Direction': directions,
    'Result of Penalty Shoots': results
})

# Save to CSV file
df.to_csv('penalty_kicks_dataset.csv', index=False)