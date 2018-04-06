import pandas as pd
from collections import namedtuple
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic
import os

df = pd.read_csv('applicants.csv')

Person = namedtuple("Person", "Name Major Year Companies")
Company = namedtuple("Company", "Name Applicants")

people = []
for index, row in df.iterrows():
    row['Companies'] = row['Companies'].split(", ")
    people.append(Person(row['Name'], row['Major'], row['Year'], row['Companies']))

companies = {}
for p in people:
    for c in p[3]:
        if (c not in companies):
            companies[c] = []
        companies[c].append(p[0])
        
for c in companies:
    print(c + ": ", end='')
    for p in companies[c]:
        print(p + ", ", end='')
    print()





