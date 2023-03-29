import copy

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None

    movie = {
        "title" : title, 
        "genre" : genre, 
        "rating" : rating
    }

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    new_user_data = {
        "watchlist" : user_data["watchlist"].copy(),
        "watched" : user_data["watched"].copy()
    }
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            new_user_data["watchlist"].remove(movie)
            new_user_data["watched"].append(movie)

    return new_user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_rating = 0
    watched_movies = user_data["watched"]

    if len(watched_movies) == 0: return 0.0

    for movie in watched_movies:
        sum_rating += movie["rating"]
    average_rating = sum_rating / len(watched_movies)

    return average_rating

def get_most_watched_genre(user_data):
    genre_dict = {}
    highest_num = 0
    highest_genre = ""
    watched_movies = user_data["watched"]

    if len(watched_movies) == 0: return None

    for movie in watched_movies:
        if movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
        else:
            genre_dict[movie["genre"]] = 1

    for genre, num in genre_dict.items():
        if num > highest_num:
            highest_num = num
            highest_genre = genre
    
    return highest_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friend_movies(friend_list):
    friend_watched_movies = []

    for movies in friend_list:
        for movie in movies["watched"]:
            friend_watched_movies.append(movie)
    
    return friend_watched_movies

def get_unique_watched(user_data):
    watched_movies = user_data["watched"].copy()
    friend_watched_movies = get_friend_movies(user_data["friends"])
    not_watched_by_friends = []

    fw_copy = friend_watched_movies.copy()

    for movie in watched_movies:
        if movie not in friend_watched_movies:
            not_watched_by_friends.append(movie)

    return not_watched_by_friends

def get_friends_unique_watched(user_data):
    watched_movies = user_data["watched"].copy()
    friend_watched_movies = get_friend_movies(user_data["friends"])
    not_watched_by_user = []
    
    for movies in user_data["friends"]:
        for movie in movies["watched"]:
            friend_watched_movies.append(movie)

    fw_copy = friend_watched_movies.copy()

    for movie in friend_watched_movies:
        if movie not in watched_movies and movie not in not_watched_by_user:
            not_watched_by_user.append(movie)   

    return not_watched_by_user


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    friend_watch = get_friend_movies(user_data["friends"])

    if len(user_data["watched"]) == 0 or len(friend_watch) == 0:
        return []

    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_user_genre(movie_list):
    user_genre = {}

    if not movie_list:
        return None

    for movie in movie_list:
        if movie["genre"] not in user_genre:
            user_genre[movie["genre"]] = 1
        else:
            user_genre[movie["genre"]] += 1

    most_common_genre = max(user_genre, key=user_genre.get)

    return most_common_genre

def get_new_rec_by_genre(user_data):
    recommended_movies_genre = []
    most_common_genre = get_user_genre(user_data["watched"])
    available_recs = get_available_recs(user_data)
    friend_watch = get_friend_movies(user_data["friends"])

    if len(user_data["watched"]) == 0 or len(friend_watch) ==0:
        return []

    for movie in available_recs:
        if movie["genre"] == most_common_genre:
            recommended_movies_genre.append(movie)

    return recommended_movies_genre

def get_rec_from_favorites(user_data):
    recommended_movies_fav = []
    friend_watch = get_friend_movies(user_data["friends"])

    for movie in user_data["favorites"]:
        if movie not in friend_watch:
            recommended_movies_fav.append(movie)
    
    return recommended_movies_fav
