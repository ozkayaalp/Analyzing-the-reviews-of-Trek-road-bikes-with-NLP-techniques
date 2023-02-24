import pandas as pd
import streamlit as st
from PIL import Image

st.title("Analyzing the reviews of Trek road bikes with NLP techniques")
st.header("Finding the best Trek!")

option = st.selectbox(
    'Select model',
    ('Trek1500', 'Pilot_5_0', 'Madone_5_2', 'Trek2100', 'Trek1_5','Emonda', 'Pilot2_1', 'Trek2300', 'Trek1000', 'Trek2200', 'MadoneSL5_9','Madone6_9','Trek1_2','Madone5_9', 'Superlight59', 'Madone5_2_2008', 'Madone4_5', 'Trek1800c','MadoneSL5_2', 'Trek5200', 'Trek1200'))

if option == 'Trek1500':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1500sentst.png")
            st.image(image, caption='Trek1500')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1500pie_st.png")
            st.image(image, caption='Trek1500')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1500_Keyword_st.png")
            st.image(image, caption='Trek1500')
            
            st.subheader('Top Keywords about Trek1500 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1500.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1500sent_wk.png")
            st.image(image, caption='Trek1500')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1500pie_wk.png")
            st.image(image, caption='Trek1500')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1500_wordcloud_wk.png")
            st.image(image, caption='Trek1500')
            
            st.subheader('Top Keywords about Trek1500 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1500wk.csv")
            st.dataframe(df)
                        
            
if option == 'Pilot_5_0':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Pilot5.0sent.png")
            st.image(image, caption='Pilot5.0')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Pilot5.0pie_st.png")
            st.image(image, caption='Pilot5.0')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Pilot5.0_Keyword_st.png")
            st.image(image, caption='Pilot5.0')
            
            st.subheader('Top Keywords about Pilot5.0 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrekPilot5.0.csv")
            st.dataframe(df)
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Pilot5.0sent_wk.png")
            st.image(image, caption='Pilot5.0')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Pilot5.0pie_wk.png")
            st.image(image, caption='Pilot5.0')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Pilot5.0_wordcloud_wk.png")
            st.image(image, caption='Pilot5.0')
                        
            st.subheader('Top Keywords about Pilot5.0 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwPilot5.0wk.csv")
            st.dataframe(df)
            
if option == 'Madone_5_2':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone_5_2sentst.png")
            st.image(image, caption='Madone5.2')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone_5_2pie_st.png")
            st.image(image, caption='Madone5.2')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone_5_2_Keyword_st.png")
            st.image(image, caption='Madone5.2')
            
            st.subheader('Top Keywords about Madone5-2 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone_5_2.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone_5_2sent_wk.png")
            st.image(image, caption='Madone5.2')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone_5_2pie_wk.png")
            st.image(image, caption='Madone5.2')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone_5_2_wordcloud_wk.png")
            st.image(image, caption='Madone5.2')
            
            st.subheader('Top Keywords about Madone5-2 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone_5_2wk.csv")
            st.dataframe(df)

if option == 'Trek2100':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek2100sentst.png")
            st.image(image, caption='Trek2100')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek2100pie_st.png")
            st.image(image, caption='Trek2100')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek2100_Keyword_st.png")
            st.image(image, caption='Trek2100')
            
            st.subheader('Top Keywords about Trek2100 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek2100.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek2100sent_wk.png")
            st.image(image, caption='Trek2100')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek2100pie_wk.png")
            st.image(image, caption='Trek2100')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek2100_wordcloud_wk.png")
            st.image(image, caption='Trek2100')
            
            st.subheader('Top Keywords about Trek2100 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek2100wk.csv")
            st.dataframe(df)   

if option == 'Trek1_5':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1_5sentst.png")
            st.image(image, caption='Trek1_5')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1_5pie_st.png")
            st.image(image, caption='Trek1_5')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1_5_Keyword_st.png")
            st.image(image, caption='Trek1_5')
            
            st.subheader('Top Keywords about Trek1-5 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1_5.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1_5sent_wk.png")
            st.image(image, caption='Trek1_5')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1_5pie_wk.png")
            st.image(image, caption='Trek1_5')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1_5_wordcloud_wk.png")
            st.image(image, caption='Trek1_5')
            
            st.subheader('Top Keywords about Trek1-5 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1_5wk.csv")
            st.dataframe(df)
            
if option == 'Emonda':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Emondasentst.png")
            st.image(image, caption='Emonda')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Emondapie_st.png")
            st.image(image, caption='Emonda')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Emonda_Keyword_st.png")
            st.image(image, caption='Emonda')
            
            st.subheader('Top Keywords about Emonda Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwEmonda.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Emondasent_wk.png")
            st.image(image, caption='Emonda')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Emondapie_wk.png")
            st.image(image, caption='Emonda')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Emonda_wordcloud_wk.png")
            st.image(image, caption='Emonda')
            
            st.subheader('Top Keywords about Emonda Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwEmondawk.csv")
            st.dataframe(df)

if option == 'Pilot2_1':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Pilot2_1sentst.png")
            st.image(image, caption='Pilot2_1')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Pilot2_1pie_st.png")
            st.image(image, caption='Pilot2_1')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Pilot2_1_Keyword_st.png")
            st.image(image, caption='Pilot2_1')
            
            st.subheader('Top Keywords about Pilot2_1 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwPilot2_1.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Pilot2_1sent_wk.png")
            st.image(image, caption='Pilot2_1')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Pilot2_1pie_wk.png")
            st.image(image, caption='Pilot2_1')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Pilot2_1_wordcloud_wk.png")
            st.image(image, caption='Pilot2_1')
            
            st.subheader('Top Keywords about Pilot2_1 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwPilot2_1wk.csv")
            st.dataframe(df)
            
if option == 'Trek2300':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek2300sentst.png")
            st.image(image, caption='Trek2300')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek2300pie_st.png")
            st.image(image, caption='Trek2300')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek2300_Keyword_st.png")
            st.image(image, caption='Trek2300')
            
            st.subheader('Top Keywords about Trek2300 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek2300.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek2300sent_wk.png")
            st.image(image, caption='Trek2300')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek2300pie_wk.png")
            st.image(image, caption='Trek2300')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek2300_wordcloud_wk.png")
            st.image(image, caption='Trek2300')
            
            st.subheader('Top Keywords about Trek2300 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek2300wk.csv")
            st.dataframe(df)
            
if option == 'Trek1000':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1000sentst.png")
            st.image(image, caption='Trek1000')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1000pie_st.png")
            st.image(image, caption='Trek1000')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1000_Keyword_st.png")
            st.image(image, caption='Trek1000')
            
            st.subheader('Top Keywords about Trek1000 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1000.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1000sent_wk.png")
            st.image(image, caption='Trek1000')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1000pie_wk.png")
            st.image(image, caption='Trek1000')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1000_wordcloud_wk.png")
            st.image(image, caption='Trek1000')
            
            st.subheader('Top Keywords about Trek1000 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1000wk.csv")
            st.dataframe(df)
            
if option == 'Trek2200':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek2200sentst.png")
            st.image(image, caption='Trek2200')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek2200pie_st.png")
            st.image(image, caption='Trek2200')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek2200_Keyword_st.png")
            st.image(image, caption='Trek2200')
            
            st.subheader('Top Keywords about Trek2200 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek2200.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek2200sent_wk.png")
            st.image(image, caption='Trek2200')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek2200pie_wk.png")
            st.image(image, caption='Trek2200')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek2200_wordcloud_wk.png")
            st.image(image, caption='Trek2200')
            
            st.subheader('Top Keywords about Trek2200 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek2200wk.csv")
            st.dataframe(df)
            
if option == 'MadoneSL5_9':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_9sentst.png")
            st.image(image, caption='MadoneSL5-9')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_9pie_st.png")
            st.image(image, caption='MadoneSL5-9')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_9_Keyword_st.png")
            st.image(image, caption='MadoneSL5-9')
            
            st.subheader('Top Keywords about MadoneSL5_9 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadoneSL5_9.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_9sent_wk.png")
            st.image(image, caption='MadoneSL5-9')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_9pie_wk.png")
            st.image(image, caption='MadoneSL5-9')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_9_wordcloud_wk.png")
            st.image(image, caption='MadoneSL5_9')
            
            st.subheader('Top Keywords about MadoneSL5_9 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadoneSL5_9wk.csv")
            st.dataframe(df)
            
if option == 'Madone6_9':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone6_9sentst.png")
            st.image(image, caption='Madone6-9')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone6_9pie_st.png")
            st.image(image, caption='Madone6-9')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone6_9_Keyword_st.png")
            st.image(image, caption='Madone6-9')
            
            st.subheader('Top Keywords about Madone6-9 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone6_9.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone6_9sent_wk.png")
            st.image(image, caption='Madone6-9')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone6_9pie_wk.png")
            st.image(image, caption='Madone6-9')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone6_9_wordcloud_wk.png")
            st.image(image, caption='Madone6_9')
            
            st.subheader('Top Keywords about Madone6-9 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone6_9wk.csv")
            st.dataframe(df)
            
if option == 'Trek1_2':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1_2sentst.png")
            st.image(image, caption='Trek1-2')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1_2pie_st.png")
            st.image(image, caption='Trek1-2')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1_2_Keyword_st.png")
            st.image(image, caption='Trek1-2')
            
            st.subheader('Top Keywords about Trek1_2 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1_2.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1_2sent_wk.png")
            st.image(image, caption='Trek1-2')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1_2pie_wk.png")
            st.image(image, caption='Trek1-2')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1_2_wordcloud_wk.png")
            st.image(image, caption='Trek1_2')
            
            st.subheader('Top Keywords about Trek1_2 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1_2wk.csv")
            st.dataframe(df)
            
if option == 'Madone5_9':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone5_9sentst.png")
            st.image(image, caption='Madone5_9')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone5_9pie_st.png")
            st.image(image, caption='Madone5_9')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone5_9_Keyword_st.png")
            st.image(image, caption='Madone5_9')
            
            st.subheader('Top Keywords about Madone5_9 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone5_9.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone5_9sent_wk.png")
            st.image(image, caption='Madone5_9')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone5_9pie_wk.png")
            st.image(image, caption='Madone5_9')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone5_9_wordcloud_wk.png")
            st.image(image, caption='Madone5_9')
            
            st.subheader('Top Keywords about Madone5_9 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone5_9wk.csv")
            st.dataframe(df)
            
if option == 'Superlight59':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Superlight59sentst.png")
            st.image(image, caption='Superlight59')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Superlight59pie_st.png")
            st.image(image, caption='Superlight59')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Superlight59_Keyword_st.png")
            st.image(image, caption='Superlight59')
            
            st.subheader('Top Keywords about Superlight59 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwSuperlight59.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Superlight59sent_wk.png")
            st.image(image, caption='Superlight59')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Superlight59pie_wk.png")
            st.image(image, caption='Superlight59')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Superlight59_wordcloud_wk.png")
            st.image(image, caption='Superlight59')
            
            st.subheader('Top Keywords about Superlight59 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwSuperlight59wk.csv")
            st.dataframe(df)  
            
if option == 'Madone5_2_2008':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone5_2_2008sentst.png")
            st.image(image, caption='Madone5_2_2008')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone5_2_2008pie_st.png")
            st.image(image, caption='Madone5_2_2008')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone5_2_2008_Keyword_st.png")
            st.image(image, caption='Madone5_2_2008')
            
            st.subheader('Top Keywords about Madone5_2_2008 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone5_2_2008.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone5_2_2008sent_wk.png")
            st.image(image, caption='Madone5_2_2008')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone5_2_2008pie_wk.png")
            st.image(image, caption='Madone5_2_2008')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone5_2_2008_wordcloud_wk.png")
            st.image(image, caption='Madone5_2_2008')
            
            st.subheader('Top Keywords about Madone5_2_2008 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone5_2_2008wk.csv")
            st.dataframe(df) 
            
if option == 'Madone4_5':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone4_5sentst.png")
            st.image(image, caption='Madone4_5')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone4_5pie_st.png")
            st.image(image, caption='Madone4_5')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone4_5_Keyword_st.png")
            st.image(image, caption='Madone4_5')
            
            st.subheader('Top Keywords about Madone4_5 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone4_5.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Madone4_5sent_wk.png")
            st.image(image, caption='Madone4_5')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Madone4_5pie_wk.png")
            st.image(image, caption='Madone4_5')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Madone4_5_wordcloud_wk.png")
            st.image(image, caption='Madone4_5')
            
            st.subheader('Top Keywords about Madone4_5 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadone4_5wk.csv")
            st.dataframe(df)  

if option == 'Trek1800c':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1800csentst.png")
            st.image(image, caption='Trek1800c')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1800cpie_st.png")
            st.image(image, caption='Trek1800c')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1800c_Keyword_st.png")
            st.image(image, caption='Trek1800c')
            
            st.subheader('Top Keywords about Trek1800c Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1800c.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1800csent_wk.png")
            st.image(image, caption='Trek1800c')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1800cpie_wk.png")
            st.image(image, caption='Trek1800c')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1800c_wordcloud_wk.png")
            st.image(image, caption='Trek1800c')
            
            st.subheader('Top Keywords about Trek1800c Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1800cwk.csv")
            st.dataframe(df)
            
if option == 'MadoneSL5_2':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_2sentst.png")
            st.image(image, caption='MadoneSL5_2')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_2pie_st.png")
            st.image(image, caption='MadoneSL5_2')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_2_Keyword_st.png")
            st.image(image, caption='MadoneSL5_2')
            
            st.subheader('Top Keywords about MadoneSL5_2 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadoneSL5_2.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_2sent_wk.png")
            st.image(image, caption='MadoneSL5_2')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_2pie_wk.png")
            st.image(image, caption='MadoneSL5_2')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/MadoneSL5_2_wordcloud_wk.png")
            st.image(image, caption='MadoneSL5_2')
            
            st.subheader('Top Keywords about MadoneSL5_2 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwMadoneSL5_2wk.csv")
            st.dataframe(df)  
        
if option == 'Trek5200':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek5200sentst.png")
            st.image(image, caption='Trek5200')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek5200pie_st.png")
            st.image(image, caption='Trek5200')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek5200_Keyword_st.png")
            st.image(image, caption='Trek5200')
                         
            st.subheader('Top Keywords about Trek5200 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek5200.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek5200sent_wk.png")
            st.image(image, caption='Trek5200')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek5200pie_wk.png")
            st.image(image, caption='Trek5200')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek5200_wordcloud_wk.png")
            st.image(image, caption='Trek5200')
                         
            st.subheader('Top Keywords about Trek5200 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek5200wk.csv")
            st.dataframe(df)
                         
if option == 'Trek1200':
    option_sw = st.selectbox('Select feature',('Strength', 'Weakness'))
    if option_sw == 'Strength':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1200sentst.png")
            st.image(image, caption='Trek1200')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1200pie_st.png")
            st.image(image, caption='Trek1200')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1200_Keyword_st.png")
            st.image(image, caption='Trek1200')
                         
            st.subheader('Top Keywords about Trek1200 Strength')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1200.csv")
            st.dataframe(df)
            
    elif option_sw == 'Weakness':
        analysis = st.radio('Analysis',['Sentiment','Emotion', 'Keyword'])
        if analysis == "Sentiment":
            st.subheader('Sentiment Analysis NLTK Vader Lexicon')
            image = Image.open(r"C:/Users/ozkay/Trek1200sent_wk.png")
            st.image(image, caption='Trek1200')
        elif analysis == "Emotion":
            st.subheader('Emotion Analysis with NCRLex')
            image = Image.open(r"C:/Users/ozkay/Trek1200pie_wk.png")
            st.image(image, caption='Trek1200')
        elif analysis == "Keyword":
            st.subheader('Keyword Analysis YAKE')
            image = Image.open(r"C:/Users/ozkay/Trek1200_wordcloud_wk.png")
            st.image(image, caption='Trek1200')
            st.subheader('Top Keywords about Trek1200 Weakness')
            df = pd.read_csv(r"C:/Users/ozkay/kwTrek1200wk.csv")
            st.dataframe(df)
            
        

    
    
    

    




