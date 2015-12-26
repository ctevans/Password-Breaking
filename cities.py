import sys 
import string

def inserter(x):
    try:
        for i in characters:
            print(i.join(x))
    except:
        return

characters = set(string.printable) - set(string.digits) - set(string.ascii_letters)

f = open('locations.txt', 'r', encoding='utf8')
s = sys.stdout
output = open('2wordcities.lst', 'w')
sys.stdout = output

data = ''.join(f).strip().replace('"', '')[1:-2]
data = data.split('],')

for country in data:
    cities = country.split(':[')
    
    s.write(cities[0] + '\n')
    
    if len(cities) > 1:
        cities = cities[1].split(',')

        for city in cities:
            city = city.lower().split(' ')
            if len(city) == 2:
                inserter(city)

f.close()
output.close()