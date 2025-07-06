import pandas as pd
from docx import Document


#create a dictionary
data = {"name": ["John", "Anna", "Peter", "Linda"],"age": [28, 24, 35, 32], "city": ["New York", "Paris", "Berlin", "London"]}

df = pd.DataFrame(data)


print(df)