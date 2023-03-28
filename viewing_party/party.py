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
    

    # - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
    # - ```python
    #   {
    #     "title": "Title A",
    #     "genre": "Horror",
    #     "rating": 3.5
    #   }

#   - Have three key-value pairs, with specific keys
#   - The three keys should be `"title"`, `"genre"`, and `"rating"`
#   - The values of these key-value pairs should be appropriate values


    # new_movie = {}
    # if title and genre and rating : 
    #     new_movie["title"] = title
    #     new_movie["genre"] = genre
    #     new_movie["rating"]= rating   
    #     # print(new_movie)
    #     return new_movie
    
    # else: 
    #     # print(None)
    #     return None
        

# take two parameters: user_data, movie 
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    # print(user_data)
    return user_data

# ========================================= wave 01- # 3. add to watchlist ==========
# take two parameters: user_data, movie

def add_to_watchlist(user_data, movie):
    #  value of user_data is a dict w/ key "watch_list"
    
    # user_data= {
    #     "watchlist": []
    #     }
    
    user_data["watchlist"].append(movie)
    return user_data
        
# ========================================= wave 01- # 4. add to watchlist ==========
    
    
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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

