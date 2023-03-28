# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        new_movie = None
    else:
        new_movie = {"title": title, "genre": genre, "rating": rating}
    return new_movie

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    user_data["watched"] = watched_list  
        
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    user_data["watchlist"] = watchlist  

    return user_data

def watch_movie(user_data, movie):
    # look up movie in watchlist
    tracker_dict = {}
    for movie_dict in user_data["watchlist"]:
        if movie == movie_dict["title"]:
            tracker_dict = movie_dict
        else:
            return user_data
    # reassign movie dictionary to watchedlist
    user_data["watched"].append(tracker_dict)

    # iterate through index of watchlist
    index = 0
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i] == tracker_dict:
            index = i

    user_data["watchlist"].pop(index)

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

