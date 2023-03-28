# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
            }
    
    return None

def add_to_watched(user_data, movie):
    if movie not in user_data.get("watched"):
        user_data.get("watched").append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    if movie not in user_data.get("watchlist"):
        user_data.get("watchlist").append(movie)

    return user_data

def watch_movie(user_data, title):
    movies = user_data.get("watchlist")

    for movie in movies:
        if title == movie["title"]:
            movies.remove(movie)
            user_data.get("watched").append(movie)
    
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

