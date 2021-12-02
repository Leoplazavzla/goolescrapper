import requests
import sys
import pandas as pd
import webbrowser
import urllib
from bs4 import BeautifulSoup

# Location of excel file
dataLocation = "C:\\Users\\Leonardo Plaza\\Documents\\123 Frank Tasks\\linkedinbelgiumbot\\goolescrapper\\mainData.xlsx"
df = pd.read_excel(dataLocation)

# number of rows for excel file
rows = len(df)

# headers for browser
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
}

# main URL to use for scrapping
searchURL = "https://www.google.com/search?q=linkedin"

# Script
for row in range(rows):
    studentName = df.loc[row][0]
    soup = BeautifulSoup(requests.get(
        searchURL + ' ' + studentName + ' ' + 'prince2').text, "html.parser")
    linkElements = soup.find('div', {"class": "kCrYT"})
    # get the anchor tags
    # print(linkElements.a)
    enlace = linkElements.a
    # print(enlace['href'])

    # get the raw href
    try:
        inicio = enlace['href']
    except TypeError:
        inicio = 'No link available'

    # clean the raw link from Google (Remove noise text)
    inicioa = inicio.find("https")
    iniciof = inicio.find("&")

    # # LinkedIn profile link
    imprimir = inicio[inicioa:iniciof]
    print(imprimir)
    # print(inicioa)
    # print(iniciof)

    df.loc[row, 'linkedinID'] = imprimir
    df.to_excel(dataLocation, index=False)
