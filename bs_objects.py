import requests as r

from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

with open('index.html', 'w') as f:
    f.write(html_doc)

soup = BeautifulSoup(html_doc, 'lxml')

print('\n')
print(soup.b)
print(soup.p)
print('\n')

print('*' * 50)
print('\n', soup.find('b'))
print(soup.find('p'),'\n')
print('*' * 50)
print('\n', soup.find_all('b'), '\n')
print('*' * 50)
print('\n', soup.b.name, '\n')
print('3' * 50)

tag = soup.b
print(tag)
tag.name = 'bold'
print(tag)

tags = soup.find_all('b')[2]
print(tags)
print(tags.attrs) # Return as Dictionary

