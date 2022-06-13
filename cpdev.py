# load the necessary libraries
from bs4 import BeautifulSoup
import pandas as pd

# open the file and make soup
with open("test.html") as file:
    soup = BeautifulSoup(file, "html.parser")

# TODO: extract all the needed information
# --- all categories sorted with products ---- #

# chemistry: -------------------------
chemistry_category = soup.find_all("li")[25]
# chemistry_products = chemistry_category.find_all("ul", attrs={"class": "sublist application-sublist"})
_chemistry = chemistry_category.find_all("a")
chemistry_links = []
chemistry_name = []
for chem in _chemistry:
    _link1 = chem.get("href")
    chemistry_links.append(_link1)
    _name1 = chem.get_text()
    chemistry_name.append(_name1)

chemistry_dict = {
    "name": chemistry_name,
    "link": chemistry_links
}
chemistry_df = pd.DataFrame(chemistry_dict)
chemistry_df.to_csv("chemistry.csv", index=False)

# life science: -------------------------
life_science_category = soup.find_all("li")[116]
# life_science_products = life_science_category.find_all("ul", attrs={"class": "sublist application-sublist"})
_life_science = life_science_category.find_all("a")
life_science_links = []
life_science_name = []
for ls in _life_science:
    _link2 = ls.get("href")
    life_science_links.append(_link2)
    _name2 = ls.get_text()
    life_science_name.append(_name2)

life_science_dict = {
    "name": life_science_name,
    "link": life_science_links
}
life_science_df = pd.DataFrame(life_science_dict)
life_science_df.to_csv("life_science.csv", index=False)

# reactors: -----------------------------
reactors_category = soup.find_all("li")[199]
# reactors_products = reactors_category.find_all("ul", attrs={"class": "sublist application-sublist"})
_reactors = reactors_category.find_all("a")
reactors_links = []
reactors_name = []
for r in _reactors:
    _link3 = r.get("href")
    reactors_links.append(_link3)
    _name3 = r.get_text()
    reactors_name.append(_name3)

reactors_dict = {
    "name": reactors_name,
    "link": reactors_links
}
reactors_df = pd.DataFrame(reactors_dict)
reactors_df.to_csv("reactors.csv", index=False)

# vials: -------------------------------
vials_category = soup.find_all("li")[242]
# vials_products = vials_category.find_all("ul", attrs={"class": "sublist application-sublist"})
_vials = vials_category.find_all("a")
vials_links = []
vials_name = []
for v in _vials:
    _link4 = v.get("href")
    vials_links.append(_link4)
    _name4 = v.get_text()
    vials_name.append(_name4)

vials_dict = {
    "name": vials_name,
    "link": vials_links
}
vials_df = pd.DataFrame(vials_dict)
vials_df.to_csv("vials.csv", index=False)

# TODO table: --------------------------
# table - headers, names, descriptions,pq, prices, qty_avail,
table = soup.find_all("table", attrs={"class": "product-variant-table"})
table_header = soup.find_all("tr", attrs={"class": "product-variant-header-row"})
item_num = soup.find_all("span", attrs={"itemprop": "sku"})
item_description = soup.find_all("div", attrs={"class": "variant-description"})
table_pq = soup.find_all("div", attrs={"class": "variant-pq"})
table_price = soup.find_all("span", attrs={"itemprop": "price"})
table_qty_avail = soup.find_all("div", attrs={"class": "variant-availablequantity"})

# print(table_qty_avail)

headers = []
for th in table_header:
    header = th.get_text()
    headers.append(header.strip().split())
headers = str(headers)[1:-1]
# pulling out names from the table(item number)
names = []
for item in item_num:
    name = item.get_text()
    names.append(name)
names.pop(0)
# description from table
descriptions = []
for desc in item_description:
    description = desc.get_text()
    descriptions.append(description.strip())
# pq from table
pq = []
for p in table_pq:
    _p = p.get_text()
    pq.append(_p.strip())
# prices from table
prices = []
for price in table_price:
    _price = price.get_text()
    prices.append(_price.strip())
# qty avail
qty_avail = []
for q in table_qty_avail:
    _q = q.get_text()
    qty_avail.append(_q.strip())

# TODO  make csv from the extracted TABLE data, that is requested in the email
table_dict = {
    "Item Number": names,
    "Item Description": descriptions,
    "PQ": pq,
    "Prices": prices,
    "Qty Avail": qty_avail
}
table_df = pd.DataFrame(table_dict)
table_df.to_csv("table.csv", index=False)

# those 3 items with images and big fonts - image_urls,board_products_name
boards = soup.find_all("div", attrs={"class": "product-item"})
board_image_urls = soup.find_all("img", attrs={"class": "scale-with-grid"})
board_name = soup.find_all("h3", attrs={"class": "product-sku"})
board_price = soup.find_all("span", attrs={"class": "price actual-price"})

image_urls = []
for i in board_image_urls:
    _url = i.get("src")
    image_urls.append(_url)

board_products_name = []
for j in board_name:
    _name5 = j.get_text()
    board_products_name.append(_name5)

board_cost = []
for k in board_price:
    _name6 = k.get_text()
    board_cost.append(_name6)

board_dict = {
    "name": board_products_name,
    "image URL": image_urls,
    "price": board_cost
}
board_df = pd.DataFrame(board_dict)
board_df.to_csv("board.csv", index=False)