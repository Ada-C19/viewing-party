# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # if the parameters are truthy; return dictionary
    # 3 keys: title, genre, rating

    #initialize empty dictionary 
    movie_ratings = {}

    #if any of parameters is Falsy, return None
    if not title or not genre or not rating:
        return None
    
    #otherwise, populate dictionary
    movie_ratings["title"] = title
    movie_ratings["genre"] = genre
    movie_ratings["rating"] = rating
    
    #return dictionary
    return movie_ratings


def add_to_watched(user_data, movie):
    user_data["watched"] = movie

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

