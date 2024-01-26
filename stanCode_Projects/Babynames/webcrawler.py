"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #

        tags = soup.find_all("table", {"class": "t-stripe"})  # tags是list
        amount_male = 0
        amount_female = 0
        tokens = []
        for tag in tags:
            target = tag.tbody.text  # 長字串
            tokens = target.split()  # 將長字串split存入list
        for i in range(len(tokens)):
            if i % 5 == 2 and tokens[i].replace(",", "").isdigit():
                amount_male += int(tokens[i].replace(",", ""))
            elif i % 5 == 4 and tokens[i].replace(",", "").isdigit():
                amount_female += int(tokens[i].replace(",", ""))
        print("Male Number: " + str(amount_male))
        print("Female Number: " + str(amount_female))


if __name__ == '__main__':
    main()
