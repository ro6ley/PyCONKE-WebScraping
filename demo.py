# import the library to query a website
import requests

# import beautiful soup too
from bs4 import BeautifulSoup

# specify the url to scrap
urlToScrap = 'https://github.com/NaiRobley?tab=repositories'

# Query the web page
page = requests.get(urlToScrap)

# parse the html file
soup = BeautifulSoup(page.content, 'html.parser')

# to view the source
# print(soup.prettify)

# Find main content
main_content = soup.find('div', {'id': 'user-repositories-list'})

# Extract list of repositories
list_of_repos = main_content.findAll('li')

# Extract each repos details
for repo in list_of_repos:
    print('Repository name: ' + repo.a.string)
    print('Link: http://github.com' + repo.a.get('href'))
    if repo.p and repo.p.string:
        print("Description: " + repo.p.string)
    else:
        print("No description available for this repository")
