from threading import Thread

import requests
from bs4 import BeautifulSoup as BS

def get_page(year, num):
    code = "ccc%.2ds%d" % (year, num)

    req = requests.get("http://wcipeg.com/problem/" + code)

    soup = BS(req.text, 'html.parser')

    parsed = (soup.find(id="descContent")
                  .get_text()
                  .strip()
                  .replace("Stage 1", "Stage 1\n\n")
                  .replace("\nInput", "\n\nInput")
                  .replace("\nOutput", "\n\nOutput")
                  .replace("Sample", "\nSample")
                  .replace("\n\n\n", "\n\n")
    )

    with open("problems/" + code + ".txt", "wb+") as f:
        f.write(str(parsed).encode("utf-8"))



for year in range(1, 16):
    for num in range(1, 6):
        t = Thread(target=get_page, args=(year,num))
        t.start()
















