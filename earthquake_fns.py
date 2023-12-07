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
    lats = np.array(df["Latitude"])
    lons = np.array(df["Longitude"])
    depths = np.array(df["Depth"])
    magnitudes = np.array(df["Magnitude"])
    times_object = np.array(df["Time"])
    times = pd.to_datetime(times_object)
    return lats, lons, depths, magnitudes, times

#helper function for c2 graph

def break_line_at_boundary(pb_dict, threshold=180):
    broken_lines = []

    for bound_lons, bound_lats in pb_dict.items():
        boundary_indices = np.where(np.abs(np.diff(bound_lats[:, 0])) > threshold)[0] + 1
        line_segments = np.split(bound_lats, boundary_indices)
        
        broken_lines.extend(line_segments)

    return broken_lines

#quake subset function
def select_quake_subset(df, times=None, lons=None, lats=None, depths=None, mags=None):
    '''
    argues default arguments that keeps it the same unless you put different things in to fulfill the ifs

    input: df, the original dataframe
    +whatever filters u want

    output: df_sub, a subselected dataframe
    '''
    df_sub = df.copy()

    if depths: #corrected for elegance
        df_sub = df_sub[(df["Depth"] >= depths[0]) & (df["Depth"] <= depths[1])]
    if times:
        df_sub = df_sub[(pd.to_datetime(df["Time"]) >= times[0]) & (pd.to_datetime(df["Time"]) <= times[1])]
    if lons:
        df_sub = df_sub[(df["Longitude"] >= lons[0]) & (df["Longitude"] <= lons[1])]
    if lats:
        df_sub = df_sub[(df["Latitude"] >= lats[0]) & (df["Latitude"] <= lats[1])]
    if mags:
        df_sub = df_sub[(df["Magnitude"] >= mags[0]) & (df["Magnitude"] <= mags[1])]
        
    df = df.reset_index(drop=True)
    df_sub = df_sub.reset_index(drop=True)
    return df_sub

#slope function
def get_slope(start_pt, end_pt):
    """
    Calculates slope between two Cartesian points and returns the degree of the angle created by the slope

    inputs: start_pt, end_pt, the two Cartesian points we want to try
    output: slope_degrees, the degree of the angle created by the slope
    """
    x1, y1 = start_pt
    x2, y2 = end_pt

    if x1 == x2:
        raise ValueError("The x-coordinates of the start and end points cannot be the same. Please provide viable x-coordinates")

    try:
        slope_radians = math.atan((y2 - y1) / (x2 - x1))
    except ZeroDivisionError:
        raise ValueError("The x-coordinates of the start and end points cannot be the same. Please provide viable x-coordinates")

    # Convert slope to degrees
    slope_degrees = math.degrees(slope_radians)

    return slope_degrees

