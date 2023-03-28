# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies_dict = {}
    if not title or not genre or not rating:
        return None
    else:
        movies_dict["title"] = title
        movies_dict["genre"] = genre
        movies_dict["rating"] = rating 
    return movies_dict

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    is_valid = True

    ### checking that watched_list is not empty
    if watched_list:
    ### checking that title is not already in watched_list keys
        for movie_dict in watched_list:
            if movie_dict["title"] == movie["title"]:
                is_valid = False
    
    ### if movie is not duplicate, append to watched_list
    if is_valid:
        watched_list.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):  
    want_to_watch_list = user_data["watchlist"]
    is_valid = True

    ### checking that want_to_watch_list is not empty
    if want_to_watch_list:
    ### checking that title is not already in want_to_watch_list keys
        for movie_dict in want_to_watch_list:
            if movie_dict["title"] == movie["title"]:
                is_valid = False
    
    ### if movie is not duplicate, append to want_to_watch_list
    if is_valid:
        want_to_watch_list.append(movie)

    return user_data

def watch_movie(user_data, title):
    want_to_watch_list = user_data["watchlist"]
    watched_list = user_data["watched"]
    ##iterating through want_to_watch_list to see if title is present
    for movie_dict in want_to_watch_list:
        ##if title present, remove from want_to_watch list and add to watched_list
        if movie_dict["title"] == title:
            watched_list.append(movie_dict)
            want_to_watch_list.remove(movie_dict)
        ##tried to account for if title not in want_to_watch_list or watched_list
        ## else:
             ##if title not present in want_to_watch_list, just add to watched_list
             ##watched_list.append(movie_dict)
    return user_data






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------



def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    avg_rating = 0.0
    ##empty watch list is 0.0 avg rating
    if len(watched_list) == 0:
        return avg_rating
    else:
        ##iterate through watched_list, add all ratings and then divide by length of watched_list
        for movie_dict in watched_list:
            avg_rating += movie_dict["rating"]
        avg_rating = avg_rating/len(watched_list)
    return avg_rating


def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    genre_dict = {}
    ##return None for empty list
    if len(watched_list) == 0:
        return None
    else:
        #iterate through watched_list for genre and add genre to genre_dict. 
        # Increment value according to genre count.
        for movie_dict in watched_list:
            if movie_dict["genre"] not in genre_dict.keys():
                genre_dict[movie_dict["genre"]] = 1
            else:
                genre_dict[movie_dict["genre"]] += 1
    ##return key that has the max value in genre_dict            
    return max(genre_dict, key=genre_dict.get)
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# 1. Create a function named `get_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends 
# have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies

def get_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends_watched_list = user_data["friends"]
    watched_list_set = set()
    friends_watched_list_set = set()
    unique_watched_list = []

    if not watched_list:
        return []
    elif not friends_watched_list:
        return watched_list

    for movie_dict in watched_list:
        watched_list_set.add(movie_dict["title"])
        print(f"watched_list_set = {watched_list_set}")
    
    for friend in friends_watched_list:
        for movie_dict in friend["watched"]:
            print(f"movie_dict in friend = {movie_dict}")
            friends_watched_list_set.add(movie_dict["title"])
            print(f"friends_watched_list_set = {friends_watched_list_set}")
    
    unique_watched_set = watched_list_set - friends_watched_list_set

    if len(unique_watched_set) == 0:
        return []

    for title in unique_watched_set:
        for movie_dict in watched_list:
            if movie_dict["title"] == title:
                unique_watched_list.append(movie_dict)
    
    return unique_watched_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

