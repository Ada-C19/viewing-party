from statistics import multimode,mode
# ------------- WAVE 1 --------------------

# Create definition to store movie
def create_movie(title, genre, rating):
    # Create empty dictionary to store the movie
    movie = { "title": "", "genre" : "", "rating" : 0}

    # Check for edge case of one item being none
    if title is None or genre is None or rating is None:
        return None
    else:
        movie["title"]= title
        movie["genre"]= genre
        movie["rating"]= rating

    return movie

def add_to_watched(user_data, movie):
    # Add movie a dictionary to watched
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    # Add movie a dictionary to watchlist
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
    # Check if title is in watchlist, add it to watched
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            add_to_watched(user_data, movie) 
            user_data["watchlist"].remove(movie)
    return user_data
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # Set initial value of sum_rating to 0
    sum_rating = 0
    # Create a new list of "watched" movies in user_data dict
    movie_list = user_data["watched"]

    # Iterate through movies in list of movies
    for movie in movie_list:
        # Find the sum of the integers in value for "rating" in the movie dict
        sum_rating += movie["rating"]
    # If the input is an empty list, return 0.0 for average
    if len(movie_list) == 0:
        return 0.0
    else:
        # Return the sum of movie ratings divided by the number of movies in input user_data dict
        return sum_rating / len(movie_list)


def get_most_watched_genre(user_data):
    genre_list = []

    movie_list = user_data["watched"]
    for movie in movie_list:
        genre_list.append(movie["genre"])
    if len(genre_list) == 0:
        return None
    else:
        return(multimode(genre_list)[0])


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    pass
    

def get_friends_unique_watched(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------