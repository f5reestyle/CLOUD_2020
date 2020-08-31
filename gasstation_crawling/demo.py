from crawling import GETcity, GETgu
cities = GETcity()
for city in cities :
    gu_s = GETgu(city)
    A=3