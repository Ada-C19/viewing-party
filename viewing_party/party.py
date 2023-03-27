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

# print(create_movie("Seahawks", "sportsball", 1))

def add_to_watched(user_data, movie):
    user_data = {
        "watched": []
    }

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

