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

#4th funcyion in wave_01
def watch_movie(user_data, title):
    index = 0
    for index in range(len(user_data["watchlist"])):
        if title in (user_data["watchlist"][index]["title"]):
            move_movie = user_data["watchlist"].pop(index)
            #to move to end of list
            user_data["watched"].append(move_movie)
            #to move to begiiniing of list
            # user_data["watched"].insert(0, move_movie)
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

