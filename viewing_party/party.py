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
# 3. Create a function named `add_to_watchlist`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value which is a list of dictionaries representing the movies the user wants to watch
#     - An empty list represents that the user has no movies in their watchlist
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watchlist"` list inside of `user_data`
# - return the `user_data`
    future_watch_list = user_data["watchlist"]
    is_valid = True

    ### checking that future_watch_list is not empty
    if future_watch_list:
    ### checking that title is not already in future_watch_list keys
        for movie_dict in future_watch_list:
            if movie_dict["title"] == movie["title"]:
                is_valid = False
    
    ### if movie is not duplicate, append to watched_list
    if is_valid:
        future_watch_list.append(movie)

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

