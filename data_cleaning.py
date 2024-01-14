import pandas as pd
from data_cleaning_functions import remove_house_numbers, remove_cm, split_tree_circ

def cleanup_data(df):

    # deleting multiple columns from the dataset
    df.drop(columns =["baumnr", "east_etrs89", "north_etrs89", "originalbild"],inplace=True)

    # 5. Translating the columns into English
    new_column_names = ["id_nr", "name_ger","name_sci","location","street","house_number","postalcode","tree_circ","prot_purpose","senate_admin_nr","lat","long","image"]
    df.columns = new_column_names

    # 6. Data Type Conversions
    columns_to_str = ["name_ger","name_sci", "location", "street", "tree_circ", "image", "prot_purpose", "senate_admin_nr","house_number"]
    df[columns_to_str] = df[columns_to_str].astype(str)


    # 7. Data Cleaning Finetuning
    # Removing numerics in column "street"
    df['street'] = df['street'].apply(remove_house_numbers)

    # Adding unit into the tree_circ column
    df.rename(columns={"tree_circ": "tree_circ_cm"}, inplace=True)

    # Deleting both unit and " und" form tree_circ_cm column
    df["tree_circ_cm"] = df["tree_circ_cm"].apply(remove_cm)
    print(df.tree_circ_cm.head())

    # Adding split tree trunk as int columns to dataframe
    df_updated = split_tree_circ(df,"tree_circ_cm")

    # adding tr_count column to data frame
    df_updated["tr_count"] = df["tree_circ_cm_list"].apply(lambda x: len(x) if x else None)
    # adding trunk_mean column to data frame
    df_updated["trunk_mean"] = round(df["tree_circ_cm_list"].apply(lambda x: sum(x)/len(x) if x else None),2)

    # Saving the updated dataframe
    #df_updated.to_csv("df_cleaned.csv")

    return df_updated
