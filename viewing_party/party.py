# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    movie_ratings = {}

    if not title or not genre or not rating:
        return None
    
    movie_ratings["title"] = title
    movie_ratings["genre"] = genre
    movie_ratings["rating"] = rating
    
    return movie_ratings


def add_to_watched(user_data, movie):

    watched = user_data["watched"]
    watched.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    watch_list = user_data["watchlist"]
    watch_list.append(movie)

    return user_data

def watch_movie(user_data, title):
    # list of dictionaries(each dictionary has title, genre, rating)
    watch_list = user_data["watchlist"]
    # list of watched movies
    watched = user_data["watched"]

    for movie in watch_list:
        if title in movie["title"]:
            watch_list.remove(movie)
            watched.append(movie)   
    
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

