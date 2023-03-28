# ------------- WAVE 1 -------------------- 

# ========================================= wave 01- # 1. add to watched ==========

def create_movie(title, genre, rating):
    # movies = {}
    
    # If those three attributes are truthy, 
    # then return a dictionary. 
    # This dictionary should...
    if title and genre and rating:
        # movies.update(new_movies)
        return {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    else:
    # - If `title` is falsy, `genre` is falsy, 
    # or `rating` is falsy, this function should return `None`
        return None
    # return movies

# ========================================= wave 01- # 2. add to watched ==========

# Create a function named `add_to_watched`. This function should...
# take two parameters: `user_data`, `movie`
def add_to_watched(user_data, movie):
#   - the value of `user_data` will be a dictionary with a key 
# `"watched"`, and a value which is a list of dictionaries representing 
# the movies the user has watched
    user_data["watched"] = movie
    if user_data:
        user_data["watched"].update(movie)
    else:
        return None

# 3. Create a function named `add_to_watchlist`. This function should...take two parameters: `user_data`, `movie`
def add_to_watchlist(user_data, movie):
#   - the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value which is a list of dictionaries representing the movies the user wants to watch
    user_data["watchlist"] = movie
    if user_data:
        user_data["watchlist"].update(movie)
        return user_data
    # return An empty list represents that the user has no movies in their watchlist
    else:
        return None

# take two parameters: user_data, movie 
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    # print(user_data)
    return user_data

# ========================================= wave 01- # 3. add to watchlist ==========
# take two parameters: user_data, movie

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
        
def watch_movie(user_data, title):
    # - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`   
    # This represents that the user has a watchlist and a list of watched movies
    # The value of `title` will be a string
    # This represents the title of the movie the user has watched
    for movie in user_data["watchlist"]:
    # - If the title is in a movie in the user's watchlist:
        # if
        # remove that movie from the watchlist
        user_data["watchlist"].pop(movie)
        # add that movie to watched
        user_data["watched"].append(movie)
        # return the `user_data`
        return user_data
    # - If the title is not a movie in the user's watchlist:
        # else:
            # return the `user_data`    
            # return user_data
# ========================================= wave 01- # 4. watch movie ==========

def watch_movie(user_data, title):
    # if there's a movie dictionary in watchlist with the title fleabag, remove it from watchlist and add it to watched
    for movie in user_data["watchlist"]:
    # check the title for each element
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            print(user_data)  
            return user_data
    if title not in user_data["watchlist"]:
        return user_data
            
    # user_data= {
    #     "watchlist": [{"title": "A movie title", "genre": "A movie genre", "rating": "soem number"}],
        
    #     "watched" : [{"title": "A movie title", "genre": "A movie genre", "rating": "soem number"}] 
    #     }
    
    # user_data is a dict that contains 2 keys: watchlist and watched
    
    # movie is a ditionary format contained in both watched and watchlist
    
    # each movie dictionary has a key named "title"
    
    # the parameter title is a value, associated with the key "title"
def watch_movie(user_data, title):
    
    for movie in user_data["watchlist"]: 
        
        if title == movie["title"]:
            # remove that movie dictionary from the watchlist
            user_data["watchlist"].remove(movie)

            # add the movie dictionary to the the watched
            user_data["watched"].append(movie)
            
            #then return user data
            # print(user_data)
            return user_data
            
            # else, if the title is not a movie in the user's watchlist, 
            # return the user_data
    else: 
        return user_data
            
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched = user_data.get("watched", [])
    if not watched:
        return 0.0
    total_ratings = sum(movie.get("rating", 0.0) for movie in watched)
    avg_rating = total_ratings / len(watched)
    return avg_rating# ========================================= wave 02- # 1. get_watched_avg_rating ==========

# user_data = {
    # 'watched': [
        # {'genre': 'Fantasy', 'rating': 4.8, 'title': 'The Lord of the Functions: The Fellowship of the Function'}... 'rating': 2.0, 'title': 'Recursion'}, 
        # {'genre': 'Intrigue', 'rating': 4.5, 'title': 'Instructor Student TA Manager'}]}

def get_watched_avg_rating(user_data):
    
    # for movie in user_data["watched": ]
    # average = total ratings / length of watched list
    # total_ratings = user_data["watched"]["ratings"]
    
    # print(user_data["watched"][0]["rating"]) = 4.8
    # print(len(user_data["watched"])) # 6
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

