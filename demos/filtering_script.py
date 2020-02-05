filter_categories = {
    'water': ['drink', 'water','contamination', 'thirst', 'thirsty', 'to drink', 'hydrate'],
    'financial': ['Money', 'money', 'stocks', 'GDP', 'business', 'economy'],
    'health': ['injured', 'medical', 'death', 'casualitiy', 'hospital', 'accident', 'victims', 'casualities'],
    'building': ['houses','structure','structure', 'buildings','building', 'apartments', 'apartment'],
    'power': ['electricity', 'electric', 'power', 'utility', 'lights'],
    'transportation':[' road ',' roads ', ' bus ', ' car ', ' uber ', ' highway ', ' hwy ', ' traffic ', ' tollway ']
}

import pandas as pd


df = pd.read_csv('data/twitter/tweets.csv')
df['text'] = df['text'].str.lower()
df['category'] = False


filter_water = df['text'].str.contains('|'.join(filter_categories['water']), na=False)
filter_financial = df['text'].str.contains('|'.join(filter_categories['financial']), na=False)
filter_health = df['text'].str.contains('|'.join(filter_categories['health']), na=False)
filter_building = df['text'].str.contains('|'.join(filter_categories['building']), na=False)
filter_power = df['text'].str.contains('|'.join(filter_categories['power']), na=False)
filter_transportation = df['text'].str.contains('|'.join(filter_categories['transportation']), na=False)

df.loc[filter_water, 'category'] = 'water'
df.loc[filter_financial, 'category'] = 'financial'
df.loc[filter_health, 'category'] = 'health'
df.loc[filter_building, 'category'] = 'building'
df.loc[filter_power, 'category'] = 'power'
df.loc[filter_transportation, 'category'] = 'transportation'

f = df['category'] != False
df = df[f]
df.to_csv('filtered_tweets.csv')
