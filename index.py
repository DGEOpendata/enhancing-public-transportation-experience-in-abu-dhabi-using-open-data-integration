python
import requests
import folium
from datetime import datetime

# Function to fetch Abu Dhabi public transportation data
def get_transport_data():
    url = "https://api.abudhabi.opendata/public_transport"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to create a map with transportation routes
def create_transport_map(data):
    # Initialize map centered on Abu Dhabi
    transport_map = folium.Map(location=[24.4539, 54.3773], zoom_start=12)
    
    # Add transportation routes to the map
    for route in data['routes']:
        folium.Marker(
            location=[route['latitude'], route['longitude']],
            popup=f"Route: {route['route_number']}, Stop: {route['stop_name']}",
            icon=folium.Icon(color='blue', icon='bus', prefix='fa')
        ).add_to(transport_map)
    
    # Save the map to an HTML file
    transport_map.save('AbuDhabiTransportMap.html')

# Fetch and display the transportation data
transport_data = get_transport_data()
if transport_data:
    create_transport_map(transport_data)
else:
    print("Failed to retrieve transport data.")
