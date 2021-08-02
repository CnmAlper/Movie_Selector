# you have to use "https://www.themoviedb.org" on this code.
import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "api_url" # please enter your api url before run the code!!!
        self.api_key = "api_key" # please enter your api key before run the code!!!
    
    def getPopulars(self):
        response1 = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response1.json()
    
    def getSearch(self, keyword):
        response2 = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&language=en-US&page=1")
        return response2.json()

movieApi = theMovieDb()
           
while True:
    secim = input("1-Popular Movies\n2-Search Keyword\n3-Exit\nChoice:")
    if secim == "3":
        print("You chose exit from the code.")
        break

    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            print("Popular Movies:")
            for movie in movies['results']:
                print(movie['title']) 
        elif secim == "2":
            keyword = input("Keyword: ") # enter the keyword you want to watch a movie about (example: 'Space')
            movies = movieApi.getSearch(keyword)
            print("Movies that you might interested:")
            for movie in movies['results']:
                print(movie['name']) # you will get movie's titles
# CNMALPS











