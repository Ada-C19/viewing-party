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

def get_most_watched_genre(user_data):
    frequency_counter = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in frequency_counter:
            frequency_counter[movie["genre"]] = 1
        else:
            frequency_counter[movie["genre"]] += 1
    mode = 0
    mode_genre = ""
    for genre_name, genre_frequency in frequency_counter.items():
        if genre_frequency > mode:
            mode = genre_frequency
            mode_genre = genre_name
    return mode_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

