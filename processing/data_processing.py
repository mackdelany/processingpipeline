import datetime
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

from processing.data_parameters import *
from processing.custom_functions import *


def process_and_return_dataset(filepath, filename):
    processed_data = process_dataset(filepath)
    processed_data.to_csv(filename, encoding='utf-8', index=False)


def process_dataset(filepath):
    dataset = pd.read_csv(filepath)
    dataset = map_nulls(dataset, mappings_for_nulls)
    dataset = select_features(dataset, data_features, target_feature)
    dataset = set_datatypes(dataset, data_features, target_feature)
    dataset = transform_features(dataset, feature_transformations)
    dataset = custom_functions(dataset, custom_functions_to_be_run)
    dataset = scale_features(dataset, features_to_be_scaled)
    dataset = standardize_features(dataset, features_to_be_standardized)
    dataset = rename_features(dataset, features_to_be_renamed)
    dataset = hot_encode(dataset, features_to_hot_encode)
    return dataset.dropna()


def select_features(dataset, data_features, target_feature):
    """Select designated columns from DataFrame

    Keyword arguments:
    dataset -- DataFrame to operate on
    data_features -- Dictionary of independent (X) features and their types
    target_feature -- Dictionary of the dependent (y) feature and it's type
    """
    return dataset[(list(data_features.keys()) + list(target_feature.keys()))]


def map_nulls(dataset, mappings_for_nulls):
    """Execute custom operations on null values in dataframe

    Keyword arguments:
    dataset -- DataFrame to operate on
    mappings_for_nulls -- Dictionary of features (keys) to operate on, and the o
    operations to execute on them (values)
    """
    for feature in mappings_for_nulls:

        if mappings_for_nulls[feature] == 'DROP':
            dataset = dataset.dropna(subset = [feature])

        elif mappings_for_nulls[feature] == 'ZEROS':
            dataset[feature] = dataset[feature].fillna(value=0)

        elif mappings_for_nulls[feature] == 'MEAN':
            dataset[feature] = dataset[feature].fillna(value=dataset[feature].mean())

        elif callable(mappings_for_nulls[feature]):
            dataset[feature] = mappings_for_nulls[feature](dataset)

        else :
            fill_value = mappings_for_nulls[feature]
            dataset[feature].fillna(value=fill_value, inplace=True)

    return dataset


def set_datatypes(dataset, data_features, target_feature):
    """Set column types in feature dataframe

    Keyword arguments:
    dataset -- DataFrame to operate on
    data_features -- Dictionary of independent (X) features and their types
    target_feature -- Dictionary of the dependent (y) feature and it's type
    """
    for feature in data_features.keys():
        dataset[feature] = dataset[feature].astype(data_features[feature])

    for feature in target_feature.keys():
        dataset[feature] = dataset[feature].astype(target_feature[feature])
    return dataset


def transform_features(dataset, feature_transformations):
    """Transform feature values according to pre-set mappings

    Keyword arguments:
    dataset -- DataFrame to operate on
    feature_transformations -- Dictionary of features to operate on (keys) and
    the associated mapping of feature values (values)
    """
    for feature in feature_transformations:
        dataset[feature] = dataset[feature].map(feature_transformations[feature])
    return dataset


def custom_functions(dataset, custom_functions_to_be_run):
    """Transform feature values according to pre-set mappings

    Keyword arguments:
    dataset -- DataFrame to operate on
    feature_transformations -- Dictionary of features to operate on (keys) and
    the associated mapping of feature values (values)
    """
    for custom_function in custom_functions_to_be_run:
        if (custom_functions_to_be_run[custom_function]) == 'NO ADDITIONAL ARGUMENTS':
            dataset = custom_function(dataset)
        else:
            dataset = custom_function(dataset, custom_functions_to_be_run[custom_function])
    return dataset


def scale_features(dataset, features_to_be_scaled):
    """Scale chosen features using MinMaxScaler from SciKitLearn

    Keyword arguments:
    dataset -- DataFrame to operate on
    features_to_be_scaled -- List of features to be scaled
    """
    if len(features_to_be_scaled) > 0:
        scaler = MinMaxScaler()
        dataset[features_to_be_scaled] = scaler.fit_transform(dataset[features_to_be_scaled])
    return dataset


def standardize_features(dataset, features_to_be_standardized):
    """Standardize chosen features using StandardScaler from SciKitLearn

    Keyword arguments:
    dataset -- DataFrame to operate on
    features_to_be_standardized -- List of features to be standardized
    """
    if len(features_to_be_standardized) > 0:
        scaler = StandardScaler()
        dataset[features_to_be_standardized] = scaler.fit_transform(dataset[features_to_be_standardized])
    return dataset


def rename_features(dataset, features_to_be_renamed):
    """Rename chosen columns using a preset mapping

    Keyword arguments:
    dataset -- DataFrame to operate on
    features_to_be_renamed -- Dictionary of features to be renamed (keys) and
    their new names (values)
    """
    dataset.rename(features_to_be_renamed, inplace=True)
    return dataset


def hot_encode(dataset, features_to_hot_encode):
    """Hot encode chosen features using a preset mapping

    Keyword arguments:
    dataset -- DataFrame to operate on
    features_to_hot_encode -- List of features to be hot encoded
    """
    for feature in features_to_hot_encode:
        dummies = pd.get_dummies(dataset[feature])
        dataset.reset_index(drop=True, inplace=True)
        dummies.reset_index(drop=True, inplace=True)
        dataset = pd.concat([dummies, dataset],axis=1, sort=False)
        dataset = dataset.drop(feature, axis=1)
    return dataset