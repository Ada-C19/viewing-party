# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    movie = {
        "title" : title,
        "genre" : genre,
        "rating" : rating
    }

    if not title or not genre or not rating:
        return None
    
    return movie

def add_to_watched(user_data, movie):
    '''GOAL: passing in user_data and movie
    add movie to user_data
    
    append dictionary to list of watched'''
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

