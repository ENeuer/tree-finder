1. Searched for a project that interests me. Difficulties to decide as there is such a vast amount of datasets
available. However I was looking for,
- something that interests me & and I can relate to
- relatively up-to-date data, i.e. nothing older than max. 5 years

2. Data sources I looked at
- Kaggle (more ML focused -> for future)
- WHO.int/data
- UCI (University of California) ML Repository
- daten.Berlin (open source data from Berlin)

3. Choice: A data set about protected trees in Berlin's district Charlottenburg- Wilmersdorf. This interests me for multiple reasons:
- I live in this district of Berlin
- In the past I obtained a hunting license in Germany, even though I do not actively hunt now or ever have. My main reason for this was
due to always being interested in the wildlife and nature that we have here around us. I had noticed that too many of my friends and family
know so little about the trees or animals around us.
- downloaded: 21.12.2023 last updated: 17.11.2023
- source: https://daten.berlin.de/datensaetze/als-naturdenkmale-gesch%C3%BCtzte-b%C3%A4ume-charlottenburg-wilmersdorf

4. Data Exploration & Data Cleaning

- Loading the dataset -> a small data set with only 38 rows and 17 columns
- exploring the columns & missing values
Understanding these columns:
    - standort: sometimes includes the address, sometimes it's a location such as a landmark
    - adresse: street + house number
    - nummer: the house number, here we encounter missing values

Missing vales:
    - nummer: 7 rows
    - "baumnr", "north_etrs89 ", "east_etrs89", "breitengrad", "laengengrad", "originalbild" : all rows

Next steps:
- explore the columns where the nummer is missing and see if it is available in the column adresse
- get rid of the columns "baumnr", "east_etrs89", "north_etrs89", "originalbild"
    -> north_etrs89 and "east_etrs89" both refer to the European Terrestrial Reference System 1989, a geodetic Cartesian reference frame.
    -> for simplicity reasons I decided to stick with the reference frame already known to me, i.e. the geographic coordinate system
    based on latitude and longitude

Results:
- no additional house number was given for the 7 rows with missing values in "nummer" --> tbd how to depict this data later
- the updated dataframe now only consists of 13 columns

5. Renaming of columns into English
The dataframe is now reduced, but all columns are still in German, therefore as a next measure, I will rename the columns by translating them into english

6. Data type conversions
Most of the columns are still marked as the Dtype "object" and must be converted for further analysis

Next steps:
- deep dive data format of current columns and transfer into correct data type

Results in:
- transfer into data type "str": "name_ger","name_sci", "location", "street", "tree_circ", "image", "prot_purpose", "senate_admin_nr", "house_number"

- more data cleanings must be done with "tree_circ"


7. Fine tuning of columns
Some columns are still not where they should be
- street is now a string, but must be removed of the numerics

- tree_circ was transferred into string as it contains the units (cm) and sometimes more than 1 value
  Trees with multiple values have more than one trunk.
  Idea: First add the unit (cm) to the columns name and delete from rows, then find all rows with len()>3 to see what the max. no of trunks is a tree in this set can have
  Add as many new columns to the data set as we have max. no. of trunks, naming them "circ_trunk_1", "circ_trunk_2", etc.
  If a tree has only one number in "tree_circ", then only "circ_trunk_1" is filled and the other columns get a 0 as default
