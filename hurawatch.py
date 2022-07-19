
import requests
from bs4 import BeautifulSoup
import datetime
import gspread

url = "https://hurawatch.at/movies?page=5"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
lol = "https://hurawatch.at"





film = soup.find("div", class_ = "content")
list = film.find_all("div", class_ = "item")


for movies in list:
    new = movies.find("a", class_ ="title")
    
    minutes = movies.find("div", class_= "meta")
    dura = movies.find("div", class_ = "meta")
    links = movies.find("a", class_= "poster")["href"]
    

    # print(f"Name of the movie: {new.text.strip()}")
    # print(f"Year: {minutes.text.strip()[:5]}")
    # print(f"Duration : {dura.text.strip()[6:13]}")
    # print(f"Watch Movie here: {lol + links}")
    # print()

     
    result = {"Title":new.text.strip(),"Year":minutes.text.strip()[:5],"Duration":dura.text.strip()[6:13],"Links":lol + links}
    gc = gspread.service_account(filename='hu.json')
    sh = gc.open('hurawatch').sheet1
    sh.append_row([result["Title"],result["Year"],result["Duration"],result["Links"]])
        








    





