# ------------- WAVE 1 --------------------
# 1st function in wave_01
def create_movie(title, genre, rating):
    movie = {}

    # checks to see if all values are truthy
    if title and genre and rating: 
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

    return None
# 2nd function in wave_01
def add_to_watched(user_data, movie):      
    user_data["watched"].append(movie)
    return user_data

# 3rd function in wave_01
def add_to_watchlist(user_data, movie): 

    user_data["watchlist"].append(movie)
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

