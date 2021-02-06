import requests
from bs4 import BeautifulSoup
import csv
import os
from multiprocessing import Pool

class ParserSite:
    """Parser"""
    def __init__(self, url='https://www.linux.com/', name='Linux.com'):
        self.url = url
        self.name =name
        
    def get_html(self, url):
        response = requests.get(url) #Response
        return response.text #Your html-cod 

    def get_all_links_and_title(self, html):
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find_all('div', class_='vc_column')
        links = []
        for as_ in div:
            h_3 = as_.find_all('h3')
            for as_ in h_3:
                a = as_.find('a').get('href')
                #title = as_.find('a').text.strip()
                links.append(a)
        return links

    def get_data(self, html):
        soup = BeautifulSoup(html, 'lxml')
        title = soup.find('h1', class_='entry-title').text.strip()
        data = {'title': title}
        return data

    def write_csv(self, title, link):
        with open (f'datas/{self.name}_file.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow((title['title'], link))
            print(title['title'], link)


    def make_all(self, link):
        html = self.get_html(link)
        data = self.get_data(html)
        self.write_csv(data, link)


    def main(self):
        links = self.get_all_links_and_title(self.get_html(self.url))
        with Pool(10) as p:
            p.map(self.make_all, links)

if __name__ == '__main__':
    parser = ParserSite()
    parser.main()