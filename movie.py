import requests
from bs4 import BeautifulSoup
import csv


url = "https://hurawatch.at/movies?page=2"
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

     
    result = [[new.text.strip(),minutes.text.strip()[:5],dura.text.strip()[6:13],lol + links]]
    header = ["Title","Year", "Duration","Links"]


    with open("page2.csv" , "a",newline="\n", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(result)
        
        
        
   

