"""
playlists.py — Sets and Set Operations
Chapter 9: Tuples & Sets

Demonstrates:
- Creating sets (no duplicates, unordered)
- Converting a list to a set to remove duplicates
- Set operations: union |, intersection &, difference -, symmetric difference ^
- .add() and .discard() methods
- Fast membership testing with 'in'
"""

# --- Set basics ---
# Sets use curly braces {} — like dicts but with no key-value pairs

genres = {'rock', 'pop', 'jazz', 'rock', 'pop', 'indie'}
print(genres)
# Output: {'rock', 'jazz', 'pop', 'indie'}  — duplicates removed automatically!
# Note: order is NOT guaranteed in sets

# --- Removing duplicates from a list ---
raw_list = ['Python', 'JavaScript', 'Python', 'Go', 'JavaScript', 'Rust']
unique = set(raw_list)
print(unique)       # Output: {'Python', 'Go', 'JavaScript', 'Rust'}

# Convert back to list if you need indexing
unique_list = list(unique)

# --- Two playlists with overlapping songs ---
playlist_a = [
    'MGMT - Little Dark Age',
    'Joji - YUKON (INTERLUDE)',
    'Rihanna - Only Girl (In The World)',
    'Dean Martin - Everybody Loves Somebody',
    'MGMT - Little Dark Age',              # duplicate
    'Childish Gambino - Me and Your Mama'
]

playlist_b = [
    'Joji - YUKON (INTERLUDE)',
    'Bad Bunny - Tití Me Preguntó',
    'Rihanna - Only Girl (In The World)',
    'Karol G - CAIRO',
    'Bad Bunny - Tití Me Preguntó',        # duplicate
    'Dean Martin - Everybody Loves Somebody'
]

# Convert to sets (removes duplicates automatically)
set_a = set(playlist_a)
set_b = set(playlist_b)

# --- Set Operations ---

# Intersection & — songs in BOTH playlists
both = set_a & set_b
print('\n🎵 In both playlists:')
for song in both:
    print(f'  {song}')
# Output includes: Joji, Rihanna, Dean Martin

# Difference - — songs only in A (not in B)
only_a = set_a - set_b
print('\n🔵 Only in Playlist A:')
for song in only_a:
    print(f'  {song}')
# Output: MGMT, Childish Gambino

# Difference - — songs only in B (not in A)
only_b = set_b - set_a
print('\n🟠 Only in Playlist B:')
for song in only_b:
    print(f'  {song}')
# Output: Bad Bunny, Karol G

# Union | — all songs, no duplicates
combined = set_a | set_b
print(f'\n🎶 Combined playlist ({len(combined)} unique songs):')
for song in combined:
    print(f'  {song}')

# Symmetric difference ^ — songs in one but NOT both
exclusive = set_a ^ set_b
print(f'\n✨ Exclusive to one playlist only ({len(exclusive)} songs):')
for song in exclusive:
    print(f'  {song}')

# --- Adding and removing ---
set_a.add('Tame Impala - Eventually')
set_a.discard('MGMT - Little Dark Age')   # safe remove — no error if missing
set_a.discard('Song That Does Not Exist') # does nothing, no crash

# --- Membership testing (faster than lists for large collections) ---
print('\nIs "Karol G - CAIRO" in Playlist B?', 'Karol G - CAIRO' in set_b)
# Output: True
