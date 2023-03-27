# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        return {"title": title, 
                "genre": genre,
                "rating": rating}
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    print(user_data)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data['watchlist']
    watched = user_data['watched']
    for movie in watchlist:
        if movie['title'] == title:
            #remove from watchlist
            watched.append(movie)
            #add to watched
            watchlist.remove(movie)
            print(watchlist)
    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    average = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]: 
        sum += movie["rating"]
    average = sum / len(user_data["watched"])
    return average
#

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

