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
   
    watchlist_value = user_data["watchlist"]
    watched_value = user_data["watched"]
    
    for item in watchlist_value:
        item_title = item["title"]
        if  title == item_title:
            watchlist_value.remove(item)
       
            watched_value.append(item)
            return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    try:
        number_of_movies = 0
        average_rating = 0.0
        for movie in user_data["watched"]: 
            average_rating += movie["rating"]
            number_of_movies += 1
 
        average_rating = average_rating / number_of_movies
        return average_rating
    except ZeroDivisionError:
        return 0.0


def get_most_watched_genre(user_data):
    counter_fantasy = 0
    counter_horror = 0
    counter_action = 0
    counter_intrigue = 0

    if user_data["watched"] == []:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] == "Fantasy":
            counter_fantasy += 1
        elif movie["genre"] == "Action":
            counter_action += 1
        elif movie["genre"] == "intrigue":
            counter_intrigue += 1
        elif movie["genre"] == "Horror":
            counter_horror += 1 

    if  counter_fantasy > counter_horror and counter_fantasy > counter_action and \
    counter_fantasy > counter_intrigue:
        return "Fantasy"
    
    elif counter_horror > counter_action and counter_horror > counter_intrigue and \
    counter_horror > counter_fantasy:
        return "Horror"
    
    elif  counter_action > counter_horror and counter_action > counter_fantasy and \
    counter_action > counter_intrigue:
        return "Action"
    
    elif  counter_action > counter_horror and counter_action > counter_fantasy and \
    counter_action > counter_intrigue:
        return "Action"
    
    elif  counter_intrigue > counter_horror and counter_intrigue > counter_fantasy and \
    counter_intrigue > counter_action:
        return "Intrigue"
                
def get_unique_watched(user_data):
    only_user_watched = []
    friends_watched =[]
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched.append(movie) 
 
    for movie in user_data["watched"]:
            if movie not in friends_watched:
                only_user_watched.append(movie)
    return only_user_watched   


def get_friends_unique_watched(user_data):
    only_friends_watched = []
    friends_watched =[]

    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched.append(movie)

    unique_movies = []
    for movie in friends_watched:
        if movie not in user_data["watched"] and movie not in unique_movies: 
            unique_movies.append(movie)

    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

