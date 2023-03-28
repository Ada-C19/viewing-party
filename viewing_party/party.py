# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    movie={}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie ["rating"] = rating
        return movie
    else:
        return None 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie (user_data, title):
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watched"].append(movie) 
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_total = 0.0 

    if user_data["watched"] == []:
        return 0.0 
    
    for each_movie in user_data["watched"]:
        rating_total += each_movie["rating"]
        
    rating_average = rating_total/len(user_data["watched"])

    return rating_average
def get_most_watched_genre(user_data):

    frequency_dict = {}
    if user_data["watched"] == []:
        return None 
    
    for movie in user_data["watched"]:
        if movie['genre'] in frequency_dict:
            frequency_dict[movie['genre']] += 1
        else:
            frequency_dict[movie['genre']] = 1           
    winner = max(frequency_dict, key=frequency_dict.get)
    return winner


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

