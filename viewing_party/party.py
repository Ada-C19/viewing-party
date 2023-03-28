
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    input: title, genre, rating
    output: dictionary
    '''
    if not title:
        return None
    if not genre: 
        return None
    if not rating:
        return None
    
    movie_dict = {'title': title, 'genre': genre, 'rating': rating}
    if movie_dict == False:
        return None
    return movie_dict
        

def add_to_watched(user_data, movie):
    #user_data is a dict with key "watched"
    movies_user_has_watched = user_data["watched"]
    # a list of dicts rep the movies the user has watched
    # append (represent) movie to list of dict
    movies_user_has_watched.append(movie)
    #add movie to the "movies_user_has_watched" inside of user data

    return user_data

def add_to_watchlist(user_data, movie):
    # user_data is a dict with key "watchlist"
    movies_user_wants_to_watch = user_data["watchlist"]
    if movies_user_wants_to_watch is None:
        # an empty list rep that the user has no movies in their watchlist
        movies_user_wants_to_watch = []
        # a list of dicts rep the movies the user has watched
    # append (represent) movie to list of dict
    movies_user_wants_to_watch.append(movie)


    return user_data


def watch_movie(user_data, title):
    '''
    input: user_data is a dictionary with a "watchlist" and a "watched" list of movies;
    title is a string representing the title of the movie the user has watched
    output: user_data
    '''
    if not title in user_data:
        return user_data
    
    if title in user_data:
        user_data.remove(title['watchlist'])
        user_data.append(title['watched'])
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    pass
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries
    # calculate the average rating of all movies in the watched list
    # an empty "watched" list has a value of 0.0
    output: average rating 
    '''    
    # #user_data is a dict with "watched" list of dict
    # user_list_of_watched_movies = user_data["watched"]
    # #calc th avg rating of all movies in the watched list
    # for i in range(len(user_data)):
    #     sum(user_list_of_watched_movies)
# }
def get_most_watched_genre(user_data):
    pass
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries. 
    # each movie dictionary has a key 'genre' which is a string
    # determine which genre is the most frequently occurring in the 'watched' list 
    # if the value of 'watched' is an empty string, function should return None
    output: genre that's most frequently watched 
    ''' 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

