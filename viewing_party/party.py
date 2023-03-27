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

def get_unique_watched(user_data):
    watched = user_data["watched"]
    friends = user_data["friends"]
    if not watched: return []

    #Make list of all movies watched by friends (dupes ok)
    friend_watched = []
    for friend in friends:
        friend_watched.extend(friend["watched"])

    #Compare own watched movies to friends' watched movies
    unique_movies = []
    for movie in watched:
        if movie not in friend_watched:
            unique_movies.append(movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    watched = user_data["watched"]
    friends = user_data["friends"]
    if not watched: return []

    #Make list of all movies watched by friends (dupes ok?)
    friend_watched = []
    for friend in friends:
        friend_watched.extend(friend["watched"])

    #Compare friends' watched movies to own watched movies
    friend_unique_movies = []
    for movie in friend_watched:
        if movie not in watched and movie not in friend_unique_movies:
            friend_unique_movies.append(movie)
    return friend_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

