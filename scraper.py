import datetime
import requests
from bs4 import BeautifulSoup

url = "https://pixelford.com/blog/"

response = requests.get(url, headers={ "user-agent": "I'm not bad"})    
#print (response.status_code)                     
html = response.content
soup = BeautifulSoup(html, "html.parser")
blogs = soup.find_all('article', class_= "type-post")

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()
    blog_datetime_string = blog.find('time', class_="entry-time").get('datetime')
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    pretty_date = blog_datetime.strftime("%a %b %m %H %m")
    print(f"{pretty_date} - {title}")


#print(requests.utils.default_headers())
#a_tags = soup.find_all('a', class_="entry-title-link")

#for a_tag in a_tags:
    #print(a_tag.get_text())

#list_of_a_tags = list(map(lambda a_tag: a_tag.get_text(), a_tags))
#print(list_of_a_tags)