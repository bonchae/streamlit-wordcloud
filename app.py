# Benefited from https://github.com/rahulbanerjee26/Word_Clouds

import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def get_word_cloud(image,data,max_words,max_font_size):
    if image == 'default':
        wordcloud = WordCloud(width=400, height=400, repeat=True, max_words=max_words,
                      max_font_size= max_font_size, background_color='white',
                      ).generate(data)
    else:
        path = f'data/image_masks/{image}.jpg'
        mask = np.array(Image.open(path))
        wordcloud = WordCloud(width=400, height=400, repeat=True, max_words=max_words,
                        max_font_size= max_font_size,background_color='white',
                        mask = mask).generate(data)
    return wordcloud

st.subheader("Visualize your words using wordcloud")
image = st.selectbox(label='Select Image Mask', options=['default','twitter','hashtag','heart'])

text_input = st.text_input("Enter some texts and press enter")    

if text_input:   
    wordcloud = get_word_cloud(image,text_input,800,15)
    fig1 = plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    st.pyplot(fig1)  

    
    