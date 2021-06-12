import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "854f95b699d723d78c2982e3742a32f1"
    
    def getPopulars(self):
        response1 = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response1.json() # dönen bilgiyi dict'e çevrildi
    
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
                print(movie['title']) # filmlerin sadece isimleri 'title' (başlıkları) gelecek.
        elif secim == "2":
            keyword = input("Keyword: ") # hakkında film izlemek istediğin anahtar kelime gir (example: 'Avrupa' :) )
            movies = movieApi.getSearch(keyword)
            print("Movies that you might interested:")
            for movie in movies['results']:
                print(movie['name']) # filmlerin sadece isimleri 'title' (başlıkları) gelecek.












