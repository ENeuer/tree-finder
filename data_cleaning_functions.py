import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def remove_house_numbers(street):
    return ''.join(filter(lambda x: not x.isdigit(), street)).rstrip()


# Function to remove "cm" from strings
def remove_cm(measurement):
    return measurement.replace("cm", "").replace(" und", "").strip()

def split_tree_circ(data:pd.DataFrame, column:str):

    col_list = f"{column}_list"

    # splitting the selected column of the dataframe
    data[col_list] = data[column].str.split(' ')
    data[col_list] = data[col_list].apply(convert_to_integers)
    sub_df = data[col_list].apply(pd.Series)

    # changing columns to start with 1 instead of 0
    sub_df.columns += 1

    # adding a prefix to the columns
    sub_df = sub_df.add_prefix('trunk_')

    # concatenate full dataframe with sub_df
    result = pd.concat([data, sub_df], axis=1)

    return result

def split_prot_purp(data:pd.DataFrame, column:str):

    col_list = f"{column}_list"

    # splitting the selected column of the dataframe
    data[col_list] = data[column].str.split(',')
    sub_df = data[col_list].apply(pd.Series)

    # changing columns to start with 1 instead of 0
    sub_df.columns += 1

    # adding a prefix to the columns
    sub_df = sub_df.add_prefix('prot_purp_')

    # concatenate full dataframe with sub_df
    result = pd.concat([data, sub_df], axis=1)

    return result

def convert_to_integers(str_list):
    return [int(x) for x in str_list if x.isdigit()]


def get_location(address):
    geolocator = Nominatim(user_agent="my-tree-app")
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
    except GeocoderTimedOut:
        return None, None
    return None, None
