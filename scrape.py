from bs4 import BeautifulSoup
import requests
import psycopg2

class Scrape:
    # url = 'https://quotes.toscrape.com/'
    # def getData(url):
    #     r = requests.get(url)
    #     f = open('quotes.html', 'w')
    #     f.write(r.text)
    # getData(url)
    def uploadDB(quote, author, tags):
        conn = psycopg2.connect(database = "scrape", user = "user", password = "user", host = "db")
        curr = conn.cursor()
        curr.execute(f"insert into scraper_scrape(quote, author, tags) values (%s, %s, %s)", (quote, author, tags ))
        curr.close()
        conn.commit()
        conn.close()
    
    
    soup = BeautifulSoup(open('quotes.html'), 'html.parser')

    for i in soup.find_all("div", class_="quote"):
        tags = []
        for j in i.find_all("a", class_="tag"):
            tags.append(j.text)
        uploadDB(i.span.text, i.small.text, ", ".join(tags) )
            

    