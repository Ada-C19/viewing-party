# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # if the parameters are truthy; return dictionary
    # 3 keys: title, genre, rating

    #if any of the parameters is Falsy,...
    if title == False or genre == False or rating == False:
        #...then return None
        return None
    
    #initialize empty dictionary
    movie_ratings = {}

    if title == False or genre == False or rating == False:
        return None

    
    movie_ratings["title"] = title
    movie_ratings["genre"] = genre
    movie_ratings["rating"] = rating

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

