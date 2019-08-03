import pytest
import sys
sys.path.append('..')
from processing import *
from test_parameters import *
import numpy as np 
import pandas as pd

@pytest.mark.parametrize('animals, test_mapping_for_nulls', [(animals, test_mapping_for_nulls)])
def test_map_nulls(animals, test_mapping_for_nulls):
    processed_test_set = map_nulls(animals, test_mapping_for_nulls)
    assert processed_test_set.isnull().any().any() == False
    assert processed_test_set.shape[1] == animals.shape[1]

@pytest.mark.parametrize('animals, test_data_features, test_target_feature', [(animals, test_data_features, test_target_feature)])
def test_select_features(animals, test_data_features, test_target_feature):
    processed_test_set = select_features(animals, test_data_features, test_target_feature)
    assert processed_test_set.shape[1] == (len(test_data_features) + len(test_target_feature))
    assert processed_test_set.shape[0] == animals.shape[0]

@pytest.mark.parametrize('animals, test_data_features, test_target_feature', [(animals, test_data_features, test_target_feature)])
def test_set_datatypes(animals, test_data_features, test_target_feature):
    processed_test_set = set_datatypes(animals, test_data_features, test_target_feature)
    assert type(processed_test_set.Animal.at[0]) == str
    assert type(processed_test_set.MaxLifespan.at[0]) == np.float64
    assert processed_test_set.shape == animals.shape

@pytest.mark.parametrize('animals_no_nans, test_feature_transformations', [(animals_no_nans, test_feature_transformations)])
def test_transform_features(animals_no_nans, test_feature_transformations):
    processed_test_set = transform_features(animals_no_nans, test_feature_transformations)
    assert processed_test_set.Domesticated.at[0] == 0
    assert type(processed_test_set.Domesticated.at[0]) == np.int64
    assert processed_test_set.shape == animals_no_nans.shape

@pytest.mark.parametrize('animals_no_nans, test_custom_functions_to_be_run', [(animals_no_nans, test_custom_functions_to_be_run)])
def test_custom_functions(animals_no_nans, test_custom_functions_to_be_run):
    processed_test_set = custom_functions(animals_no_nans, test_custom_functions_to_be_run)
    assert processed_test_set.shape == animals_no_nans.shape

@pytest.mark.parametrize('animals_no_nans, test_features_to_be_scaled', [(animals_no_nans, test_features_to_be_scaled)])
def test_scale_features(animals_no_nans, test_features_to_be_scaled):
    processed_test_set = scale_features(animals_no_nans, test_features_to_be_scaled)
    assert processed_test_set.AverageWeight.max() <= 1.00001
    assert processed_test_set.AverageWeight.min() >= -0.00001

@pytest.mark.parametrize('animals_no_nans, test_features_to_be_standardized', [(animals_no_nans, test_features_to_be_standardized)])
def test_standardize_features(animals_no_nans, test_features_to_be_standardized):
    processed_test_set = standardize_features(animals_no_nans, test_features_to_be_standardized)
    assert processed_test_set.AverageWeight.mean() <= 0.01
    assert processed_test_set.AverageWeight.mean() >= -0.01

@pytest.mark.parametrize('animals_no_nans, test_features_to_be_renamed', [(animals_no_nans, test_features_to_be_renamed)])
def test_rename_features(animals_no_nans, test_features_to_be_renamed):
    processed_test_set = rename_features(animals_no_nans, test_features_to_be_renamed)
    assert 'ChineseZodiacYear' in processed_test_set.columns

@pytest.mark.parametrize('animals_no_nans, test_features_to_hot_encode', [(animals_no_nans, test_features_to_hot_encode)])
def test_hot_encode(animals_no_nans, test_features_to_hot_encode):
    processed_test_set = hot_encode(animals_no_nans, test_features_to_hot_encode)
    assert 'Fantasy' in processed_test_set.columns
    assert 'Habitat' not in processed_test_set.columns
    assert ~processed_test_set.isnull().any().any()
