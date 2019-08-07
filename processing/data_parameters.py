from processing.custom_functions import *

## Dictionary with {'FeatureName': type}
target_feature = {'MaxLifespan': float}

## Dictionary with {'FeatureName': type}
data_features = {
    'Habitat' : str,
    'AverageWeight' : float,
    'ChineseZodiacYear' : str,
    'Domesticated' : str
}

# DROP = drop null columns
# String = fill null with string
# ZEROS = fill null with zero
# Callable = function to be run, function should be stored in custom_functions.py
mappings_for_nulls = {
    'Animal' : 'DROP',
    'Habitat': 'Land',
    'AverageWeight': 'MEAN',
    'ChineseZodiacYear': '2200-01-01',
    'Domesticated': 'DROP',
    'MaxLifespan': 'DROP'
}

# Dictionary mapping values, format is: {'FeatureName': {'PriorValue':'NewValue'}}
feature_transformations = {
    'Domesticated': {'No': 0, 'Yes': 1},
}

# Custom functions to be run, format is {function: 'arguments'}, note that dataset is always included as an argument
# by default, it does not need to be listed here
custom_functions_to_be_run = {
    log_transform_base10 : 'AverageWeight',
    identify_if_zodiac_animal: 'ChineseZodiacYear'
}

# List of features to be scaled, format is ['FeatureName1', 'FeatureName2']
features_to_be_scaled = [
    'AverageWeight'
]

# List of features to be standardized, format is ['FeatureName1', 'FeatureName2']
features_to_be_standardized = [
    'AverageWeight'
]

# Dict of features to be renamed, format is {'PriorName', 'NewName'}
features_to_be_renamed = {
    'ChineseZodiacYear' : 'IsAnimalOfTheZodiac'
}

# List of features to hot encode, format is ['FeatureName1', 'FeatureName2']
features_to_hot_encode = [
    'Habitat'
]
