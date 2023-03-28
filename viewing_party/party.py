# ------------- WAVE 1 --------------------
# Wave 1



# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.

def create_movie(title, genre, rating):

    #for movie in title:

    movies = title, genre, rating
    if all(movies):
    #if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None


def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)
    return user_data


# add the movie to the "watched" list inside of user_data
# return the user_data
    
#   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is 
# a list of dictionaries representing the movies the user has watched
#     - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watched"` list inside of `user_data`
# - return the `user_data`

    pass

def add_to_watchlist(user_data, movie):
    pass

def watch_movie(user_data, title):
    pass
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

