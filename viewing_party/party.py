from statistics import multimode,mode
# ------------- WAVE 1 --------------------

#Create function to store movie
def create_movie(title, genre, rating):
    #create empty dictionary to store the movie
    movie = { "title": "", "genre" : "", "rating" : 0}

    #Check for edge case of one item being none
    if title is None or genre is None or rating is None:
        return None
    else:
        movie["title"]= title
        movie["genre"]= genre
        movie["rating"]= rating

    return movie

def add_to_watched(user_data, movie):
    #add movie a dictionary to watched
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    #add movie a dictionary to watchlist
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
    # Check if title is in watchlist, add it to watched
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            add_to_watched(user_data, movie) 
            user_data["watchlist"].remove(movie)
    return user_data
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # Set initial value of sum_rating to 0
    sum_rating = 0
    # Create a new list of "watched" movies in user_data dict
    movie_list = user_data["watched"]

    # Iterate through movies in list of movies
    for movie in movie_list:
        # Find the sum of the integers in value for "rating" in the movie dict
        sum_rating += movie["rating"]
    # If the input is an empty list, return 0.0 for average
    if len(movie_list) == 0:
        return 0.0
    else:
        # Return the sum of movie ratings divided by the number of movies in input user_data dict
        return sum_rating / len(movie_list)


def get_most_watched_genre(user_data):
    genre_list = []

    movie_list = user_data["watched"]
    for movie in movie_list:
        genre_list.append(movie["genre"])
    if len(genre_list) == 0:
        return None
    else:
        return(multimode(genre_list)[0])


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_watched = []

    for friend in user_data["friends"]:
        friends_watched += friend["watched"]

    unique_movies = []
    for movie in user_watched:
        if movie not in friends_watched and movie not in unique_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    # Get the list of watched movies from the user
    watched_movies = user_data["watched"]
    # Set up an empty list to store movies that the user's friends have watched
    friends_unique_watched = []
    # Iterate through each friend in the user's list of friends
    for friend in user_data["friends"]:
        # Iterate through each movie that the friend has watched
        for movie in friend["watched"]:
            # Check if the user has watched the movie
            if movie not in watched_movies and movie not in friends_unique_watched:
                # If not, add the movie to the friends_unique_watched list
                friends_unique_watched.append(movie)
    # Return the list of movies
    return friends_unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data): 
    # List of friends
    friends = user_data["friends"]
    # List of movies user has watched
    watched_movies = user_data["watched"]
    # Create empty list of recommended movies
    recommendations = []
    
    # Loop over friends
    for friend in friends:
        # List of movies watched by friend
        friend_movies = friend["watched"]
        # Loop over movies watched by friend
    for movie in friend_movies:
        # Conditional if movie user has not watched and movie has available host
        if movie["host"] in user_data["subscriptions"] and movie not in watched_movies and movie not in recommendations:
            # if so, add to list of recommended movies
            recommendations.append(movie)
    print(movie)
    # return list of recommended movies
    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # Get most frequent genre
    genre = get_most_watched_genre(user_data)
    # List of friends
    friends = user_data["friends"]
    # List of movies user has watched
    watched_movies = user_data["watched"]
    # Create empty list of recommended movies
    recommended_movies = []
    
    # Loop over friends
    for friend in friends:
        # List of movies watched by friend
        friend_movies = friend["watched"]
        # Loop over movies watched by friend
    for movie in friend_movies:
        # Conditional if movie is favorite genre/user has not watched
        if movie["genre"] == genre and movie not in watched_movies and movie not in recommended_movies:
            # if so, add to list of recommended movies
            recommended_movies.append(movie)
    
    # return list of recommended movies
    return recommended_movies


def get_rec_from_favorites(user_data):
    # List of friends
    friends = user_data["friends"]
    # Create empty list of recommended movies
    recommended_movies = []

    # # Loop over friends
    for friend in friends:
        # List of movies watched by friend
        friend_movies = friend["watched"]

        # Loop over movies watched by friend
        for movie in friend_movies:
            # Conditional if movie is in favorites/friends have not watched
            if movie in user_data["favorites"] and movie not in friend_movies:
                # if so, add to list of recommended movies
                recommended_movies.append(movie)
    
    # return list of recommended movies
    return recommended_movies
