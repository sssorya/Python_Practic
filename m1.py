from bs4 import BeautifulSoup

with open('element.xml', 'r') as f:
    file = f.read()
soup = BeautifulSoup(file, 'xml')

names = soup.find_all('name')

ages = soup.find_all('key')

subjects = soup.find_all('price')

print('-'.center(35, '-'))
print('|' + 'Name'.center(15) + '|' + ' Key ' + '|' + 'Price'.center(11) + '|')
for i in range(0, len(names)):
    print('-'.center(35, '-'))
    print(
        f'|{names[i].text.center(15)}|{ages[i].text.center(5)}|{subjects[i].text.center(11)}|')
print('-'.center(35, '-'))
