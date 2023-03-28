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

def add_to_watchlist(user_data, movie):
    if movie in user_data["watchlist"]:
        return user_data
    user_data["watchlist"].append(movie)
    return user_data 

def watch_movie(user_data, title):
    watched = user_data["watched"]
    watchlist = user_data["watchlist"]
    for i in range(len(watchlist)):
        if watchlist[i]["title"] == title:
            del watchlist[i]
            watched.append(watchlist[i])
        
    return user_data 

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    sum = 0.0
    for movie in user_data["watched"]:
        sum += movie["rating"]
    avg_rating = sum / len(user_data["watched"])
    return avg_rating

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
def get_unique_watched(user_data):
    my_movie_list = []
    for i in range(0,len(user_data["watched"])):
	    my_movie_list.append(user_data["watched"][i])
    
    friend_movie_list = []
    for i in range(0,len(user_data["friends"])):
	    for j in range(0,len(user_data["friends"][i]["watched"])):
		    friend_movie_list.append(user_data["friends"][i]["watched"][j])

    unique_movies = []
    for movie in my_movie_list:
	    if movie not in friend_movie_list:
		    unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    my_movie_list = []
    for i in range(0,len(user_data["watched"])):
	    my_movie_list.append(user_data["watched"][i])
    
    friend_movie_list = []
    for i in range(0,len(user_data["friends"])):
	    for j in range(0,len(user_data["friends"][i]["watched"])):
		    friend_movie_list.append(user_data["friends"][i]["watched"][j])

    unique_movies = []
    for movie in friend_movie_list:
	    if movie not in my_movie_list and movie not in unique_movies:
		    unique_movies.append(movie)

    return unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

