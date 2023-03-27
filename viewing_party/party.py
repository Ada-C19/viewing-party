# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    movie = {"title": title, 
            "genre": genre, 
            "rating": rating}
    
    return movie

def add_to_watched(user_data, movie):
    #check for potential duplicates
    if movie in user_data["watched"]:
        return user_data

    user_data["watched"].append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_most_watched_genre(user_data):
    if user_data["watched"] == []:
        return None
    
    genre_frequencies = {}

    for movie in user_data["watched"]:
        if movie["genre"] in genre_frequencies:
            genre_frequencies[movie["genre"]] += 1
        else:
            genre_frequencies[movie["genre"]] = 1
    
    return max(genre_frequencies, key=genre_frequencies.get)
 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

