import pandas as pd
import streamlit as st
import altair as alt
import requests
from data_cleaning import cleanup_data
import folium
from streamlit_folium import st_folium


@st.cache_data
def read_clean_data(url):
    response = requests.get(url)
    print(response.status_code)
    response_dict = response.json()

    data = response_dict["index"]
    df = pd.DataFrame(data)

    df_clean = cleanup_data(df)

    return df_clean


def create_chart(sub_df, column):
    values_df = sub_df[column].value_counts().reset_index()
    values_df.columns = [column, "Count"]

    chart = (
        alt.Chart(values_df)
        .mark_bar(color="#CBD4C2")
        .encode(
            x="Count",
            y=alt.Y(column, sort="-x"),
        )
    )
    return chart


def create_map(df):
    map = folium.Map(location=(df.loc[3, ["latitude"]], df.loc[3, ["longitude"]]), zoom_start=15)

    for idx, row in df.iterrows():

        if pd.isna(row["latitude"]):
            continue

        folium.Marker((row["latitude"], row["longitude"]), popup=row["name_ger"]).add_to(map)

    # return st_folium(map, width="1500")
    return st_folium(map, use_container_width=True)


def main():
    st.set_page_config(page_title="Protected Trees", page_icon=None, layout="wide", initial_sidebar_state="auto",
                       menu_items={'About': "# This is a header. This is an *extremely* cool app!"})

    # df = pd.read_csv("/Users/eNeuer/PycharmProjects/tree-finder/df_cleaned.csv")
    url = "https://www.berlin.de/ba-charlottenburg-wilmersdorf/verwaltung/aemter/umwelt-und-naturschutz/naturschutz/baeume/index.php/index/all.json?q="
    df = read_clean_data(url)

    st.title("🌳 Protected Trees in Berlin Charlottenburg-Wilmersdorf")

    st.write("### Map of all trees*")
    st.write("(Zoom out for all trees)")
    st_data = create_map(df)

    st.write("### Tree Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="No. of trees", value=df.shape[0])

    with col2:
        st.metric(label="Trees with > 1 trunk", value=len(df[df['tr_count'] > 1]))

    with col3:
        st.metric(label="Mean trunk (cm)", value=round(df['trunk_mean'].mean(), 2))

    st.divider()
    st.write("### Types and Frequency of Trees")

    sub_df = df[["name_ger", "name_sci"]]
    new_column_names = ["Tree Name - GER", "Tree Name - LAT"]
    sub_df.columns = new_column_names
    column = st.selectbox('Select the column to analyze', sub_df.columns)

    chart = create_chart(sub_df, column)

    st.altair_chart(chart, use_container_width=True)

    # st.write("### Protection Reason for trees")
    # st.dataframe(df)

    st.divider()
    st.text('* Only trees for which coordinates could be identified are displayed here.')


if __name__ == '__main__':
    main()
