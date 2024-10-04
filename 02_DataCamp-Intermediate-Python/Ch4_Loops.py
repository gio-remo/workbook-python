""" Loop over dictionary """

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print(f"the capital of {k} is {v}")

""" Loop over NumPy array """

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height:
    print(f"{x} inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)

""" Loop over DataFrame (1) """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for i, row in cars.iterrows():
    print(i)
    print(row)

""" Loop over DataFrame (2) """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars.info)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(f"{lab}: {row['cars_per_cap']}")

""" Add column (1) """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for i, row in cars.iterrows():
    cars.loc[i, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)

""" Add column (2) """

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)