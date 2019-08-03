import pandas as pd
import numpy as np

animals = pd.DataFrame(
    data={
        'Animal' : ['Dolphin', 'Whale', 'Dragon', 'Tiger', 'Cat', 'Unicorn', np.nan, 'Ox'],
        'Habitat': ['Ocean', 'Ocean', 'Fantasy', 'Land', np.nan, 'Fantasy', 'Land', 'Land'],
        'AverageWeight': [150, 30000, 10000, 200, 4, np.nan, 120, 600],
        'ChineseZodiacYear': [np.nan, np.nan, '2012-01-01', '2010-01-01', np.nan, np.nan, '1912-01-01', '2009-01-01'],
        'Domesticated': ['No', 'No', 'No', 'No', 'Yes','No', 'No', 'Yes'],
        'MaxLifespan': [45, 200, 4500, 18, 16, 2000, 60, 15],
    }
)

animals_no_nans = pd.DataFrame(
    data={
        'Animal' : ['Dolphin', 'Whale', 'Dragon', 'Tiger', 'Cat', 'Unicorn', 'Ox'],
        'Habitat': ['Ocean', 'Ocean', 'Fantasy', 'Land', 'Land', 'Fantasy', 'Land'],
        'AverageWeight': [150, 30000, 10000, 200, 4, 6746, 600],
        'ChineseZodiacYear': ['2200-01-01', '2200-01-01', '2012-01-01', '2010-01-01', '2200-01-01','2200-01-01', '2009-01-01'],
        'Domesticated': ['No', 'No', 'No', 'No', 'Yes','No', 'Yes'],
        'MaxLifespan': [45, 200, 4500, 18, 16, 2000, 15],
    }
)

test_target_feature = {'MaxLifespan': float}

test_data_features = {
    'Habitat' : str, 
    'AverageWeight' : float,
    'ChineseZodiacYear' : str,
    'Domesticated' : str
}

test_mapping_for_nulls = {
    'Animal' : 'DROP',
    'Habitat': 'Land',
    'AverageWeight': 'MEAN',
    'ChineseZodiacYear': '2200-01-01',
    'Domesticated': 'DROP',
    'MaxLifespan': 'DROP'
}

test_feature_transformations = {
    'Domesticated': {'No': 0, 'Yes': 1},
}

def log_transform_base10(dataset, features):
    dataset[features] = dataset[features].transform(np.log10)
    return dataset

def identify_if_zodiac_animal(dataset, features):
    dataset[features] = pd.to_datetime(dataset[features])
    def identify_zodiac_year(row):
        if row.year == 2200:
            return 0
        else :
            return 1
    dataset[features] = dataset[features].apply(identify_zodiac_year)
    return dataset

test_custom_functions_to_be_run = {
    log_transform_base10 : 'AverageWeight',
    identify_if_zodiac_animal: 'ChineseZodiacYear'
}

test_features_to_be_scaled = [
    'AverageWeight'
]

test_features_to_be_standardized = [
    'AverageWeight'
]

test_features_to_be_renamed = {
    'ChineseZodiacYear' : 'IsAnimalOfTheZodiac'
}

test_features_to_hot_encode = [
    'Habitat'
]
