import math


def distance_latitude_longitude(latitude1, latitude2, longitude1, longitude2):
    r_eq = 6378
    r_p = 6356
    radius_of_earth_at_latitude1 = ((r_eq**2 * math.cos(latitude1))**2 + (r_p**2 * math.sin(latitude1))**2 /
                                    (r_eq * math.cos(latitude1))**2 + (r_p * math.sin(latitude1))**2) ** 0.5

    radius_of_earth_at_latitude2 = ((r_eq**2 * math.cos(latitude2))**2 + (r_p**2 * math.sin(latitude2))**2 /
                                    (r_eq * math.cos(latitude2))**2 + (r_p * math.sin(latitude2))**2) ** 0.5
    mean_radius = (radius_of_earth_at_latitude1 + radius_of_earth_at_latitude2) / 2

    # Haversine Formula
    latitude1, latitude2 = math.radians(latitude1), math.radians(latitude2)
    delta_lat = math.radians(latitude2 - latitude1)
    delta_long = math.radians(longitude2 - longitude1)
    a = (math.sin(delta_lat / 2))**2 + math.cos(latitude1) * math.cos(latitude2) * (math.sin(delta_long / 2))**2
    c = 2 * math.atan2(a ** 0.5, (1-a) ** 0.5)
    distance = mean_radius * c
    return distance


lat1, lon1 = 500359, 0o0504253
lat2, lon2 = 583838, 0o030412
print(distance_latitude_longitude(lat1, lat2, lon1, lon2))
