#!/usr/bin/python3.11
import folium
from geopy.geocoders import Nominatim
import csv


with open('insurance.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]


def calculate_average_age(list_items):
    total_age = []
    for item in list_items:
        age = int(item['age'])
        children = item['children']
        if int(children) > 0:
            total_age.append(age)
    print("Average age for person with 1 children or more: " + str(int(sum(total_age)/len(total_age))))


def get_unique_regions(data):
    unique_regions = set()
    for item in data:
        unique_regions.add(item['region'])
    return list(unique_regions)

"""Average charges of smokers and average charges of non smokers"""

def smoker_charges(data):
    smoker_list = []
    non_smoker_list = []
    for item in data:
        smoker = item['smoker']
        charges = float(item['charges'])
        if smoker == 'yes':
            smoker_list.append(charges)
        else:
            non_smoker_list.append(charges)

    average_smoker_charges = round(sum(smoker_list)/len(smoker_list), 2)
    print(f"Average charge for smokers: {average_smoker_charges}")

    average_non_smoker_charges = round(sum(non_smoker_list) / len(non_smoker_list), 2)
    print(f"Average charge for non-smokers: {average_non_smoker_charges}")


def children_smoker(data):
    smokers_with_children = []
    non_smokers_with_children = []
    for item in data:
        smoker = item['smoker']
        children = int(item['children'])
        if children > 0:
            if smoker == "yes":
                smokers_with_children.append(item)
            else:
                non_smokers_with_children.append(item)

    print(f"Number of smokers with children: {len(smokers_with_children)}")
    print(f"Number of non-smokers with children: {len(non_smokers_with_children)}")


children_smoker(data)


# smoker_charges(data)
# calculate_average_age(data)
# print(get_unique_regions(data))


# # Define coordinates for each region
# region_coordinates = {
#     'southwest': [32.0, -105.0],
#     'southeast': [33.0, -85.0],
#     'northwest': [45.0, -120.0],
#     'northeast': [42.0, -75.0],  # Add coordinates for northeast
# }
#
# # Create a base map centered at a specific location
# m = folium.Map(location=[37.7749, -122.4194], zoom_start=5)
#
# # Initialize a dictionary to store the count of people per region
# region_counts = {}
#
# # Iterate through your data and add markers based on regions
# for item in data:
#     region = item.get("region")
#
#     # Increment the count for the region
#     region_counts[region] = region_counts.get(region, 0) + 1
#
#     # Use predefined coordinates or set a default location
#     coordinates = region_coordinates.get(region, [0, 0])
#
#     # Customize the marker color based on the region
#     if region == "southwest":
#         marker_color = "red"
#     elif region == "southeast":
#         marker_color = "gray"
#     elif region == "northeast":
#         marker_color = "purple"
#     elif region == "northwest":
#         marker_color = "blue"
#
#     # Add a marker with a popup showing the region and count of people
#     popup_text = f"Region: {region}<br>People count: {region_counts[region]}"
#     folium.Marker(coordinates, popup=folium.Popup(popup_text, parse_html=True), icon=folium.Icon(color=marker_color)).add_to(m)
#
# # Save the map to an HTML file or display it in the notebook
# m.save("map_with_count_and_northeast.html")
