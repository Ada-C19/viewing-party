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

