"""
dna = ['AUG', 'AUC', 'UCG']

dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)            # ['GAU', 'UCG', 'UAA']
"""

reading_list = ['Harry Potter','1984','The Fault in Our Stars','The Mom Test','Life in Code']
reading_list.append('Pachinko')
reading_list.remove('The Fault in Our Stars')
reading_list.pop(1)
print(reading_list)