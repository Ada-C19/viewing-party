# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    '''
    input: title, genre, rating of a movie
    output: movie dictionary with 3 keys
    '''
    if not title:
        return None
    if not genre: 
        return None
    if not rating:
        return None
    
    movie_dict = {'title': title, 'genre': genre, 'rating': rating}

    return movie_dict
        

def add_to_watched(user_data, movie):
    '''
    input: user_data with a key for "watched" , movie
    output: user_data with movie passed in added
    '''
    movies_user_has_watched = user_data["watched"]
    # append (represent) movie to list of dict
    movies_user_has_watched.append(movie)
    
    return user_data


def add_to_watchlist(user_data, movie):
    '''
    input: user_data with a key for "watchlist", movie
    output: user_data with movie added to the "watchlist
    '''
    movies_user_wants_to_watch = user_data["watchlist"]
    
    if movies_user_wants_to_watch is None:
        # an empty list rep that the user has no movies in their watchlist
        movies_user_wants_to_watch = []
    # append (represent) movie to list of dict
    movies_user_wants_to_watch.append(movie)

    return user_data


def watch_movie(user_data, title):
    '''
    input: user_data is a dictionary with a "watchlist" and a "watched" list of movies;
    output: user_data with a movie that moves from "watchlist" to "watched"
    '''
    user_watchlist_movies = user_data["watchlist"]
    watched_movies = user_data["watched"]
 
    # iterate through the watchlist to find if movie in there 
    for movie in user_watchlist_movies:
    #if movie is already in watchlist, remove it and add it to watched movies
        if title == movie['title']:
            user_watchlist_movies.remove(movie)
            watched_movies.append(movie)
    
    return user_data
            
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries
    output: average rating of all movies in the "watched" list, where empty list has a value of 0.0
    '''
    #initiate sum to 0.0 and guard against an empty watched list
    sum = 0.0
    if not user_data['watched']:
        return sum
    
    #grab values of rating from each movie dictionary and add them to the sum
    for movie in user_data['watched']:
        sum += movie['rating']
        
    #return average (sum / # of watched movies)
    return sum / len(user_data['watched'])
    

def get_most_watched_genre(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of; each movie has a "genre" key
    output: genre that's most frequently watched from the watched list. Return None if "watched" is empty
    ''' 
    genre_dict = {}
    #guard against an empty watched list
    if not user_data['watched']:
        return None

    #add genre of each watched movie as a key, adding to its frequency everytime 
    for movie in user_data['watched']:
        movie_genre = movie['genre']

        #if the genre is not in genre_dict, add it as a key with a value of 1, else, add to genre frequency
        if not movie_genre in genre_dict:
            genre_dict[movie_genre] = 1
        else:
            genre_dict[movie_genre] += 1
    
    #return genre with highest value from genre_dict
    most_popular_genre = max(genre_dict, key=genre_dict.get)
    
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries and a "friends" list
    output: list of dictionaries that represents a list of movies that user has uniquely watched, ("friends" have not)
    '''          
    user_watched_movies = user_data['watched']
    friends_watched_movies = user_data['friends']
    friend_movie_list = []
    
    if len(friends_watched_movies) == 0:
        return user_watched_movies
    
    #iterate through the list of movies that friends have watched
    for movie in friends_watched_movies: 
        friend_movie_list += movie["watched"]
        #initialize an empty list for unique movies
        unique_watched_movies =  []

    #iterate through the list of movies the user has watched
        for movie in user_watched_movies:
            #if the movie hasn't been watched by friends and it's not yet in the list of unique movies they've watched
            if movie not in friend_movie_list and movie not in unique_watched_movies:
                #add movie to unique movies, guard against duplicates
                unique_watched_movies.append(movie)
                
    return unique_watched_movies


def get_friends_unique_watched(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries and a "friends" list
    output: list of movies that at least one friend has watched but user has not
    '''
    user_watched_movies = user_data['watched']
    list_of_friends = user_data['friends']
    friend_unique_watched_movies = []
    
    #iterates through all of the friends in the list
    for friend in list_of_friends: 
        #for each friend, iterate to find what each of them has watched         
        for movie in friend["watched"]:
            #if the movie isn't something the user has watched and hasn't yet beed added to the friends unique list, add it
            if movie not in user_watched_movies and movie not in friend_unique_watched_movies:
                friend_unique_watched_movies.append(movie)
    
    return friend_unique_watched_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    '''
    input: user_data with a field for "subscriptions"; "friends" watchlist now has a field for "host" that outlines streaming service
    output: movie recommendations for user if they haven't watched it yet and its a subscription they have
    '''
    recs = []
    friends = user_data['friends']
    user_watched_movies = user_data['watched']
    service_subscriptions = user_data['subscriptions']

    #iterate through each friend to get a list of the movies they've watched
    for friend in friends:
        friend_movie_list = friend['watched']
        
        #iterate through each movie friends have watched to look for the host
        for movie in friend_movie_list:
            movie_host = movie['host']
            #if the movie host is also in the subscriptions that the user has; the user hasn't watched the movie yet
            if movie_host in service_subscriptions and movie not in user_watched_movies and movie not in recs:
                #add movie to recs, guarding for duplicates
                recs.append(movie)

    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''
    input: user_data which includes "friends" list of watched movies 
    output: a recommended list of movies for the user, if they haven't watched it and it matches their most frequent genre
    '''
    recommended_movies = []
    user_watched_movies = user_data['watched']
    user_frequently_watched_genre = get_most_watched_genre(user_data)
    friends_watched_movies = get_friends_unique_watched(user_data)
    
    # go through the list of movies that only friends have watched
    for movie in friends_watched_movies:
        #get the genre of the movie
            movie_genre = movie['genre']
            # if the movie isn't one that the user has watched and the movie genre matches their favorite:
            if not movie in user_watched_movies and movie_genre == user_frequently_watched_genre:
                #append the movie to the recommended list
                recommended_movies.append(movie)
                
    return recommended_movies

    
def get_rec_from_favorites(user_data):
    '''
    input: user_data with a "favorites" movie list
    output: a recommended list of movies for friends, if it's in the "favorites" list and none of the friends have watched it yet
    '''
    user_watched_movies = get_unique_watched(user_data)
    favorite_movies = user_data['favorites']
    reccommended_from_favorites = []

    #iterate through each movie in favorites list
    for movie in favorite_movies:
        #append movies to the recommendations if it's in the favorites list and the user has uniquely watched it
        if movie in user_watched_movies:
            reccommended_from_favorites.append(movie)
            
    return reccommended_from_favorites