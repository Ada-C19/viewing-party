# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return 

def add_to_watched(user_data, movie):
    if not movie:
        return user_data
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if not movie:
        return user_data
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for watchlist_movie in user_data["watchlist"]:
        if title == watchlist_movie["title"]:
            user_data["watched"].append(watchlist_movie)
            user_data["watchlist"].remove(watchlist_movie)
            return user_data
    return user_data 

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    if not watched: return 0

    return sum(watched[i]["rating"] for i in range(len(watched))) / len(watched)

def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    if not watched: return None
    
    genre_list = [watched[i]["genre"] for i in range(len(watched))]
    return max(genre_list, key=genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friend_movies(user_data):
    #Return list of movies watched by friends (no duplicates)
    friend_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_watched: friend_watched.append(movie)
    return friend_watched

def create_unique_list(movies, comparison):
    unique_movies = []
    for movie in movies:
        if movie not in comparison: unique_movies.append(movie)
    return unique_movies

def get_unique_watched(user_data):
    watched = user_data["watched"]
    if not watched: return []

    friend_watched = get_friend_movies(user_data)

    #Compare own watched movies to friends' watched movies
    return create_unique_list(watched, friend_watched)

def get_friends_unique_watched(user_data):
    watched = user_data["watched"]
    if not watched: return []

    friend_watched = get_friend_movies(user_data)

    #Compare friends' watched movies to own watched movies
    return(create_unique_list(friend_watched, watched))

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    for movie in get_friend_movies(user_data):
        if movie["host"] in user_data["subscriptions"] and movie not in user_data["watched"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    watched = user_data["watched"]
    if not watched: return []

    fave_genre = get_most_watched_genre(user_data)
    friend_movies = get_friend_movies(user_data)

    recommended_movies = []
    for movie in friend_movies:
        if movie not in watched and movie["genre"] == fave_genre: 
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    if not favorites: return []

    friend_movies = get_friend_movies(user_data)
    
    recommended_movies = []
    for movie in favorites:
        if movie not in friend_movies: recommended_movies.append(movie)
    return recommended_movies