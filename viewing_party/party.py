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

def get_most_watched_genre(user_data):


    if len(user_data["watched"]) == 0:
        return None

    movie_genre={}
    for movie in user_data['watched']:
        if movie['genre'] not in movie_genre:
            movie_genre[movie['genre']]=1
        else:
            movie_genre[movie['genre']]+=1

    most_watched_genre=''
    frequency=0

    for genre, amount in movie_genre.items():
        if amount > frequency:
            most_watched_genre = genre
            frequency = amount

    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
#friends is a list of dics
#1. deep copy list of watched movies, iterate over all friends dics and remove movies 
#2. Make list of docs with unique movies friends have and remove all the user has

def get_unique_watched(user_data):
    # user_watched = []
    # friends_watched = []

    # for movie in user_data["watched"]:
    #     user_watched.append((movie["title"], movie))
    
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         friends_watched.append((movie["title"], movie))

    # return set(user_watched) - set(friends_watched)
    user_watched = {}

    for movie in user_data["watched"]:
        user_watched[movie['title']]=movie
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie['title'] in user_watched:
                del user_watched[movie['title']]
    return_list=[]
    for title in user_watched:
        return_list.append(user_watched[title])

    return return_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# 1. call the function prevously made and check the host of movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
#1. same as before but fikter by genre 
#2. find unique movies of user filter the favorites
