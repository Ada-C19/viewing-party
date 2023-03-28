MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    input: title, genre, rating
    output: dictionary
    '''

    movie_dict = {'title': title, 'genre': genre, 'rating': rating}
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
    

def watch_movie(user_data, title):
    '''
    input: user_data is a dictionary with a "watchlist" and a "watched" list of movies;
    title is a string representing the title of the movie the user has watched
    output: user_data
    '''
    #If title in user's watchlist
    #   remove movie from watchlist
    #   add to movies watched
    #   return user_data
    #if not title in user's watchlist
    #   return user_data
    if not title in user_data:
        return user_data
    
    if title in user_data:
        user_data.remove(title)
        user_data.append(title)
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

