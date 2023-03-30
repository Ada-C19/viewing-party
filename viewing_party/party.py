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

user_data = {"watched":[{"title":"meep","genre":"horror","rating":5},{"title":"Ghost","genre":"horror","rating":5},{"title":"Hehe","genre":"horror","rating":5}], "friends": [{"watched":[{"title":"Bionicles"},{"title":"Ghost"}, {"title":"Paranormal"} ]},{"watched":[{"title":"Bionicles"},{"title":"Paranormal"}]}]}
def get_unique_watched(user_data):
    unique_movies = []
    friends_watched_set = set()
    user_watched_set = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_set.add(movie["title"])

    for i in range(len(user_data["watched"])):
        user_watched_set.add(user_data["watched"][i]["title"])

    differences = user_watched_set.difference(friends_watched_set)
    
    for i in user_data["watched"]:
        if i["title"] in differences:
            unique_movies.append(i)
    return unique_movies

user_data = {"watched":[{"title":"meep","genre":"horror","rating":5},{"title":"Ghost","genre":"horror","rating":5},{"title":"Hehe","genre":"horror","rating":5}], "friends": [{"watched":[{"title":"Bionicles"},{"title":"Ghost"}, {"title":"Paranormal"} ]},{"watched":[{"title":"Bionicles"},{"title":"Paranormal"}]}]}
def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    friends_watched_set = set()
    user_watched_set = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_set.add(movie["title"])

    for i in range(len(user_data["watched"])):
        user_watched_set.add(user_data["watched"][i]["title"])

    differences = friends_watched_set.difference(user_watched_set)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in differences and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
                continue
    return friends_unique_watched



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

friends_unique_watched = [{"title": "Paranormal Activity"}, {"title": "Lord of the Rings"}]
user_unique_watched = [{'title': 'meep', 'genre': 'horror', 'rating': 5}, {'title': 'Hehe', 'genre': 'horror', 'rating': 5}]
user_data = {
        "subscriptions": ["hulu", "disney+"],
        "watched": [],
        "friends": [
            {
                "watched": [{"title": "Paranormal Activity","genre":"horror","rating": 5,"host":"Netflix"}]
            },
            {
                "watched": [{"title": "Lord of the Rings","genre":"fantasy","rating": 4, "host":"hulu"}]
            }
        ]
    }
def get_available_recs(user_data):
    user_unique_watched = get_unique_watched(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    recommended_movies = []
    for watchlist in user_data["friends"]:
        for movie in watchlist["watched"]:
            if movie["host"] in user_data["subscriptions"] and (movie in friends_unique_watched and movie not in recommended_movies):
                recommended_movies.append(movie)
                    
                    
    print(recommended_movies)
    return recommended_movies
            # if recommended movie in friends_unique_watched,


    print(recommended_movies)
        # if movie's subscription is in user_data subscriptions list
        
        # append movie title to recommended_movies
get_available_recs(user_data)

#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies

# for i in range(len(user_data["friends"])):
#    if movie in user_data["freinds"][i]:


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

