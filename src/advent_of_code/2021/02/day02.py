import numpy as np
import pandas as pd

directions = pd.read_csv('input.txt', header=None, delimiter=' ', names=['direction', 'distance'])

forward_distance = directions['distance'][directions['direction'] == 'forward']
horizontal_pos = forward_distance.sum()

up_distance = directions['distance'][directions['direction'] == 'up']
down_distance = directions['distance'][directions['direction'] == 'down']
vertical_pos = down_distance.sum() - up_distance.sum()

print(f'Final horizontal position: {horizontal_pos}')
print(f'Final vertical position: {vertical_pos}')
print(f'Product: {horizontal_pos * vertical_pos}')


# Part II

# convert 'up' 'down' to -/+ 1
directions['up_down'] = 0
directions.loc[directions['direction'] == 'down', 'up_down'] = 1
directions.loc[directions['direction'] == 'up', 'up_down'] = - 1

# calculate aim at every step
directions['aim'] = (directions['up_down'] * directions['distance']).cumsum()

# convert 'forward' to 0/1
directions['forward'] = 0
directions.loc[directions['direction'] == 'forward', 'forward'] = 1

# calculated depth change at every step
directions['depth_change'] = directions['forward'] * directions['distance'] * directions['aim']

# print(directions.head(30))

vertical_pos = directions['depth_change'].sum()
print(f'Final vertical position considering aim: {vertical_pos}')
print(f'Product: {horizontal_pos * vertical_pos}')
