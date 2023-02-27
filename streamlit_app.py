import json
from pathlib import Path

import pandas as pd
import streamlit as st
from PIL import Image


# load bike dictionary from json file with file prefixes of bike images and csv files
@st.cache_resource
def load_bike_dict():
    with open('bikes.json') as f:
        bike_dict = json.load(f)
    return bike_dict

# get all csv filenames from csvfiles folder
@st.cache_resource
def get_csv_filenames():
    return list(Path('csvfiles').glob(pattern='*.csv'))

# get all png filenames from pngfile folder
@st.cache_resource
def get_png_filenames():
    return list(Path('pngfile').glob(pattern='*.png'))

# load bike image from file
@st.cache_resource
def load_bike_image(image_file):
    return Image.open(image_file)

# load bike dataframe from csv file
@st.cache_resource
def load_bike_dataframe(csvpath):
    return pd.read_csv(csvpath)

# get all files based on bike name prefix
@st.cache_resource
def get_all_files_bike(filenames, bike_name_prefix):
    return [p for p in filenames if p.stem.startswith(bike_name_prefix)]

# get all csv files based on option postfix st or wk
@st.cache_resource
def get_csv_file_by_option(csv_files_per_bike, option_sw):
    for csv_file in csv_files_per_bike:
        if option_sw == 'Weakness' and csv_file.stem.endswith('wk'):
            return csv_file.resolve()
        elif option_sw == 'Strength' and not csv_file.stem.endswith('wk'):
            return csv_file.resolve()
    return None

# get all png files based on analysis and option
@st.cache_resource
def get_png_file_by_analysis_and_option(png_files_per_bike, analysis, option_sw):
    for png_file in png_files_per_bike:
        if analysis == "Sentiment" and 'sent' in png_file.stem.lower():
            pass
        elif analysis == "Emotion" and 'pie' in png_file.stem.lower():
            pass
        elif analysis == "Keyword" and 'keyword' in png_file.stem.lower() or 'wordcloud' in png_file.stem.lower():
            pass
        else:
            continue
        if option_sw == 'Weakness' and png_file.stem.endswith('wk'):
            return png_file.resolve()
        elif option_sw == 'Strength' and png_file.stem.endswith('st'):
            return png_file.resolve()
    return None


st.title("Analyzing the reviews of Trek road bikes with NLP techniques")
st.header("Finding the best Trek!")

options = load_bike_dict()
csv_filenames = get_csv_filenames()
png_filenames = get_png_filenames()

option = st.selectbox(label='Select model', options=options.keys())
png_files_per_bike = get_all_files_bike(png_filenames, bike_name_prefix=options.get(option))
csv_files_per_bike = get_all_files_bike(csv_filenames, bike_name_prefix=f'kw{options.get(option)}')

# st.write(png_files_per_bike)  # just for debugging
# st.write(csv_files_per_bike)  # just for debugging

option_sw = st.selectbox('Select feature', ('Strength', 'Weakness'))
analysis = st.radio('Analysis', ['Sentiment', 'Emotion', 'Keyword'])
png_file = get_png_file_by_analysis_and_option(png_files_per_bike, analysis=analysis, option_sw=option_sw)

if png_file is None:
    st.error(f'No matching image found for prefix: {options.get(option)}; analysis: {analysis}; feature: {option_sw}')
    st.stop()
image = load_bike_image(png_file)
if analysis == "Sentiment":
    st.subheader('Sentiment Analysis NLTK Vader Lexicon')
    st.image(image=image, caption=option)
elif analysis == "Emotion":
    st.subheader('Emotion Analysis with NCRLex')
    st.image(image=image, caption=option)
elif analysis == "Keyword":
    st.subheader('Keyword Analysis YAKE')
    st.image(image=image, caption=option)
    st.subheader('Top Keywords about Trek1500 Strength')
    st.dataframe(load_bike_dataframe(get_csv_file_by_option(csv_files_per_bike, option_sw=option_sw)))

# Setting up columns
c1, c2 = st.columns([1,1])

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if c1.checkbox("Show Dataframe strength"):
    st.subheader("This is strength reviews dataset:")
    df_strength = pd.read_csv("Dataframes/df_strength.csv")
    st.dataframe(data=df_strength)

elif c1.checkbox("Show Dataframe weakness"):
    st.subheader("This is weakness reviews dataset:")
    df_weakness = pd.read_csv("Dataframes/df_weakness.csv")
    st.dataframe(data=df_weakness)

link = '[To see the code in GitHub ](https://github.com/ozkayaalp/Analyzing-the-reviews-of-Trek-road-bikes-with-NLP-techniques)'
c2.markdown(link, unsafe_allow_html=True)
