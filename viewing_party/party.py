# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # create empty dictionary
    movie_ratings = {}

    # verify valid input, otherwise return None
    if not title or not genre or not rating:
        return None
    
    # assign key-value pairs to empty dictionary
    movie_ratings["title"] = title
    movie_ratings["genre"] = genre
    movie_ratings["rating"] = rating
    
    # return dictionary
    return movie_ratings


def add_to_watched(user_data, movie):
    # pull out the list of movie dictionaries
    watched = user_data["watched"]

    # add movie dictionaries to the watched list
    watched.append(movie)

    # return user_data dictionary with the added movie dictionary
    return user_data

def add_to_watchlist(user_data, movie):
    # pull out the list of movie dictionaries to be watched
    watch_list = user_data["watchlist"]

    # add movie dictionaries to watch list
    watch_list.append(movie)

    # return user_data dictonary with the added movie dictionary
    return user_data

def access_element_in_list(list):
    # helper function to grab an element from a list
    for item in list:
        desired_item = item
    return desired_item

def watch_movie(user_data, title):
    # pull out the list of movie dictionaries to be watched
    watch_list = user_data["watchlist"]

    # pull out the list of movie dictionaries already watched 
    watched = user_data["watched"]

    # invoke helper function to grab the list of movie dictionaries from watch list
    movie = access_element_in_list(watch_list)

    # check if the title is already in the to be watched list
    # remove movie and add it to the already watched list
    if title in movie["title"]:
        watch_list.remove(movie)
        watched.append(movie)   
    
    # return updated user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # initialize total rating variable to zero
    total_rating = 0
    
    # pull out list of already watched movie dictionaries
    watched = user_data["watched"]
    
    # iterate through each movie dictionary
    # add each movie's rating to total rating 
    for movie in watched:
        rating = movie["rating"]
        total_rating += rating

    # calculate average rating and catch ZeroDivisionError
    try:
        average_rating = total_rating / len(watched)
    except ZeroDivisionError:
        average_rating = 0.0

    # return average movie rating
    return average_rating

    
def get_most_watched_genre(user_data):
    # pull out list of watched movie dictionaries
    watched = user_data["watched"]
    
    # return None if watched list is empty
    if len(watched) == 0:
        return None
    
    # create empty list of genres
    genre_list = []

    # iterate through each movie in watched list
    # grab each genre and add to genre list
    for movie in watched:
        genre = movie["genre"]
        genre_list.append(genre)
    
    # calculate most frequent genre
    max_genre = max((genre_list), key = genre_list.count)
    
    # return most frequent genre
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # pull out list of user's watched movie dictionaries 
    watched = user_data["watched"]

    # pull out list of friends' data
    friends = user_data["friends"]

    # create empty list for movie dictionaries unique to user but not to friends
    unique_movies = []
    # create empty list for movie titles that friend have seen
    friends_movies = []

    # iterate through friends' data to get to movie titles
    # add the titles to the friend movie list
    for films in friends:
        for film in films["watched"]:
            friend_title = film["title"]
            friends_movies.append(friend_title)

    # iterate through user watched list to get movie titles
    # if movie title not in friend movie list, add to unique movie list
    for movie in watched:
        title = movie["title"]
        if not title in friends_movies:
            unique_movies.append(movie)

    # return updated unique_movie list
    return unique_movies

def get_friends_unique_watched(user_data):
    # pull out list of user's watched movie dictionaries
    watched = user_data["watched"]

    # pull out list of friends' data
    friends = user_data["friends"]

    # create empty list for movie dictionaries unique to friends but not to user
    friend_unique_movies = []
    # create empty list for movie titles that user has watched
    user_movies = []

    # iterate through watched movies and add movie title to user movies list
    for movie in watched:
        title = movie["title"]
        user_movies.append(title)

    # iterate through friends'data to get to movie titles
    # compare friend's movie titles to user movies 
    for films in friends:
        for film in films["watched"]:
            friend_title = film["title"]
            # check that movie title is unique to friends 
            # and not duplicated in friends' unique movie list
            # add unique movies to friend's unique movies list
            if friend_title not in user_movies and (film not in friend_unique_movies):
                friend_unique_movies.append(film)
    
    # return list of movie dictionaries unique to friends
    return friend_unique_movies
            

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # pull out list of subscriptions from user data
    user_subscriptions = user_data["subscriptions"]

    # invoke function to get friends' unique movies
    unique_movies = get_friends_unique_watched(user_data)

    # create empty list for recommended movies
    recommended_movies = []
    
    # iterate through friends' unique movies
    # grab streaming host for that movie
    # check if friend host is in the user's subscriptions
    # then add movie dictionaries to recommended movies list
    for movie in unique_movies:
        friend_host = movie["host"]
        if friend_host in user_subscriptions:
            recommended_movies.append(movie)
    
    # return list of recommended movies for user with same subscriptions 
    return recommended_movies
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    # invoke functions to get most watched genre 
    # and movie dictionaries unique to friends
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    
    # create empty list for recommended movies by genre
    rec_movies_by_genre = []
    
    # iterate through friends' unique movies
    # if the genre is the same as most watched genre
    # add movie dictionary to recommendation list
    for movie in friends_unique_watched:
        if movie["genre"] == most_watched_genre:
            rec_movies_by_genre.append(movie)

    # return recommended movie list of most watched genre    
    return rec_movies_by_genre

def get_rec_from_favorites(user_data):
    # pull out list of user's favorite movie dictionaries
    favorite_movies = user_data["favorites"]
    
    # create empty list for recommended favorite movies
    rec_from_favorites = []
    
    # iterate through user's favorite movies
    # invoke function to check if favorite movies are unique to user
    # add movie dictionary to recommended favorite movies list
    for movie in favorite_movies:
        if movie in get_unique_watched(user_data):
            rec_from_favorites.append(movie)

    # return list of recommended favorite movies     
    return rec_from_favorites
                
