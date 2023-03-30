from statistics import multimode,mode
# ------------- WAVE 1 --------------------

# Create function to store movie
def create_movie(title, genre, rating):
    # Create empty dictionary to store the movie
    movie = { "title": "", "genre" : "", "rating" : 0}

    # Check for edge case of one item being none
    if title is None or genre is None or rating is None:
        return None
    else:
        movie["title"]= title
        movie["genre"]= genre
        movie["rating"]= rating

    return movie

def add_to_watched(user_data, movie):
    # Add movie a dictionary to watched
    user_data["watched"].append(movie)
    
    return user_data
    
def add_to_watchlist(user_data, movie):
    # Add movie a dictionary to watchlist
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    
    # Iterate through movies in user watchlist
    for movie in user_data["watchlist"]:
        # Conditional if title is in user movie in watched
        if title in movie["title"]:
            add_to_watched(user_data, movie) 
            # Then remove the watched movie from watchlist
            user_data["watchlist"].remove(movie)

    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """Set initial value of sum_rating to 0.
    Create a new list of "watched" movies in user_data dict.
    Iterate through movies in list of movies
    Iterate through movies in list of movies
    Find the sum of the integers in value for "rating" in the movie dict
    If the input is an empty list, return 0.0 for average
    Return the sum of movie ratings divided by the number of movies in input user_data dict
    """

    sum_rating = 0
    
    movie_list = user_data["watched"]

    for movie in movie_list:
        sum_rating += movie["rating"]
    if len(movie_list) == 0:
        return 0.0
    else:
        return sum_rating / len(movie_list)


def get_most_watched_genre(user_data):
    """
    Create variable that is a list
    Set variable to user's watched list
    Loop through movies in user's watched list
    Add movie genre to genre list
    If genre list has 0 genres, then return None
    Multimode returns most commonly occurring element in list

    """
    genre_list = []

    movie_list = user_data["watched"]

    for movie in movie_list:
        genre_list.append(movie["genre"])

    if len(genre_list) == 0:
        return None
    else:
        return(multimode(genre_list)[0])


# # My super long implementation w/o using multimode
# def get_most_watched_genre(user_data):
#     # Get the watched list
#     watched_list = user_data["watched"]

#     # Check if the watched list is empty
#     if len(watched_list) == 0:
#         return None

#     # Create a dictionary to store the count of each genre
#     genre_count = {}

#     # Iterate through the watched list
#     for movie in watched_list:
#         genre = movie["genre"]

#     # Check if the genre is already in the dictionary
#     if genre in genre_count:
#         # Increment the count
#         genre_count[genre] += 1
#     else:
#         # Initialize the count
#         genre_count[genre] = 1

#     # Get the most frequent genre
#     most_frequent_genre = None
#     most_frequent_count = 0

#     for genre, count in genre_count.items():
#         if count > most_frequent_count:
#             most_frequent_count = count

#     return most_frequent_count


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """ 
    Get the list of watched movies from user
    Create variable of friends watched movies
    Set variable to list of unique movies
    Loop through friends 
    Adding friends watched movies to list friends_watched
    Iterate through movies of user's watched list
    Conditional that movie is not in friends watched and not in unique movies lists
    Add that movie to unique movies list
    """
    user_watched = user_data["watched"]
    friends_watched = []
    unique_movies = []

    for friend in user_data["friends"]:
        friends_watched += friend["watched"]

    for movie in user_watched:
        if movie not in friends_watched and movie not in unique_movies:
            unique_movies.append(movie)
    
    return unique_movies

def get_friends_unique_watched(user_data):
    """
    Get the list of watched movies from the user
    Set up an empty list to store movies that the user's friends have watched
    Iterate through each friend in the user's list of friends
    Iterate through each movie that the friend has watched
    Check if the user has watched the movie
    If not, add the movie to the friends_unique_watched list
    """
    watched_movies = user_data["watched"]
    friends_unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in watched_movies and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)

    return friends_unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data): 
    """
    Create empty list of recommended movies
    Loop over movies watched by friend
    Conditional if host is in subscriptions and in friends watched and movie not in recommendations list
    If so, add to list of recommended movies
    """
    friend_unique_watched = get_friends_unique_watched(user_data)
    recommendations = []
    for movie in friend_unique_watched:
        if (movie["host"] in user_data["subscriptions"]) and (movie in friend_unique_watched) and (movie not in recommendations):
            recommendations.append(movie)
    
    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    Get most frequent genre
    List of friends
    List of movies user has watched
    Create empty list of recommended movies
    Loop over friends
    List of movies watched by friend
    Loop over movies watched by friend
    Conditional if movie is favorite genre/user has not watched
    If so, add to list of recommended movies
    """
    genre = get_most_watched_genre(user_data)
    friends = user_data["friends"]
    watched_movies = user_data["watched"]
    recommended_movies = []
    
    
    for friend in friends:
        friend_movies = friend["watched"]
        for movie in friend_movies:
            if (movie["genre"] == genre) and (movie not in watched_movies) and (movie not in recommended_movies):
                recommended_movies.append(movie)
    
    return recommended_movies


def get_rec_from_favorites(user_data):
    """
    Set favorites to user's favorite movies
    Set unique watched variable to unique watched movies from function call
    Set variable to an empty list
    Iterate through favorite movies
    Conditional if movie is in the unique watched list
    Add movie to the recommendation list
    """
    favorites = user_data["favorites"]
    unique_watched = get_unique_watched(user_data)
    reccomendation_list = []

    for movie in favorites:
        if movie in unique_watched:
            reccomendation_list.append(movie)
    
    return reccomendation_list