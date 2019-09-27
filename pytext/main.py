import requests

from bs4 import BeautifulSoup

responce=requests.get("https://stackoverflow.com/questions/936687/how-do-i-declare-a-2d-array-in-c-using-new#")
soup=BeautifulSoup(responce.text,"html.parser")

questions=soup.select(".question-hyperlink")

for question in questions:

    print(question.getText())
