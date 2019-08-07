"""Example functions"""
import numpy as np
import pandas as pd


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


def encode_cyclical_time_of_day(dataset, DateTimeColumn):
    dataset[DateTimeColumn] = pd.to_datetime(dataset[DateTimeColumn]).dt.hour
    dataset['hour_sin'] = np.sin(2 * np.pi * dataset[DateTimeColumn]/23.0)
    dataset['hour_cos'] = np.cos(2 * np.pi * dataset[DateTimeColumn]/23.0)
    dataset = dataset.drop(columns=[DateTimeColumn])
    return dataset
