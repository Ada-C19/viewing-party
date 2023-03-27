# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass

    # if the three parameters are valid, return a dictionary:
        # 'title': movie name   'genre': '(eg horror, drama, suspense)'     'rating': (float)
    # elif one of the three parameters are not valid: (valid == type (str vs float)? if type(int)
    # cast to float; present vs not present?)
        # return None

    # if (title, genre, rating) == True: return dict
    # elif: 
    # return None
    

def add_to_watched(user_data, movie):
    pass

    # user_data = dictionary
        # key = 'watched':  value = [list of {dictionaries}] to represent what movies the user has watched.
            # would each dict contain the format title/genre/rating? yes
            # empty list = no movies in watch list
    # add the movie to the "watchlist" inside of user_data
        
    # user_data = {"title": "Title A","genre": "Horror", "rating": 3.5}]}
        # if user_data empty = none watched


def add_to_watchlist(user_data, movie):
    pass

    # user_data = dictionary
        # key = watchlist:  value = [list of {dictionaries}] to represent what movies the user wants to watch
            # add movie to 'watchlist' inside of user_data
            # return user_data

def watch_movie(user_data, title):
    pass

    # user_data = dictionary with 'watchlist' and 'watched': 
        # watchlist and watched represent that the user has a watchlist (<---is this a list as well?) 
        # and a list of watched movies.

        # title = str; represents the title of the movie the user has watched
    
    # if title in user's watchlist:
        # remove that movie from the watchlist
        # add that movie to watched
        # return user_data
    # elif not title in user's watchlist:
        #return user_data

# ****** Waves 2, 3, 4, 5: should not modify user_data ******










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

