# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if check_invalid_inputs(title, genre, rating) is True:
        
        movie = {"title": title, "genre": genre, "rating": rating}
        return movie
    
def check_invalid_inputs(title, genre, rating):
    if (title, genre, rating) == None:
        return None
    return True
     
        
    
# def add_to_watched(user_data, movie):
#      watched_movie = movie
#      user_data = {"watched": [watched_movie]}
#      return user_data
 
# def add_to_watchlist(user_data, movie):
#     new_movie = movie
#     user_data = {"watchlist": [new_movie]}
#     return user_data

# def watch_movie(user_data, title):
#     add_to_watched(user_data,)
    
#     user_data = {"watchlist": [new_movie], "watched": [watched_movie]}
#     title = ""
#     if title != str:
#         return None
#     elif title in user_data["watchlist"]:
#         user_data["wacthlist"].remove(title)
#         user_data["watched"].append(title)
#         return user_data
#     else:
#         return user_data 
        
        
        
        
    
    
     
      
     
        
    

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

