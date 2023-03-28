# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None

    else:
        new_movie['title'] = title
        new_movie['genre'] = genre
        new_movie['rating'] = rating
    return new_movie

def add_to_watched(user_data, movie):
    for data in user_data:
        user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    for data in user_data:
        user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for user in user_data["watchlist"]:
        if user["title"] == title:
            user_data["watchlist"].remove(user)
            user_data["watched"].append(user)

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

