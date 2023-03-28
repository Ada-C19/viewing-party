MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5
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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

