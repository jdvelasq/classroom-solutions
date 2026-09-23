#!/bin/bash

pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 -m nltk.downloader punkt_tab stopwords
