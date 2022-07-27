from requests import get 
from bs4 import BeautifulSoup
url_divar = "https://divar.ir/s/tehran"
page = get(url = url_divar)
soup = BeautifulSoup(page.content, "html.parser")
for element in soup.find_all("a", class_="kt-accordion-item__header", href = True):
    print(element['href'])
    temp_url = url_divar + element['href']
    for new_el in soup.find_all("div", class_= "post-card-item kt-col-6 kt-col-xxl-4"):
        print(new_el.text)
