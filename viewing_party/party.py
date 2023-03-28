from tests.test_constants import *
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """- add the `movie` to the `"watched"` list inside of `user_data`
- return the `user_data`"""
    user_data = {"title":title,"genre":genre,"rating":rating}
    if title and genre and rating:
        return user_data
    else:
        return None

def add_to_watched(user_data, movie):
    """- add the `movie` to the `"watched"` list inside of `user_data`
- return the `user_data`"""
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """- add the `movie` to the `"watchlist"` list inside of `user_data`
- return the `user_data`"""
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """- If the title is in a movie in the user's watchlist:
- remove that movie from the watchlist
- add that movie to watched
- return the `user_data`
- If the title is not a movie in the user's watchlist:
- return the `user_data`"""
    
    for i in user_data["watchlist"]:
        if i["title"] == title:
            user_data["watchlist"].remove(i)
            user_data["watched"].append(title)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    """- Calculate the average rating of all movies in the watched list
- The average rating of an empty watched list is `0.0`
- return the average rating"""
    pass

def get_most_watched_genre(user_data):
    """- Determine which genre is most frequently occurring in the watched list
- return the genre that is the most frequently watched
- If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`."""
    pass

# -----------------------------------------
# -----------------------------------------
# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    """- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
- Return a list of dictionaries, that represents a list of movies
"""

    set_of_data = {}
    list_of_user_data = []
    list_of_friends_data = []
    
    for i in user_data["watched"]:
        list_of_user_data.append(i)
        
    for p in user_data["friends"]:
        for k in p["watched"]:
        
            list_of_friends_data.append(k["title"])
    
    list_of_user_data = set(list_of_user_data)
    list_of_friends_data = set(list_of_friends_data)
    set_of_data = list_of_user_data.difference(list_of_friends_data)
    return_list_of_user_data = list(set_of_data)   
    return return_list_of_user_data


def get_friends_unique_watched(user_data):
    """- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
- Return a list of dictionaries, that represents a list of movies
"""
    pass

# -----------------------------------------   
# -----------------------------------------
# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    """- Determine a list of recommended movies. A movie should be added to this list if and only if:
- The user has not watched it
- At least one of the user's friends has watched
- The `"host"` of the movie is a service that is in the user's `"subscriptions"`
- Return the list of recommended movies"""
    pass

# -----------------------------------------
# -----------------------------------------
# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    """  - The user has not watched it
- At least one of the user's friends has watched
- The `"genre"` of the movie is the same as the user's most frequent genre
- Return the list of recommended movies"""
    pass
# -----------------------------------------

