from statistics import mean

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # validate_parameters (empty strings and zero evaluate to Falsy)
    if title and genre and rating:
        movie = {"title": title, "genre": genre, "rating": rating}
        return movie
    else:
        return None
    
user_data = {"watched": [], "watchlist": []}

def add_to_watched(user_data, movie):
    if movie:
        user_data["watched"].append(movie)
        return user_data

def add_to_watchlist(user_data, movie):
    if movie:
        user_data["watchlist"].append(movie)
        return user_data

def watch_movie(user_data, title):
    movie_found = False
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            movie_found = True
            break
    if not movie_found:
        return user_data
            
    return user_data

# ****** Waves 2, 3, 4, 5: should not modify user_data ******

def get_watched_avg_rating(user_data):
    for movie in user_data["watched"]:
        if movie["watched"] == []:
            average = 0.0
        else:
            average = mean(movie["rating"])
    return average


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

