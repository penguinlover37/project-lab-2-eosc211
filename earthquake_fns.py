import numpy as np
import pandas as pd
from datetime import datetime

#Function 1
def get_coastlines(coasts_file):
    '''
    Reads longitudes and latitudes of the world's coastlines from csv file.
    Returns individual 1D arrays of longitudes along world coastline and latitudes along world coastline.
    input: coasts_file
    outputs: lon_coast, lat_coast
    '''
    try:
        df = pd.read_csv(coasts_file)
        lon_coast = df.iloc[:,0]
        lat_coast = df.iloc[:,1]
        return lon_coast, lat_coast
    except:
        raise IOError
    

#Function 2
def get_plate_boundaries(plates_files):
    '''
    Reads csv file containing three columns (column 1: plate boundary name abbreviations, column 2: latitudes in degrees, column
    3: longitudes in degrees) and organizes the columns into a dictionary.
    Returns a dictionary where keys correspond to tectonic plate abbreviations, and values are 2D arrays containing longitudes in 
    the first column and latitudes in the second column
    input: plates_file
    output: pb_dict
    '''
    try:
        df = pd.read_csv(plates_files)
        plate = np.array(df.iloc[:, 0])
        lat = np.array(df.iloc[:, 1])
        lon = np.array(df.iloc[:, 2])
        pb_dict = dict()
    
        for i in range(len(plate)):
            if plate[i] not in pb_dict:
                pb_dict[plate[i]] = np.array([[lon[i], lat[i]]])
            else:
                pb_dict[plate[i]] = np.append(pb_dict[plate[i]], np.array([[lon[i], lat[i]]]), axis=0)
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
    '''
    Extracts columns latitude, longitude, depth, magnitude, and time from the input dataframe.
    Converts the time column to datetime objects.
    Returns the columns as individual 1D arrays
    input: df
    outputs: lats, lons, depths, magnitudes, times
    '''
    lats = np.array(df["Latitude"])
    lons = np.array(df["Longitude"])
    depths = np.array(df["Depth"])
    magnitudes = np.array(df["Magnitude"])
    times_object = np.array(df["Time"])
    times = pd.to_datetime(times_object)
    return lats, lons, depths, magnitudes, times

#helper function for c2 graph

def break_line_at_boundary(pb_dict, threshold=180):
    '''
    To solve the issue of plate boundaries "crossing the map" when it needs to transpose between -180 to 180 and vice versa.
    Creates a list of points at the boundary 180 and ensures that the lines are temporarily split just only at that point and continuous everywhere else
    returns list as broken_lines
    
    '''
    broken_lines = []

    for bound_lons, bound_lats in pb_dict.items():
        boundary_indices = np.where(np.abs(np.diff(bound_lats[:, 0])) > threshold)[0] + 1
        line_segments = np.split(bound_lats, boundary_indices)
        
        broken_lines.extend(line_segments)

    return broken_lines

