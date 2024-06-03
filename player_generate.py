import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(0)

# Generate data for 100 fictitious players
players = [
    {
        'name': f"Player_{i+1}",
        'main_foot': np.random.choice(['Left', 'Right']),
        'goal_prob': round(np.random.uniform(0.65, 0.95), 2)
    }
    for i in range(100)
]

# Create a DataFrame
df_players = pd.DataFrame(players)

# Display the first few entries to check
print(df_players.head())

# Save to a CSV file if needed
# df_players.to_csv('fictitious_soccer_players.csv', index=False)