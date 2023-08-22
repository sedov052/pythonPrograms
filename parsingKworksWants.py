import requests
from time import sleep
while True:
    with open("parsed.txt", "w") as file:
        response = requests.post("https://kwork.ru/projects").json()
        orders = response["data"]["wants"]
        for order in orders:
            file.write(f"{order['name']} ({order['kworkCount']} Предложений) -> {order['priceLimit']} - https://kwork.ru{order['url'][1:]}\n")
            file.write(f"{order['description']}\n\n")
    sleep(60)
