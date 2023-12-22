import pandas as pd
from data_exploration_functions import remove_house_numbers, remove_cm

# reading the dataset
df = pd.read_csv("Naturdenkmal_Bäume_CHBWIL.csv", sep=";")

# Data Exploration &  Data Cleaning

# size of dataset, output of first 5 rows
#print(df.shape)
#print(df.head())

# exploring columns & missing values
#print(df.columns)
#print(df.info())

# exploring columns where "nummer" is missing and see if it is available in the columns standort or adresse
#print(df[["standort","adresse","nummer"]][df["nummer"].isna()])

# deleting multiple columns from the dataset by creating a new subset
df.drop(columns =["baumnr", "east_etrs89", "north_etrs89", "originalbild"],inplace=True)

# Translating the columns into English
new_column_names = ["id_nr", "name_ger","name_sci","location","street","house_number","postalcode","tree_circ","prot_purpose","senate_admin_nr","lat","long","image"]
df.columns = new_column_names

# Data Type Conversions
columns_to_str = ["name_ger","name_sci", "location", "street", "tree_circ", "image", "prot_purpose", "senate_admin_nr","house_number"]
df[columns_to_str] = df[columns_to_str].astype(str)

# Data Cleaning Finetuning

# Removing numerics in column "street"
df['street'] = df['street'].apply(remove_house_numbers)

# Adding unit into the column
df.rename(columns={"tree_circ": "tree_circ_cm"}, inplace=True)

# Deleting both unit and "und"
df["tree_circ_cm"] = df["tree_circ_cm"].apply(remove_cm)
print(df.tree_circ_cm.head())