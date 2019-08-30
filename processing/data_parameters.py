from processing.custom_functions import *

"""Target Feature

Dictionary with {'FeatureName': type}
""" 
target_feature = {'MaxLifespan': float}


"""Dependent Features to be included in final dataset

Dictionary with {'FeatureName': type}
"""
data_features = {
    'Habitat' : str,
    'AverageWeight' : float,
    'ChineseZodiacYear' : str,
    'Domesticated' : str
}


"""Operations to be executed on null values

Dictionary with {'FeatureName': Operation to be taken}

To drop all rows that have a null value for a feature, enter 'DROP'
To fill all feature null values with a zero, enter 'ZEROS'
To fill all feature null values with a custom string, enter that custom string
To fill all feature null values with the mean value of that column, enter 'MEAN'
To execute a custom function upon feature null values, define that function in 
custom_functions.py and enter the name of the function in the dictionary
"""
mappings_for_nulls = {
    'Animal' : 'DROP',
    'Habitat': 'Land',
    'AverageWeight': 'MEAN',
    'ChineseZodiacYear': '2200-01-01',
    'Domesticated': 'DROP',
    'MaxLifespan': 'DROP'
}


"""Transformations to make on feature values

Dictionary with {'FeatureName': Dictionary with {'Value to be transformed': 'Value to be transformed to'} }
"""
feature_transformations = {
    'Domesticated': {'No': 0, 'Yes': 1},
}


"""Custom functions to be executed

Dictionary with {function: 'arguments'}

Note that dataset is always included as the first argument for each function by default and should not be 
included in the dictionary below. Only additional arguments should be provided below. For an example, reference the mapping
below and the example functions in custom_functions.py. 
"""
custom_functions_to_be_run = {
    log_transform_base10 : 'AverageWeight',
    identify_if_zodiac_animal: 'ChineseZodiacYear'
}


"""Features to be scaled

List of feature names: ['FeatureName1', 'FeatureName2']
"""
features_to_be_scaled = [
    'AverageWeight'
]


"""Features to be standardized

List of feature names: ['FeatureName1', 'FeatureName2']
"""
features_to_be_standardized = [
    'AverageWeight'
]


"""Features to be renamed

Dictionary with {'PriorName', 'NewName'}
"""
features_to_be_renamed = {
    'ChineseZodiacYear' : 'IsAnimalOfTheZodiac'
}


"""Features to hot encode

List of feature names: ['FeatureName1', 'FeatureName2']
"""
features_to_hot_encode = [
    'Habitat'
]
