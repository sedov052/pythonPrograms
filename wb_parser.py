import requests
import pandas as pd
from itertools import count
#import fake_headers


table = pd.DataFrame({
    "Name": [],
    "Price": [],
    "Discount": [],
    "Link": [] })

try:
    for i in count(1):
        products = requests.post(f"https://catalog.wb.ru/catalog/men_shoes/catalog?appType=1&cat=8201&curr=rub&dest=-1257786&page={i}&regions=80,38,83,4,64,33,68,70,30,40,86,75,69,1,31,66,22,110,48,71,114&sort=popular&spp=0")
        for product in products.json()["data"]["products"]:
            
            name = product["name"]
            price = str(product["salePriceU"])[:-2]
            discount = str(product["priceU"])[:-2]
            link = f"https://www.wildberries.ru/catalog/{product['id']}/detail.aspx"

            table.loc[ len(table.index) ] = [name, price, discount, link]

finally:
    table.to_excel("wb_parsed.xlsx")
    print("Done!")