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

def get_watched_avg_rating(user_data):
    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns the average rating (float) of all the movies within the watched list value in user_data.
    '''

    if len(user_data["watched"]) == 0:
        return 0.0

    ratings_list = []
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    return statistics.mean(ratings_list)

def get_most_watched_genre(user_data):
    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns the movie genre (str) of the most frequently watched movie in the nested watched list (within user_data).
    '''

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

def get_unique_watched(user_data):


    '''
    input: user_data - dictionary with information about users movie and friends
    output: list of movie dctionaries that the user has watched but
            their friends havent
    '''


    # Created a dictionay with the movie the user has watched
        #Key : str / movie tiitle   Value: dictionary containing movie info 
    watched_movies_by_user = {movie['title']:movie for movie in user_data['watched']}


    # Looped over the movies the friends have watched and modified user_watched
    # by removing the key value pair when a friend had already watched a movie


    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie['title'] in watched_movies_by_user:
                del watched_movies_by_user[movie['title']]

    # Created a list and looped over user_watched to return 
    # the movie dictionaries in a list


    movies_only_user_watched=[]
    for title in watched_movies_by_user:
        movies_only_user_watched.append(watched_movies_by_user[title])

    return movies_only_user_watched



def get_friends_unique_watched(user_data):
    '''
    input: user_data - dictionary with information about users movie and friends
    output: list of movie dctionaries that the users friends have watched but
    they havent
    '''


# Created a dictionay with the movie the users friends have watched
        #Key : str / movie tiitle   Value: dictionary containing movie info 

    friend_watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched[movie['title']] = movie


    # Looped over the movies the friends have watched and modified friend_watched
    # by removing the key value pair when the user has already watched a movie


    for movie in user_data["watched"]:
        if movie['title'] in friend_watched:
            del friend_watched[movie['title']] 

    # Created a list and looped over friend_watched to return 
    # the movie dictionaries in a list

    user_not_watched_movies = []
    for title in friend_watched:
        user_not_watched_movies.append(friend_watched[title])

    return user_not_watched_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns a list of recommended movies from the same subscription service that the user has not watched but at least one of their friend(s) has watched.
    '''
    
    subscriptions = user_data["subscriptions"]
    friends_unique_movies= get_friends_unique_watched(user_data)
    avaible_friend_movies=[]

    for movie in friends_unique_movies:
        if movie['host'] in subscriptions:
            avaible_friend_movies.append(movie)
            
    return avaible_friend_movies
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):

    user_has_not_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    rec_by_genre = []

    for movie in user_has_not_watched:
        if movie['genre'] == most_watched_genre:
            rec_by_genre.append(movie)
    
    return rec_by_genre


def get_rec_from_favorites (user_data):
    favorites = user_data['favorites']
    user_favorites = []
    user_watched= get_unique_watched(user_data)

    for movie in user_watched:
        if movie in favorites:
            user_favorites.append(movie)
    return user_favorites
