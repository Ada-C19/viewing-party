# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # Input validation
    if not title or not genre or not rating:
        return None
    
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # Return the dictionary
    return movie

def add_to_watched(user_data, movie):
    movie_data = {
        "watched": []
    }

    movie_data["watched"].append(movie)
    return movie_data

def add_to_watchlist(user_data, movie):

    if not movie:
        return user_data
    
    user_data["watchlist"].append(movie)
    
    return user_data
print(add_to_watchlist({"watchlist": ["FANTASY_2"]}, {"title": "MOVIE_TITLE_1", "genre": "GENRE_1",
        "rating": "RATING_1"}))
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

