# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        return {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
    
    return None


# user data is a dict and it has a key "watched" --> list 
# add movie to this list 

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
        
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    
    running_total = 0
    for movie in user_data["watched"]:
        running_total += movie["rating"]

    return running_total / len(user_data["watched"])
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

