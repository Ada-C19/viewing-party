# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    if not watched: return 0

    return sum([watched[i]["rating"] for i in range(len(watched))]) / len(watched)

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

def get_unique_watched(user_data):
    watched = user_data["watched"]
    if not watched: return []

    friend_watched = get_friend_movies(user_data)

    #Compare own watched movies to friends' watched movies
    unique_movies = []
    for movie in watched:
        if movie not in friend_watched: unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    watched = user_data["watched"]
    if not watched: return []

    friend_watched = get_friend_movies(user_data)

    #Compare friends' watched movies to own watched movies
    friend_unique_movies = []
    for movie in friend_watched:
        if movie not in watched: friend_unique_movies.append(movie)
    return friend_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

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