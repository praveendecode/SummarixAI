import nltk
import streamlit as st
from textblob import TextBlob
from streamlit_option_menu import *
from streamlit_extras.keyboard_url import keyboard_to_url
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
import json as js
import time
import googletrans
from googletrans import Translator
from googletrans import LANGUAGES
import gtts
from gtts import gTTS
import os
import requests
import pandas as pd
#__________________________________________________________


class language_ai :

    def process(self):
        st.set_page_config(page_title='Summarization Project By Praveen', layout="wide")
        st.markdown("<style>div.block-container{padding-top:1rem;}</style>", unsafe_allow_html=True)
        def lottie(filepath):
            with open(filepath, 'r') as file:
                return js.load(file)

        col1, col2, col3 = st.columns([4, 7, 3])

        col2.markdown(
            "<h1 style='font-size: 100px;'><span style='color: cyan;'>Summarization</span> <span style='color: white;'></span> </h1>",
            unsafe_allow_html=True)
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col4, col1, col2, col3 = st.columns([12, 10, 3, 10])

        with col1:
            file = lottie("summarization.json")
            st_lottie(
                file,
                speed=1,
                reverse=False,
                loop=True,
                quality='low',
                # renderer='svg',
                height=400,
                width=500,
                key=None
            )
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")
        col2.write("")

        API_URL = "https://api-inference.huggingface.co/models/google/pegasus-cnn_dailymail"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        try :
            col1, col2, col3 = st.columns([3, 7, 3])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            with col2:
                col2.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Provide</span> <span style='color: white;'>Text</span> </h1>",
                    unsafe_allow_html=True)
                text = st.text_area("")
                if st.button('Proceed'):
                    output = query({
                        "inputs": text,
                    })

                    res = output[0]['summary_text']
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.write("")
                    col2.markdown(
                        "<h1 style='font-size: 40px;'><span style='color: cyan;'>Summarised</span> <span style='color: white;'>Information</span> </h1>",
                        unsafe_allow_html=True)
                    st.code(res)
        except :
            col1, col2, col3 = st.columns([3, 7, 3])
            col2.success('Provide Information Again !!!')
#___________________________________________________________________________________________________________________________________________





# Object Creation

object = language_ai()
object.process()