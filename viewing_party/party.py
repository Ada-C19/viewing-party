# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {"title":title, "genre": genre, "rating": rating}
    else:
        return None

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
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    """
    user_data: dict with "watched" list of dictionaries and "friends" list of dictionaries
    """

    # Create list of all friends' watched movies
    friends_watched = []
    for friend in user_data["friends"]:
        friends_watched += friend["watched"]
    
    # Create list of movies that only user_data has watched
    unique_watched = []
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_watched.append(movie)
    
    return unique_watched
    
def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    
    return friends_unique_watched

            
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genres = []
    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    # Determine most frequent genre from watched list   
    try:
        fav_genre = max(genres, key=genres.count)
    # Capture exception for when user_data's watched list is empty
    except ValueError:
        fav_genre = None

    movie_recs = []
    # Create a list of all the movies friends have watched that user_data has not
    friends_movies = get_friends_unique_watched(user_data)
    
    for movie in friends_movies:
        if movie["genre"] == fav_genre:
            movie_recs.append(movie)
    
    return movie_recs

def get_rec_from_favorites(user_data):
    # Create list of movies only watched by user, not by friends
    friends_not_watched = get_unique_watched(user_data)
    
    # Create list of movies from favorites that have not been watched by friends
    fav_movie_recs = [movie for movie in user_data["favorites"] if movie in friends_not_watched]
 
    return fav_movie_recs


# ------------- WAVE 1 --------------------

# def create_movie(title, genre, rating):
#     pass

# If parameters title, genre, rating are all truthy:
# Return a dictionary with: 3 key-value pairs 
# If title, genre, and rating are falsy: return NONE


# def add_to_watched(user_data, movie):
#     pass
# Dictionary of list of dictionaries
# Value of user_data is a dictionary with key: "watched", value is a list of dictionary with movies watched
# Empty list --> no movies in watched list
#     user_data = {
#        "watched": [movie]
#    }
# How can I add to the "watched" list?
# add "movie" to the watched list inside of user_data
# return user data


# def add_to_watchlist(user_data, movie):
#     pass

# Dictionary of list of dictionaries
# Value of user_data is a dictionary with key: "watchlist", value is a list of dictionary with movies watched
# Empty list --> no movies in watched list
# my_watchlist_dict = {
# "watchlist:" [
#      {
#        "title": "Title A",
#        "genre": "Horror",
#        "rating": 3.5
#      }
#            ]
# }

# add "movie" to the watchlist list inside of user_data
# return user data

# def watch_movie(user_data, title):
#     pass
# The value of user_data is a dictonary with "watchlist" and "watched" -Keys
# Value of keys is a list of the watchlist and list of watched movies
# 

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

