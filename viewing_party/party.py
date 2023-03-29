# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    input: title, genre, rating
    output: dictionary with the three keys "title", "genre", and "rating"
    """
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

    return None 


def add_to_watched(user_data, movie):
    """
    input: user_data dictionary with nested list as values, movie dictionary
    output: updated user_data dictionary 
    """

    user_data["watched"].append(movie) 

    return user_data
    


def add_to_watchlist(user_data, movie):
    """
    input: user_data dictionary, and movie dictionary
    output: updated user_data dictionary
    """

    user_data["watchlist"].append(movie) 

    return user_data

# The data below is for testing function watch_movie()
user_data = {
    "watchlist": [
        {"title": "Land Before Time"},
        {"title": "Spirited Away"}
    ],
    "watched": [
            {"title": "Lord of the Rings"},
            {"title": "Parasyte"},
            {"title": "Harry Potter"},
            {"title": "Ready Player One"}
    ]
}

title = 'Land Before Time'

def watch_movie(user_data, title):
    """
    input: user_data dictionary, and title string
    output: updated user_data dictionary 
    """ 
    # print(user_data, "here")


    # new idea! Iterate through user_data to see if title is in watchlist
    # for key in user_data:
    #     print(key, "ooooo")
    #     for element in key.values():
    #             # print(key, element, "here")
    #         # if "title" in movie
    #             if title in "movie":
    #                 # user_data["watchlist"]["movie"].remove(["title"])
    #                 del user_data["watchlist"]["movie"]["title"]
    #                 user_data ["watched"].append("title")
    #                 return user_data
    #             else:
    #                 return user_data 
            


    for movie in user_data["watchlist"]:
        print(movie, 'here')
        print(title, "lll")
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
        else:
            return user_data
        # if "title" in movie:
        #     ["title"] == title
            
watch_movie(user_data, title)


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: average rating float
    """

def get_most_watched_genre(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: genre string
    """


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: list of dictionaries (which represents list of movies)
    """

def get_friends_unique_watched(user_data):
    """
    input: user_data dictionary with a "watched" list of movie dictionaries
    output: list of dictionaries (which represents list of movies)
    """


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """
    input: user_data dictionary with field "subscriptions", value of "subscriptions" is list of strings
    output: recommended movies list
    """

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    input: user_data dictionary 
    output: recommended movies list
    """


def get_rec_from_favorites(user_data):
    """
    input: user_data dictionary with field "favorites", value of "favorites" is a list of movie dictionaries
    output: recommended movies list
    """