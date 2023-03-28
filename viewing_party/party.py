# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if check_invalid_movies(title, genre, rating) is True:
        movie = {"title": title, "genre": genre, "rating": rating}
        return movie
    
def check_invalid_movies(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    return True
    
def add_to_watched(user_data, movie):
     user_data["watched"].append(movie)
     return user_data
 
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #add_to_watched(user_data,)
    watchlist_value = user_data["watchlist"]
    watched_value = user_data["watched"]
    
    for item in watchlist_value:
        item_title = item["title"]
        if  title == item_title:
            watchlist_value.remove(item)
       
            watched_value.append(item)
            return user_data
        else:
            return user_data
    
    #user_data = {"watchlist": [new_movie], "watched": [watched_movie]}
    #title = ""
    # if title != str:
    #     return None
    #elif title in user_data["watchlist"][0]["title"]:
    # for index in len(user_data["watchlist"]):
    #     if title in user_data["watchlist"][index]["title"]:
    #         user_data["watchlist"].pop(index)
    #         #user_data["wacthlist"].remove(title)
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

