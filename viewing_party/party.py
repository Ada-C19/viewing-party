# ------------- WAVE 1 --------------------
import statistics

def create_movie(title, genre, rating):

    '''
    input: 3 parameters (title, genre, and rating) which all consist of strings
    output: dictionary containing the 3 input parameters
    '''

    # Check to see if the 3 parameters (title, genre, and rating) are truthy.
    # If so, return a dictionary named movie_details containing these 3 attributes as key-value pairs.
    # If all 3 parameters are falsy, return None.
    
    if title and genre and rating:
        movie_details = {'title': title, 'genre': genre, 'rating': rating}
        return movie_details
    else:
        return None
    


def add_to_watched(user_data, movie):

    '''
    input: user_data-dictionary with list of dictionaries & movie dictionary with title of movie watched
    ouput: modified user_data with movie added to 'watched' list
    '''

    # Add new movie (dictionary) as a value (list) associated to the key, "watched" within the user_data dictionary. 

    user_data['watched'].append(movie)
    return user_data



def add_to_watchlist(user_data, movie):

    '''
    input: user_data-dictionary with list of dictionaries & movie- dict. with title of movie user wants to watch
    ouput: modified user_data with movie added to 'watchlist'
    '''

    # Add new movie (dictionary) as a value (list) associated to the key, "watchlist" within the user_data dictionary. 

    user_data['watchlist'].append(movie)
    return user_data



def watch_movie(user_data, title):

    '''
    input: dictionary user_data, string movie user has watched-title
    ouput: updated user_data
    '''

    # Loop through each movie within the "watchlist" nested data structure to see if the title (parameter) exists.
    # If so, remove that movie from the "watchlist" and append it to the "watched" list of user_data.

    for movies in user_data['watchlist']:
        if movies['title'] == title:
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

    # Return 0.0 if the average rating of all the movies int he "watched" list is empty.

    if len(user_data["watched"]) == 0:
        return 0.0

    # Calculate the average rating of all movies within the "watched" list by creating an
    # empty dictionary named "ratings", then looping through each movie in the "watched" list
    # to retrieve and append the rating value of each movie to the "ratings" list, and performing statistics.mean()

    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    return statistics.mean(ratings)



def get_most_watched_genre(user_data):

    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns the movie genre (str) of the most frequently watched movie in the nested watched list (within user_data).
    '''

    # Account for empty movie list as the value of "watched" by returning None.

    if len(user_data["watched"]) == 0:
        return None

    # Determine the genre that is most frequently watched by looping through each movie genre in "watched" to take count of
    # the frequency and adding them as values to the key, 'genre' in a new dictionary named movie_genre_ranking. From there,
    # convert the movie_genre_ranking dictionary into a list, sort from highest to lowest, and return the highest value.

    movie_genre_ranking={}
    for movie in user_data['watched']:
        if movie['genre'] not in movie_genre_ranking:
            movie_genre_ranking[movie['genre']] = 1
        else:
            movie_genre_ranking[movie['genre']] += 1

    sorted_genre_ranking = dict(sorted(movie_genre_ranking.items(),key=lambda item:item[1], reverse = True))
    return list(sorted_genre_ranking.keys())[0]




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


    movies_only_user_watched = []
    for title in watched_movies_by_user:
        movies_only_user_watched.append(watched_movies_by_user[title])

    return movies_only_user_watched



def get_friends_unique_watched(user_data):

    '''
    input: user_data - dictionary with information about users movie and friends
    output: list of movie dictionaries that the users friends have watched but
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

    # Loop through each movie in the list outputted from the get_friends_unique_watched function (which has been assigned to a variable named friends_unique_movies).
    # If the streaming service host of the movie exists in both the friends_unique_movies and "subscription" in user_data, add that movie (dictionary) to the
    # available_friend_movies list and return that list as the final output.

    subscriptions = user_data["subscriptions"]
    friends_unique_movies = get_friends_unique_watched(user_data)
    available_friend_movies = []

    for movie in friends_unique_movies:
        if movie['host'] in subscriptions:
            available_friend_movies.append(movie)
            
    return available_friend_movies
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    '''
    input: takes in one parameter in the form of a dictionary named user_data.
    output: returns a list of recommended movies where the genre is the same as the user's most frequently watched genre.
    Additionally, these movies are ones that the user has not watched but at least one of their friend(s) has watched.
    '''

    # Loop through each movie in the list outputted from the movies_user_has_not_watched function (which has been assigned to a variable named movies_user_has_not_watched).
    # If the movie genre is the same as the genres in the list outputted from the get_most_watched_genre function (which has been assigned to the variable most_watched_genre),
    # add the associated movie to the movie_rec_by_genre list and return that list as the final output.

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

    # Loop through each movie in the list outputted from the get_unique_watched function (which has been assigned to a variable user_watched).
    # If the movie also exists in user_data['favorites'] (which has been assigned to the variable favorites),
    # add the associated movie to the user_favorite_movies list and return that list as the final output.


    favorites = user_data['favorites']
    user_favorite_movies = []
    user_watched = get_unique_watched(user_data)

    for movie in user_watched:
        if movie in favorites:
            user_favorite_movies.append(movie)
    return user_favorite_movies
