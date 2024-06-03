import pandas as pd
import numpy as np

# Example data
df_players = pd.read_csv('players.csv')
# Now generate penalty kicks using these players
num_kicks = 10000  # Number of penalty kicks to simulate
kicks = []

for _ in range(num_kicks):
    player = np.random.choice(df_players.index)
    if df_players.loc[player, 'main_foot'] == 'Right':
        direction = np.random.choice([1, 4, 7, 8])  # Penalty shoot direction from 1, 3, 7, 9
    else:
        direction = np.random.choice([2, 3, 5, 6, 9])  
    if direction in [1, 3, 7, 9]:
        modified_prob = min(df_players.loc[player, 'goal_prob'] + 0.15, 1)  # Increase goal prob by 15%, cap at 100%
    else:
        modified_prob = df_players.loc[player, 'goal_prob']

    result = 'Goal' if np.random.rand() < modified_prob else 'Missed'
    
    kicks.append({
        'Player Name': df_players.loc[player, 'name'],
        'Main Foot': df_players.loc[player, 'main_foot'],
        'Penalty Shoot Direction': direction,
        'Result of Penalty Shoots': result
    })

# Create DataFrame for penalty kicks
df_kicks = pd.DataFrame(kicks)

# Display the first few entries to check
print("\nPenalty Kicks Dataset Preview:")
print(df_kicks.head())

# Save both datasets to CSV files if needed
# df_kicks.to_csv('penalty_kicks_dataset.csv', index=False)