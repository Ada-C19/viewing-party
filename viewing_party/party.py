# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    # if not title or genre or rating...find how to use if not?:
    if title == None or genre == None or rating == None:
        return None
    else:
        movie_dict["title"]= title
        movie_dict["genre"]= genre
        movie_dict["rating"]= rating
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data  

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        # if not title in movie["title"]:
        #     return user_data
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
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

