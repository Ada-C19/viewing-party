import statistics
from statistics import mode
from frozendict import frozendict

# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        return {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
    
    return None

# user data is a dict and it has a key "watched" --> list 
# add movie to this list 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
        
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    
    running_total = 0
    for movie in user_data["watched"]:
        running_total += movie["rating"]

    return running_total / len(user_data["watched"])


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_list = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])

    return mode(genre_list)

    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_titles_user_watched(user_data):
    movies_user_watched = set()

    for movie in user_data["watched"]:
        movies_user_watched.add(movie["title"])

    return movies_user_watched


def get_titles_friends_watched(user_data):
    movies_friends_have_watched = set()

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movies_friends_have_watched.add(movie["title"])

    return movies_friends_have_watched


def get_unique_watched(user_data):
    titles_friends_have_watched = get_titles_friends_watched(user_data)

    movies_only_user_watched = []
    for movie in user_data["watched"]:
        if movie["title"] not in titles_friends_have_watched:
            movies_only_user_watched.append(movie)


    return movies_only_user_watched



def get_friends_unique_watched(user_data):
    titles_user_watched = get_titles_user_watched(user_data)

    movies_only_friends_watched = []


    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in titles_user_watched:
                movies_only_friends_watched.append(frozendict(movie))


    return list(set(movies_only_friends_watched))
    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    subscriptions_set = set(user_data["subscriptions"])
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:
        if movie["host"] in subscriptions_set:
            recommended_movies.append(movie)

    return recommended_movies


# # -----------------------------------------
# # ------------- WAVE 5 --------------------
# # -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommended = set()
    favorite_genre = get_most_watched_genre(user_data)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == favorite_genre:
                recommended.add(frozendict(movie))

    return list(recommended)

def get_rec_from_favorites(user_data):
    recommended = []
    unique_watched = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in unique_watched:
            recommended.append(movie)

    return recommended

