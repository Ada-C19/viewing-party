import statistics
from statistics import mode

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
def get_unique_watched(user_data):
    user_watched_movies = {movie['title']: movie for movie in user_data['watched']}
    friends_watched_movies = set()

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_movies.add(movie['title'])

    unique_watched_movies = set(user_watched_movies.keys()).difference(friends_watched_movies)
    return [user_watched_movies[movie] for movie in unique_watched_movies]


def get_friends_unique_watched(user_data):
    user_watched_movies = {movie['title']: movie for movie in user_data['watched']}
    friends_watched_movies = {}

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_movies[movie['title']] = movie

    unique_friends_watched_movies = set(friends_watched_movies.keys()).difference(user_watched_movies.keys())
    return [friends_watched_movies[movie] for movie in unique_friends_watched_movies]

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_watched_movies = {movie['title']: movie for movie in user_data['watched']}
    friends_watched_movies = {}

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_movies[movie['title']] = movie

    unique_friends_watched_movies = set(friends_watched_movies.keys()).difference(user_watched_movies.keys())
    available_movies = [friends_watched_movies[movie] for movie in unique_friends_watched_movies if friends_watched_movies[movie]['host'] in user_data['subscriptions']]
    
    return available_movies


# # -----------------------------------------
# # ------------- WAVE 5 --------------------
# # -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended = []
    favorite_genre = get_most_watched_genre(user_data)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == favorite_genre:
                recommended.append(movie)
    print(recommended)
    return recommended

def get_rec_from_favorites(user_data):
    recommended = []
    for movie in user_data["favorites"]:
        if movie not in user_data["friends"]["watched"]:
            recommended.append(movie)
    return recommended