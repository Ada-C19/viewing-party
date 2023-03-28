# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if title != None and genre != None and rating != None:
        movies= {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movies
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


    # user_data = {
    #     "watched": [
    #         movie
    #         ]
    #     }

    # user_data["watched"] += movie
    # print(user_data)

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    #we want to move the movies (title, genre, rating) into the user_data["watch"]

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_avg_rating = 0.0

    if len(user_data["watched"]) == 0:
        return sum_avg_rating
    else:
        for movie in user_data["watched"]:
            sum_avg_rating += movie["rating"]
            avg_rating = sum_avg_rating / len(user_data["watched"])
        return avg_rating
    
def get_most_watched_genre(user_data):
    freq = {}
    highest_count = 0

    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] in freq:
            freq[movie["genre"]] += 1
        else: 
            freq[movie["genre"]]= 1

    for genre, count in freq.items():
        if count > highest_count:
            highest_count = count
            highest_genre = genre
    return highest_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# 1. Create a function named `get_unique_watched`. This function should...
# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. 
#   Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies
def get_unique_watched(user_data):
    unique_movie = []
    friends_watched = user_data["friends"]
    friend_watch_list= []
    user_watched = user_data["watched"]
    # print()
    # print("Friends watched List: ", friends_watched)
    # print()
    # print("My watched list: ", user_watched)

    for friends in friends_watched:
        for movie in friends["watched"]:
            if movie["title"] not in friend_watch_list:
                friend_watch_list.append(movie["title"])
    
    for user_movie in user_watched:
        if user_movie["title"] not in friend_watch_list:
            unique_movie.append(user_movie)
    print("unique_movies", unique_movie)
    return unique_movie



# 2. Create a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. 
# Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies

def get_friends_unique_watched(user_data):
    unique_movie = []
    friends_watched = user_data["friends"]
    user_watched_list_titles= []
    user_watched = user_data["watched"]
    friends_watched_list_title = []
    # print(friends_watched)
    # print(user_watched)

    for user_movie in user_watched:
        user_watched_list_titles.append(user_movie["title"])
    
    for friends in friends_watched:
        for movie in friends["watched"]:
            if movie["title"] not in user_watched_list_titles and movie["title"] not in friends_watched_list_title:
                friends_watched_list_title.append(movie["title"])
                unique_movie.append(movie)
                
    # print("unique_movies", unique_movie)
    return unique_movie

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# 1. Create a function named `get_available_recs`. This function should...

def get_available_recs(user_data):
    print("*********************")
    print("Wave 4 User Data: ", user_data)
    print("*********************")

# - take one parameter: `user_data`
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies

    user_not_watched = get_friends_unique_watched(user_data)
    list_of_rec_movies = []
    # print("User Not Watch List: ", user_not_watched)
    # print("*********************")
    for movie in user_not_watched:
        if movie["host"] in user_data["subscriptions"]:
            list_of_rec_movies.append(movie)
    
    # print("List of Rec Movies: ", list_of_rec_movies)
    return list_of_rec_movies

    # match movie title key to the title key of user_not_watched 
    # check for value in key 'host' is found in the value of subscription 

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

