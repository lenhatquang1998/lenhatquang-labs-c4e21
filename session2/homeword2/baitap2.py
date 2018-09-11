from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_page = raw_data.decode("utf-8")
f_conn = open('suavn.html', 'wb')
f_conn.write(raw_data)
f_conn.close()
soup = BeautifulSoup(html_page, "html.parser")
table = soup.find('table', id = 'tableContent')
header_list = soup.find_all('td','h_t')
header_data = []

for name in header_list:
    header_data.append(name.contents[0].strip())
row = table.find_all('tr')
row_list = []

for item in row:
    row_item_list = item.find_all('td','b_r_c')
    row_data_list = []
    for i in row_item_list:
        i = i.string
        if i != None:
            i = i.strip()        
        row_data_list.append(i)  
    if len(row_data_list):
        row_list.append(row_data_list)    

    end = []
for item in row_list:
    value_list = []
    value = {
            "item" : item[0]
        }  
    for i in range(len(header_data)):
        value[header_data[i]] =  item[1+i]   
              
    end.append(value)


import pyexcel
pyexcel.save_as(records=end,dest_file_name="suavn.xlsx")
