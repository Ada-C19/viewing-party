from collections import Counter
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None  or rating == None:
        movie_dict = None
    else:
        movie_dict = {"title":title,"genre":genre,"rating":rating}
    return movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

user_data = {"watchlist":[{"title": "lord of rings", "genre" : "horrpr","rating": 5}]}
movie = {"title" : "game of thrones","genre":"fantasy","rating":5}
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

user_input = {"watchlist":[{"title": "harry potter", "genre" : "horrpr","rating": 5},{"title": "lord of rings", "genre" : "horrpr","rating": 5}],"watched":[]}

def watch_movie(user_data, title):
    for index in range(len(user_data["watchlist"])):
        if title in user_data["watchlist"][index].values():
            res = user_data["watched"].insert(0, user_data["watchlist"].pop(index))
            # print(user_data["watchlist"])
            # print(user_data["watched"])
        else:
            continue
    return user_data  
# title = "lord of rings"
# watch_movie(user_input,title)



# -----------------------------------------
# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    # could make simpler using counter import
    average_rate = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie_dict in user_data["watched"]:
        average_rate += movie_dict["rating"]
    count = len(user_data["watched"])

    rate = average_rate / count
    print(rate)
    return rate
    
# user_data = {"watched":[{"title":"Ghost","genre":"horror","rating":5}, {"title":"The well","genre":"horror","rating":3}]}
user_data = {"watched":[{"title":"Ghost","genre":"horror","rating":5},{"title":"Ghost","genre":"horror","rating":5},{"title":"The well","genre":"horror","rating":3},{"title":"Wednesday","genre":"comedy","rating":5},{"title":"Wednesday","genre":"comedy","rating":5},{"title":"The car","genre":"horror","rating":3}]}

# get_watched_avg_rating(user_data)
def get_most_watched_genre(user_data):
    
    if user_data["watched"] == []:
        return None
    else: 
        genres_dict = {}

        for index in range(len(user_data["watched"])):
            genre = user_data["watched"][index]["genre"]
            if genre in genres_dict:
                genres_dict[genre] += 1
            else:
                genres_dict[genre] = 1

        most_popular = max(genres_dict, key = genres_dict.get)

        return most_popular

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

