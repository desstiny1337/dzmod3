import requests
from bs4 import BeautifulSoup
from context_manager import file_manager
import json
import os


#making dirs
folders = ["authors", "quotes"]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Папка '{folder}' создана.")
    else:
        print(f"Папка '{folder}' уже существует.")

def process_files():
    for folder in folders:
        json_file = os.path.join(folder, f"{folder}.json")
        if not os.path.exists(json_file):
            with open(json_file, "w", encoding="utf-8") as f:
                f.write("[]")  
            print(f"Файл '{json_file}' создан.")
        else:
            print(f"Файл '{json_file}' уже существует.")
        print(f"Обработка файла '{json_file}'...")
        with open(json_file, "r+", encoding="utf-8") as f:
            content = f.read()
            print(f"Содержимое файла: {content}")

process_files()


#parsing the site
def parse_data():
    url = 'https://quotes.toscrape.com/'
    store_to_quotes = []
    store_to_authors = []
    
    html_doc = requests.get(url)

    if html_doc.status_code == 200:
        soup = BeautifulSoup(html_doc.text, 'html.parser')
        elements = soup.find_all('div', class_ = 'quote')
        for element in elements:
            to_quotes = dict()
            to_author = dict()
            tag_list = []
            tags = element.find_all('a', class_ = 'tag')
            for tag in tags:
                tag_list.append(tag.text)
            to_quotes['tags'] = tag_list
            to_quotes['author'] = element.find('small', class_ = 'author').text
            to_quotes['quote'] = element.find('span', class_ = 'text').text
            store_to_quotes.append(to_quotes)

            link = url[:-1]+element.find('a')['href']
            html_doc_1 = requests.get(link)
            if html_doc_1.status_code == 200:
                soup_1 = BeautifulSoup(html_doc_1.text, 'html.parser')
                to_author['fullname'] = soup_1.find('h3', class_ = 'author-title').text
                to_author['born_date'] = soup_1.find('span', class_ = 'author-born-date').text
                to_author['born_location'] = soup_1.find('span', class_ = 'author-born-location').text
                to_author['description'] = soup_1.find('div', class_ = 'author-description').text
                store_to_authors.append(to_author)


    #opening the file using context manager and dumping infon to it
    with file_manager('authors.json', 'w') as f:
        json.dump(store_to_authors, f, indent = 4)
            
    with file_manager('quotes.json', 'w') as f:
        json.dump(store_to_quotes, f, indent = 4)

if __name__ == '__main__':
    parse_data()