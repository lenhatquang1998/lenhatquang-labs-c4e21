from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()
html_page = raw_data.decode("utf-8")
soup = BeautifulSoup(html_page, "html.parser")
section = soup.find('section', "section chart-grid")
ul = section.find('ul')
li_list = ul.find_all("li")

new_list = []

for li in li_list:
    a = li.h3.a
    title = a.string
    link = url + a["href"]
    a2 = li.h4.a
    title2 = a2.string
    news = {
        "Title": title,
        "Link": link,
        "Name": title2,
    }
    new_list.append(news)
import pyexcel
pyexcel.save_as(records=new_list, dest_file_name="itunes.xlsx")


