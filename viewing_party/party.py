# ------------- WAVE 1 --------------------

janes_data = {
    "watchlist": [{
        "title": "MOVIE_TITLE_1",
        "genre": "GENRE_1",
        "rating": "RATING_1"
    }],
    "watched": [{
        "title": "MOVIE_TITLE_2",
        "genre": "GENRE_2",
        "rating": "RATING_2"
    }]
}

def create_movie(title, genre, rating):
    '''
    input: 3 parameters (title, genre, and rating) which all consist of strings
    output: Dictionary containing the 3 input parameters
    '''
    #Keys:"title", "genre", and "rating"

    
    if title and genre and rating:
        movie_details = {'title': title, 'genre': genre, 'rating': rating }
        return movie_details
    else:
        return None
    



def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data



def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data



def watch_movie(user_data, title):
    '''
    input: dictionary user_data, string movie user has watched-title
    ouput: updated user_data
    '''

    for movies in user_data['watchlist']:
        if movies['title']==title:
            user_data["watchlist"].remove(movies)
            user_data["watched"].append(movies)


    return user_data
    




    
#watch_movie(janes_data, "MOVIE_TITLE_2")

    # if title in user_data["watchlist"]:
    #     user_data["watchlist"].remove(title)
    #     user_data["watched"].append(title)
    #     return user_data
    

    #if title in user_data
    #Validate if title is in watchlist(key in user_data)
    #     remove from watchlist 
    #     append to watched
    #     return user_data
    #else:
    #     return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
#1. 2 variables and iterate list: sum the ratings and count how many movies 
#2. create dictionary that creates key for each new genere and increments value 
#      when it reappears
#  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
#friends is a list of dics
#1. deep copy list of watched movies, iterate over all friends dics and remove movies 
#2. Make list of docs with unique movies friends have and remove all the user has
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# 1. call the function prevously made and check the host of movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
#1. same as before but fikter by genre 
#2. find unique movies of user filter the favorites
