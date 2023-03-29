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
    tracker_dict = None
    for movie_dict in user_data["watchlist"]:
        if movie == movie_dict["title"]:
            add_to_watched(user_data, movie_dict)
            tracker_dict = movie_dict
    if tracker_dict:
        user_data["watchlist"].remove(tracker_dict)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data): 
    user_data["watched"]
    #access watched and sum key values in list
    #take sum of key values of rating and divide by len of 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

