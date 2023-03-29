# ------------- WAVE 1 --------------------
# Wave 1



# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.

def create_movie(title, genre, rating):

    #for movie in title:

    movies = title, genre, rating
    if all(movies):
    #if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None


def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            watched.append(movie)
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

