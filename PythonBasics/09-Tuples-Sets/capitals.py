"""
capitals.py — Tuples
Chapter 9: Tuples & Sets

Demonstrates:
- Creating tuples (immutable, ordered)
- Storing tuples in a list
- Tuple unpacking in a for loop
- Why tuples are useful for coordinate data (shouldn't change)
- Converting between list and tuple
"""

# --- Tuple basics ---
# Tuples use parentheses () — same as lists but immutable (can't be modified)

bogota = (4.7110, -74.0721)    # (latitude, longitude)

print(bogota[0])    # Output: 4.711    (access by index, same as list)
print(bogota[-1])   # Output: -74.0721

# Trying to modify a tuple would crash:
# bogota[0] = 10    # TypeError: 'tuple' object does not support item assignment
# That's the point — coordinates shouldn't change!

# --- Tuple unpacking ---
# Assign multiple variables from a tuple in one line

lat, lon = bogota
print(f'Latitude:  {lat}')     # Output: Latitude:  4.711
print(f'Longitude: {lon}')     # Output: Longitude: -74.0721

# --- List of tuples ---
# Each item in the list is a tuple: (city_name, lat, lon)

capitals = [
    ('Bogotá', 4.7110, -74.0721),
    ('Lima', -12.0464, -77.0428),
    ('São Paulo', -23.5505, -46.6333),
    ('Buenos Aires', -34.6037, -58.3816),
    ('Santiago', -33.4569, -70.6483)
]

# --- Unpacking in a for loop ---
# Each iteration unpacks the tuple into three variables

print('\n--- Latin American Capitals 🌎 ---')
for city, lat, lon in capitals:
    print(f'{city:<15} lat: {lat:>9.4f}  lon: {lon:>9.4f}')

# Output:
# Bogotá          lat:    4.7110  lon:  -74.0721
# Lima            lat:  -12.0464  lon:  -77.0428
# São Paulo       lat:  -23.5505  lon:  -46.6333
# Buenos Aires    lat:  -34.6037  lon:  -58.3816
# Santiago        lat:  -33.4569  lon:  -70.6483

# --- Tuples as dictionary keys ---
# Lists can't be dict keys (they're mutable), but tuples can

city_map = {
    (4.7110, -74.0721): 'Bogotá',
    (-12.0464, -77.0428): 'Lima'
}
print(city_map[(4.7110, -74.0721)])    # Output: Bogotá

# --- Converting between list and tuple ---
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)

print(type(my_tuple))     # Output: <class 'tuple'>
print(type(back_to_list)) # Output: <class 'list'>
