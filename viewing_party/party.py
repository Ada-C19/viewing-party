# ------------- WAVE 1 --------------------
import statistics

def create_movie(title, genre, rating):

    '''
    input: 3 parameters (title, genre, and rating) which all consist of strings
    output: dictionary containing the 3 input parameters
    '''
    
    if title and genre and rating:
        movie_details = {'title': title, 'genre': genre, 'rating': rating }
        return movie_details
    else:
        return None
    



def add_to_watched(user_data, movie):

    '''
    input: user_data-dictionary with list of dictionaries & movie dictionary with title of movie watched
    ouput: modified user_data with movie added to 'watched' list
    '''

    user_data['watched'].append(movie)
    return user_data



def add_to_watchlist(user_data, movie):

    '''
    input: user_data-dictionary with list of dictionaries & movie- dict. with title of movie user wants to watch
    ouput: modified user_data with movie added to 'watchlist'
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

    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    return statistics.mean(ratings)



def get_most_watched_genre(user_data):

    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns the movie genre (str) of the most frequently watched movie in the nested watched list (within user_data).
    '''

    if len(user_data["watched"]) == 0:
        return None

    movie_genre_ranquing={}
    for movie in user_data['watched']:
        if movie['genre'] not in movie_genre_ranquing:
            movie_genre_ranquing[movie['genre']]=1
        else:
            movie_genre_ranquing[movie['genre']]+=1

    sorted_genre_ranquing=dict(sorted(movie_genre_ranquing.items(),key=lambda item:item[1], reverse = True))
    return list(sorted_genre_ranquing.keys())[0]




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
    # Key : str / movie tiitle   Value: dictionary containing movie info 

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
    # Key : str / movie tiitle   Value: dictionary containing movie info 

    movies_friends_watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movies_friends_watched[movie['title']] = movie


    # Looped over the movies friends have watched and modified friend_watched
    # by removing the key value pair when the user has already watched a movie


    for movie in user_data["watched"]:
        if movie['title'] in movies_friends_watched:
            del movies_friends_watched[movie['title']] 

    # Created a list and looped over friend_watched to return 
    # the movie dictionaries in a list

    user_not_watched_movies = []
    for title in movies_friends_watched:
        user_not_watched_movies.append(movies_friends_watched[title])

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

    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns a list of recommended movies where the genre is the same as the user's most frequently watched genre.
    Additionally, these movies are ones that the user has not watched but at least one of their friend(s) has watched.
    '''

    movies_user_has_not_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    movie_rec_by_genre = []

    for movie in movies_user_has_not_watched:
        if movie['genre'] == most_watched_genre:
            movie_rec_by_genre.append(movie)
    
    return movie_rec_by_genre


def get_rec_from_favorites (user_data):

    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns a list of recommended movies containing only the user's "favorites" that none of their friends have watched.
    '''

    favorites = user_data['favorites']
    user_favorite_movies = []
    user_watched= get_unique_watched(user_data)

    for movie in user_watched:
        if movie in favorites:
            user_favorite_movies.append(movie)
    return user_favorite_movies
