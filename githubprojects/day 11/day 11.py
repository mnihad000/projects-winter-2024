import bs4
import lxml
import requests

basic_url = 'https://books.toscrape.com/catalogue/page-{}.html'

high_rated_titles=[]

for page in range(1,52):
    url_page = basic_url.format(page)

    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:
            book_title = book.select('a')[1]['title']

            high_rated_titles.append(book_title)

for b in high_rated_titles:
    print(b)