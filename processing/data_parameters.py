from custom_functions import *

filepath = '/Users/mackdelany/Documents/EDAAG/ed-intelligence/ed-intelligence/data-files' + '/triageCodeSample.csv'

target_feature = {'TriageCode': str}

data_features = {
    'PresentingComplaint' : str, 
    'DOB' : str,
    'Gender' : str,
    'Airway' : str,
    'Breathing' : str,
    'NeuroAssessment' : str,
    'AlcoholAFactorInInjury' : str,
    'AlcoholInLast6Hrs' : str,
    'SignsOfIntoxication' : str,
    'PainScale' : float,
    'CirculatorySkin': str,
    'MentalHealthConcerns': str,
    'CurrentSmoker': str,
    'QuestionTwoAnswer': str,
    'QuestionThreeAnswer': str
}

# DROP = drop null columns
# String = fill null with string
# ZEROS = fill null with zero
# Dictionary = run cleaningFunction, dict should hold {'function name': 'parameters'}
mappings_for_nulls = {
    'DOB': 'DROP',
    'Gender': 'U',
    'Airway': 'ASSUMED OK',
    'Breathing': 'ASSUMED OK',
    'NeuroAssessment': 'ASSUMED OK',
    'AlcoholAFactorInInjury': 'ASSUMED NO',
    'AlcoholInLast6Hrs': 'ASSUMED NO',
    'SignsOfIntoxication': 'ASSUMED NO',
    'PainScale': fill_pain_scale_na_with_cpc_mean,
    'CirculatorySkin': 'ASSUMED NORMAL',
    'MentalHealthConcerns': 'ASSUMED NO',
    'CurrentSmoker': 'ASSUMED NO',
    'QuestionTwoAnswer': 'ASSUMED NO',
    'QuestionThreeAnswer': 'ASSUMED NO'
}

# Dictionary = mapping of values
feature_transformations = {
    'Gender': {'M':0,'U':0.5,'F':1},
    'Airway': {'PATENT':0,'ASSUMED OK':0.25,'OTHER':1},
    'Breathing': {'NO DISTRESS':0,'ASSUMED OK':0.25,'OTHER':1},
    'NeuroAssessment': {'INTACT':0,'ASSUMED OK':0.25,'OTHER':1},
    'AlcoholAFactorInInjury': {'NO':0,'ASSUMED OK':0.25,'YES':1},
    'AlcoholInLast6Hrs': {'NO':0,'ASSUMED NO':0.25,'YES':1},
    'SignsOfIntoxication': {'NO':0,'ASSUMED NO':0.25,'INFLU':0.75, 'INTOX':1},
    'CirculatorySkin': {'NORMAL':0,'ASSUMED NORMAL':0.25,'ALTERED':1},
    'MentalHealthConcerns': {'NO':0,'ASSUMED NO':0.2,'DNS':0.5, 'YES': 1},
    'CurrentSmoker': {'NEVER SMOKED':0,'ASSUMED NO':0.25,'EX SMOKER':0.75, 'YES': 1},
    'QuestionTwoAnswer': {'NO':0, 'ASSUMED NO':0, 'YES':1},
    'QuestionThreeAnswer': {'NO':0, 'ASSUMED NO':0, 'YES':1}
}

# Custom functions to be run, should be a list of lists -> each list should be [feature, [function, parameters]]

custom_functions_to_be_run = {
    DOBtoAGE : 'DOB'
}

features_to_be_scaled = [
    'DOB',
    'PainScale'
]

features_to_be_standardized = [
    
]

features_to_be_renamed = {
    'DOB' : 'Age'
}

features_to_hot_encode = [
    'PresentingComplaint'
]