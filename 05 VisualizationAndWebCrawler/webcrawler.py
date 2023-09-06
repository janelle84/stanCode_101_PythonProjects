"""
File: webcrawler.py
Name: Janelle
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
        # print(soup.tbody.text)

        table = soup.find('tbody')
        rows = table.find_all('tr')

        male_num = 0
        female_num = 0

        for row in rows:
            items = row.find_all('td')
            if len(items) > 2:
                num = items[2].text
                num = int(num.replace(',', ''))
                male_num += num

                num_f = items[4].text
                num_f = int(num_f.replace(',', ''))
                female_num += num_f

        print(f"Male Number: {male_num}")
        print(f"Female Number: {female_num}")


if __name__ == '__main__':
    main()
