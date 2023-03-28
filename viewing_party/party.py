# ------------- WAVE 1 --------------------
import statistics

def create_movie(title, genre, rating):
    '''
    input: 3 parameters (title, genre, and rating) which all consist of strings
    output: Dictionary containing the 3 input parameters
    '''
    
    if title and genre and rating:
        movie_details = {'title': title, 'genre': genre, 'rating': rating }
        return movie_details
    else:
        return None
    



def add_to_watched(user_data, movie):
    '''
    input: user_data-dictionary with list of dictionaries & movie- dict. with title of movie watched
    ouput: modified user_data with movie added to watched list
    '''
    user_data['watched'].append(movie)
    return user_data



def add_to_watchlist(user_data, movie):
    '''
    input: user_data-dictionary with list of dictionaries & movie- dict. with title of movie user wants to watch
    ouput: modified user_data with movie added to watchlist
    '''
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
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
#1. 2 variables and iterate list: sum the ratings and count how many movies 
#2. create dictionary that creates key for each new genere and increments value 
#      when it reappears
#  
def get_watched_avg_rating(user_data):

    if len(user_data["watched"]) == 0:
        return 0.0

    ratings_list = []
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    return statistics.mean(ratings_list)


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
