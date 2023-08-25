# Analyzing-the-reviews-of-Trek-road-bikes-with-NLP-techniques
This project analyzes the customer reviews of Trek Road bikes. The results can be used to identify which aspects of the Trek Road bikes need to be improved (Weaknesses) or which aspects of them are more attractive to road bikers (Strengths). One of the most critical aspects of understanding a business is understanding its strengths and weaknesses. Analyzing why it is thriving or not represents a key to the longevity of that business. As a business owner, it's critical to understand why some bike riders don't choose their products, the reasons behind some aversion, or what positively stood out to them. At this point, customer reviews are quite useful resources in terms of reputation, customer engagement, business improvement, customer relations, brand awareness, and search engine optimization.

To perform this research, I made a dataset of biker reviews and focused my attention on a specific Trek brand and bike forum: roadbikereview.com.

First, I fetched the reviews with API applications and BeautifulSoup library, then converted them into the pandas dataframe.To be ready for analysis, data is cleaned with string operations. Then, I used NLTK text pre-processessing like tokenization, stopwords, lemmatization. 

I proceeded to analyze the review texts with Natural Language Processing techniques to understand the intrinsic feelings and emotions behind reviews. First, I used Sentiment analysis with NLTK Vader Lexicon library to know whether the review was positive, negative, or neutral. Besides identifying the sentiment behind a text, another technique in NLP is to identify the emotion behind it. To achieve this, I use the NCRLex library. NCRLex library allows us to recognize emotions from texts, such as fear, anger, or surprise. This analysis allows me to more accurately understand how customers feel about a specific service or product. To further analyze the reviews, I wanted to identify the main objects of customer comments in their reviews. Keyword extraction is a useful method that computes statistical features related to characteristics for each review, including word case, position, frequency, context, and weights of each term according to these features. 

Overall, unlike bike customers who want to get an idea about Trek models, I believe this model will be useful for business if you want to search product reviews. Apart from the bike industry, this analysis can benefit any other sector with access to customer feedback, like e-commerce, automobile, or the hospitality industry.

streamlit ==v1.17.0
pandas == 1.5.3
matplotlib==3.7.0
NLTK Vader Lexicon
NRCLex 4.0
YAKE
