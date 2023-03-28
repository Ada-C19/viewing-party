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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

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

