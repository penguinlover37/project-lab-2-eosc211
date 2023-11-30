import numpy as np
import pandas as pd
from datetime import datetime

#Function 1
def get_coastlines(coasts_file):
    try:
        df = pd.read_csv(coasts_file)
        lon_coast = df.iloc[:,0]
        lat_coast = df.iloc[:,1]
        return lon_coast, lat_coast
    except:
        raise IOError
    

#Function 2
def get_plate_boundaries(plates_files):
    try:
        df = pd.read_csv(plates_files)
        plate = np.array(df.iloc[:, 0])
        lat = np.array(df.iloc[:, 1])
        lon = np.array(df.iloc[:, 2])
        pb_dict = dict()
        plate_name = ""
        for i in range(len(plate)):
            if plate_name != plate[i]:   
                plate_name = plate[i]
                pb_dict[plate_name] = np.array([[lat[i]], [lon[i]]])
            else:
                temp = pb_dict[plate_name]
                pb_dict[plate_name] = np.append(temp, np.array([[lat[i]], [lon[i]]]), axis=1)
        return pb_dict
        
    except:
        raise IOError
#Function 3
def get_earthquakes(filename):
    try: 
        earthquakes = pd.read_csv(filename)
        return earthquakes
    except:
        raise IOError

#Function 4
def parse_earthquakes_to_np(df):
    lats = np.array(df["Latitude"])
    lons = np.array(df["Longitude"])
    depths = np.array(df["Depth"])
    magnitudes = np.array(df["Magnitude"])
    times_object = np.array(df["Time"])
    times = pd.to_datetime(times_object)
    return lats, lons, depths, magnitudes, times



