import pandas as pd

def remove_house_numbers(street):
    return ''.join(filter(lambda x: not x.isdigit(), street)).rstrip()


def remove_cm(measurement):
    return measurement.replace("cm", "").strip()

data = {'measurement': ['40 and 50 cm', '30 cm', '25 cm']}
df = pd.DataFrame(data)

# Function to remove "cm" from strings
def remove_cm(measurement):
    return measurement.replace("cm", "").replace("und", "").strip()

# Apply the function to the 'measurement' column
df['measurement'] = df['measurement'].apply(remove_cm)

print(df)
print(len(df["measurement"][0]))




