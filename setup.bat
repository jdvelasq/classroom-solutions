@echo off

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m nltk.downloader punkt_tab stopwords
