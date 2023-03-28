# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {}
    if not (title and genre and rating):
        return None 
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating 
    return new_movie
    

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    if title in user_data['watchlist']:
        user_data['watched'].append(title)
        user_data['watchlist'].remove(title)
        # return user_data
    return user_data
# we need to work on it tomorrow

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

