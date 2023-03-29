# ------------- WAVE 1 -------------------- 
# ========================================= wave 01- # 1. create_movie ========== RC/ SJ

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

# ========================================= wave 01- # 2. add to watched ========== RC

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

# ========================================= wave 01- # 2. add to watchlist========== RC

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

# ========================================= wave 01- # 2. add to watched ========== SJ

# take two parameters: user_data, movie 
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    # print(user_data)
    return user_data

# ========================================= wave 01- # 3. add to watchlist ========== SJ
# take two parameters: user_data, movie

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


# ========================================= wave 01- # 4. watch movie ========== RC

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
            
# ========================================= wave 01- # 4. watch movie ========== RC

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
            
# ========================================= wave 01- # 4. watch movie ========== SJ

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
# ========================================= wave 02- # 1. get_watched_avg_rating ========== RC

def get_watched_avg_rating(user_data):
    # This represents that the user has a list of watched movies
    watched = user_data.get("watched", [])
    # The average rating of an empty watched list is `0.0`
    if not watched:
        return 0.0
    # Calculate the average rating of all movies in the watched list
    total_ratings = sum(movie.get("rating", 0.0) for movie in watched)
    # return the average rating
    avg_rating = total_ratings / len(watched)
    return avg_rating

# ========================================= wave 02- # 2. get_most_watched_genre ========== RC

def get_most_watched_genre(user_data):
    # keep the var the same
    watched = user_data["watched"]
    # if movie title not watched, return none
    if not watched:
        return None
    
    # iterate thru each "genre" key's value for the entire length of nested dictionary
    genres_watched = [watched[i]["genre"] for i in range(len(watched))]
    # get the most watched genre with max function
    return max(genres_watched, key=genres_watched.count)

# ========================================= wave 02- # 1. get_watched_avg_rating ========== RC

# user_data = {
#     'watched': [
#         {'genre': 'Fantasy', 'rating': 4.8, 'title': 'The Lord of the Functions: The Fellowship of the Function'}... 'rating': 2.0, 'title': 'Recursion'}, 
#         {'genre': 'Intrigue', 'rating': 4.5, 'title': 'Instructor Student TA Manager'}]}

def get_watched_avg_rating(user_data):
    # This represents that the user has a list of watched movies
    watched = user_data.get("watched", [])
    
    # The average rating of an empty watched list is `0.0`
    if not watched:
        return 0.0
    
    # Calculate the average rating of all movies in the watched list
    total_ratings = sum(movie.get("rating", 0.0) for movie in watched)
    
    # return the average rating
    avg_rating = total_ratings / len(watched)
    return avg_rating

# ========================================= wave 02- # 2. get_most_watched_genre ========== RC

def get_most_watched_genre(user_data):
    watched_genres = {}

# - Determine which genre is most frequently occurring in the watched list
    # iterate through 
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in watched_genres:
            watched_genres["genre"] += 1
        else:
            watched_genres["genre"] = 1

    if not watched_genres:
        return None 
    print(watched_genres)
    return max(watched_genres, key=watched_genres.get)


# ========================================= wave 02- # 2. get_watched_avg_rating ========== SJ

def get_watched_avg_rating(user_data): 
    
    #  initialize a variable for ratings  set to 0     
    ratings_total = 0
    average_rating = 0

    #  if the length of the user_ data( "watched") is empty  
    if len(user_data["watched"]) == 0: 
        average_rating == 0.0
        return average_rating
    
    else: 
        # loop through movies in the the watched list in user_data
        for movie in user_data["watched"]: 
                            
            #  add the rating to the ratings total 
            ratings_total += movie["rating"]
            print(ratings_total)
            
            #  average rating is ratings_total / length (user_data["watched"]) 
            average_rating = ratings_total/ len(user_data["watched"])
                
    return average_rating

# ========================================= wave 02- # 2. get_watched_avg_rating ========== SJ

# def get_most_watched_genre(user_data):
#     pass 
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# ========================================= wave 03- # 1. get_unique_watched ========== RC

def get_unique_watched(user_data):
    # movies that friends have watched
    friends_watched = {movie['title'] for friend in user_data['friends'] for movie in friend['watched']}

    # movies that ONLY user has watched 
    unique_movies = [movie for movie in user_data['watched'] if movie['title'] not in friends_watched]

    # Return the list of unique movies
    return unique_movies

# ========================================= wave 03- # 2. get_friends_unique_watched ========== RC


def get_friends_unique_watched(user_data):
    # Create var for movies user has watched already
    user_watched = {movie['title'] for movie in user_data['watched']}

    # Create var for movies friends have watched 
    friends_watched = {movie['title'] for friend in user_data['friends'] for movie in friend['watched']}

    # Create a set of the movies that the user's friends have watched, but the user has not watched
    unique_movies = friends_watched - user_watched

    # Return a list of dictionaries representing the unique movies
    return [{"title": movie} for movie in unique_movies]

    
    
# ========================================= wave 03- # 1. get_unique_watched ========== SJ

    
# save my watch list, remove every movie my friends have seen, and remove it from my watch list
# to do that iterate over my friends list, iterate over every movie that that friend has watched
# enumerate the key in values in my watch list 
# and remove any indicies in my watch list where the value equals the value of the movie title

# def get_unique_watched( user_data): 
    
#     #  everything that i've watched 
#     my_watched_list = user_data["watched"]
    
#     #  for each friend, loop over their watched then deletd from you watch list
#     for friend in user_data["friends"]: 
        
#         friends_watched_list = friend["watched"]
        
#         #  iterate over my watched list
#         for movie in friends_watched_list: 
            
#             # if friends_watched_list["title"] == my_watched_list["title"]: 
                
#                 my_watched_list.remove(movie)
                
#     return my_watched_list

    
    # user_data_friends
    # iterate over dictionary of friends, 
    # with each friend, iterate over the movies they have watched 
    
    # compare their watched list with the user data watched list
    
        # for the movies they share, 
        # remove the movie the user and the friend have both watched 
        
        # returning a list of dictionaries that represents a list of movies that 
        # the user has watched that none of their friends have watched
    
    
# Consider the movies that the user has watched, 
# user_data["watched"] = movies you have watched

# user_data["friends"]
# and consider the movies that their friends have watched. 
# Determine which movies the user has watched, but none of their friends have watched.


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# ========================================= wave 04- # 1. get_available_recs ==========





# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# ========================================= wave 05- # 1.  get_new_rec_by_genre ==========

# ========================================= wave 05- # 2. get_rec_from_favorites ==========
