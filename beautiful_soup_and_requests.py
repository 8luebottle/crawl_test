import requests as r

from bs4 import BeautifulSoup


result = r.get('https://www.google.com')

#Check Status Code & HTTP headers
"""
print(result.status_code)
print(result.headers)
"""

src = result.content

# Check Contents of the Website(This case : Google)
"""
print(src)
"""

# Create BeautifulSoup object
soup = BeautifulSoup(src, 'lxml')

#SEE a list of all of the Links on the Page
# find_all is a Method
links = soup.find_all('a') # which is mean find all of the "a" tags (links)
"""
print(links)
print('\n')
"""

# 'text' function to access the text content between the <a> </a> tags.
for link in links:
    if '뉴스' in link.text:
        print(link)
        print(link.attrs['href'])

