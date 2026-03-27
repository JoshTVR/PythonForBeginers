"""
csv_parser.py — String split() and join()
Chapter 10: String Methods

Demonstrates:
- .split() to break a string into a list
- .join() to merge a list back into a string
- zip() to pair two lists together
- Real-world use: parsing CSV-style data
"""

# --- .split() ---
# Breaks a string into a list using a delimiter

csv_row = 'Bogotá,Colombia,4.7110,-74.0721'
fields = csv_row.split(',')

print(fields)
# Output: ['Bogotá', 'Colombia', '4.7110', '-74.0721']

# Labeling each field
labels = ['City', 'Country', 'Latitude', 'Longitude']

for label, value in zip(labels, fields):
    print(f'{label:<12}: {value}')

# Output:
# City        : Bogotá
# Country     : Colombia
# Latitude    : 4.7110
# Longitude   : -74.0721

# Without a delimiter, .split() splits on any whitespace
sentence = '   The   quick   brown   fox   '
words = sentence.split()
print(words)
# Output: ['The', 'quick', 'brown', 'fox']  — strips extra spaces too

# --- .join() ---
# Joins a list into a string with a separator

cities = ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena']

print(', '.join(cities))
# Output: Bogotá, Medellín, Cali, Barranquilla, Cartagena

print(' | '.join(cities))
# Output: Bogotá | Medellín | Cali | Barranquilla | Cartagena

print(''.join(['H', 'o', 'l', 'a']))
# Output: Hola

# --- Practical: round-trip split → process → join ---
tags_raw = 'python, beginner, programming, tutorial, code'
tags = [tag.strip() for tag in tags_raw.split(',')]  # split and strip each tag
print(tags)
# Output: ['python', 'beginner', 'programming', 'tutorial', 'code']

# Re-join as hashtags
hashtags = ' '.join(f'#{tag}' for tag in tags)
print(hashtags)
# Output: #python #beginner #programming #tutorial #code

# --- Multi-line CSV parsing ---
print('\n--- Parsing multiple CSV rows ---')

data = [
    'Lima,Peru,-12.0464,-77.0428',
    'Buenos Aires,Argentina,-34.6037,-58.3816',
    'Santiago,Chile,-33.4569,-70.6483'
]

for row in data:
    city, country, lat, lon = row.split(',')
    print(f'{city} ({country}) → ({lat}, {lon})')

# Output:
# Lima (Peru) → (-12.0464, -77.0428)
# Buenos Aires (Argentina) → (-34.6037, -58.3816)
# Santiago (Chile) → (-33.4569, -70.6483)
