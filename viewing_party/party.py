# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not title or not genre or not rating:
        return None
        
    movie = {
        "title": title, 
        "genre": genre,
        "rating": rating
    }
    return movie

def add_to_watched(user_data, movie):

    # Check movie isn't empty and is a dictionary
    if movie and isinstance(movie, dict):
        user_data["watched"].append(movie)
    
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

