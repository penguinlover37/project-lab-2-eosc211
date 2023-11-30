import numpy as np
import pandas as pd
from datetime import datetime

#Function 1
def get_coastlines(coasts_file):
    try:
        df = pd.read_csv(coasts_file)
        lon_coast = df.iloc[:,0]
        lat_coast = df.iloc[:,1]
    except:
        raise IOError
    return lon_coast, lat_coast

#Function 2

def get_plate_boundaries(boundaries_file):
    try:
        df = pd.read_csv(boundaries_file)
        plate_dict = {}

        
        for index, row in df.iterrows():
            #
            plate_name = row['Plate Abbreviation']
            latitude = row['Latitude']
            longitude = row['Longitude']

            
            if plate_name in plate_dict:
                
                plate_dict[plate_name] = np.vstack([plate_dict[plate_name], [longitude, latitude]])
            else:
                
                plate_dict[plate_name] = np.array([[longitude, latitude]])

       
        return plate_dict

    except Exception as e:
        raise IOError(f"An error occurred while reading the CSV file: {str(e)}")

#Function 3


#Function 4
def parse_earthquakes_to_np(df):
    lats = np.array(df["Latitude"])
    lons = np.array(df["Longitude"])
    depths = np.array(df["Depth"])
    magnitudes = np.array(df["Magnitude"])
    times = np.array(df["Time"])
    return lats, lons, depths, magnitudes, times


