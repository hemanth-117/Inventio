import requests
from bs4 import BeautifulSoup
def title(link):
    """| the function is used to print ratings of all tv-shows in IMDB genrated by the link.
    | these are present in an div with class = 'ipl-rating-star small'
    | under this there is a span with class = 'ipl-rating-star__rating' in which the text is the rating of each anime
    :param link: link of tv-shows in IMDB from which we are scrapping ratings of each
    :type info: string
    """
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html5lib')
    movies=soup.find_all('div',class_='ipl-rating-star small')
    for i in range(0,len(movies)):
        sample1=movies[i].find('span',class_='ipl-rating-star__rating')
        rate=sample1.get_text()
        print(rate)
title('https://www.imdb.com/list/ls008957859/')
title('https://www.imdb.com/list/ls008957859/?sort=list_order,asc&st_dt=&mode=detail&page=2')
title('https://www.imdb.com/list/ls008957859/?sort=list_order,asc&st_dt=&mode=detail&page=3')