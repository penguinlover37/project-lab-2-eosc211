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
            plate_name = row['plate']
            latitude = row['lat']
            longitude = row['lon']

            
            if plate_name in plate_dict:
                
                plate_dict[plate_name] = np.vstack([plate_dict[plate_name], [longitude, latitude]])
            else:
                
                plate_dict[plate_name] = np.array([[longitude, latitude]])

       
        return plate_dict

    except Exception as e:
        raise IOError(f"An error occurred while reading the CSV file: {str(e)}")
#Function 3
filename = './IRIS_eq_010100_112422_mag4.csv'
    
def get_earthquakes(filename):
    try: 
        earthquakes = pd.read_csv(filename)
        return earthquakes
    except Exception as e: 
        raise I0Error (f'Error reading the earthquakes file: {e}')

#Function 4
def parse_earthquakes_to_np(df):
    lats = np.array(df["Latitude"])
    lons = np.array(df["Longitude"])
    depths = np.array(df["Depth"])
    magnitudes = np.array(df["Magnitude"])
    times_object = np.array(df["Time"])
    times = pd.to_datetime(times_object)
    return lats, lons, depths, magnitudes, times


