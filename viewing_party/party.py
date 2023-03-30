# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        new_movie = None
    else:
        new_movie = {"title": title, "genre": genre, "rating": rating}
    return new_movie

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    user_data["watched"] = watched_list  
        
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    user_data["watchlist"] = watchlist  

    return user_data

def watch_movie(user_data, movie):
    # look up movie in watchlist
    tracker_dict = None
    for movie_dict in user_data["watchlist"]:
        if movie == movie_dict["title"]:
            add_to_watched(user_data, movie_dict)
            tracker_dict = movie_dict
    if tracker_dict:
        user_data["watchlist"].remove(tracker_dict)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data): 
    sum = 0 

    if len(user_data["watched"]) != 0:
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"]
        average_rating = sum / len(user_data["watched"])
        return average_rating
    
    else:
        return 0.0
    #access watched and sum key values in list
    #take sum of key values of rating and divide by len of 

def get_most_watched_genre(user_data):
    genre_list = []
    counter = 0

    if len(user_data["watched"]) == 0:
        return None
    
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"]) 
        for i in genre_list:
            frequency = genre_list.count(i)
            if (frequency > counter):
                counter = frequency
                genre = i
                
    return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # initialize empty set
    friends_movies = set()
    unique_movies = []
    # loop through the movies in watched
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # add movies to a set
            friends_movies.add(movie["title"])    # return the set
    # for all movies in user_data friends
    # for friend in user_data["friends"]:
    #     for i in range(len(friend["watched"])):
            
    #         # if movie title not in unique movies
    #         if friend["watched"][i]["title"] not in unique_movies:
    #             # add movie dict to unique movies
    #             unique_movies.append(friend["watched"][i])
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movies:
            unique_movies.append(movie)
            

    return unique_movies    

    


    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
