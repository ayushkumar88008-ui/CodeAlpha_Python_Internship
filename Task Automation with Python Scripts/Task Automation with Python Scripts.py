import requests
from bs4 import BeautifulSoup

print("===== Website Title Scraper =====")

url = input("Enter Website URL: ")

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.text

    print("\nWebsite Title:", title)

    file = open("title.txt", "w")
    file.write("Website URL : " + url + "\n")
    file.write("Website Title : " + title)
    file.close()

    print("\nData Saved Successfully.")

else:
    print("Website Not Found.")