# Proteins that compose Zaire Ebolavirus
# Created 2.9.2018 by CB Fay

from Bio import ExPASy
from Bio import SwissProt

proteins = {
    'NP' : 'L7QHU5',
    'VP35' : 'A0A0G2YFL4',
    'VP40' : 'X5H596',
    'GP' : 'A9QPL9',
    'VP30' : 'A0A0K1NZ17',
    'VP24' : 'A0A0K1NYE7',
    'L' : 'L7QHR8'
}

records = [SwissProt.read(ExPASy.get_sprot_raw(p)) for p in proteins.values()]
table = dict(zip(proteins.keys(), records))

print('Protein Length')
for protein in table:
    print(protein, '\t', table[protein].sequence_length)
