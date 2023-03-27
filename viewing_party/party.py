# ------------- WAVE 1 --------------------
import copy
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating    }
    return movie    

def add_to_watched(user_data, movie):
    user_data_copy = copy.deepcopy(user_data)
    user_data_copy["watched"].append(movie)
    return user_data_copy



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

