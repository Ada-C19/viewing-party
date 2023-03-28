# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
   
    user_data = {}
    
    if bool(title) and bool(genre) and bool(rating) == True:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating

        return movie_dict

    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    
    return user_data    
 
        

    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    
    return user_data  

def watch_movie(user_data, title):
    if title in user_data:
        user_data["watchlist"]["title"].remove(title)
        user_data["watched"].append(title)
    else:
        user_data["watchlist"].append(title)

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

