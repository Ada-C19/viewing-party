
# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    '''
    input: title, genre, rating
    output: dictionary
    '''
    if not title:
        return None
    if not genre: 
        return None
    if not rating:
        return None
    
    movie_dict = {'title': title, 'genre': genre, 'rating': rating}
    # I think these 2 lines don't guard against anything (lines 8-13 do)
    # if movie_dict == False:
    #     return None
    return movie_dict
        

def add_to_watched(user_data, movie):
    #user_data is a dict with key "watched"
    movies_user_has_watched = user_data["watched"]
    # a list of dicts rep the movies the user has watched
    # append (represent) movie to list of dict
    movies_user_has_watched.append(movie)
    #add movie to the "movies_user_has_watched" inside of user data

    return user_data


def add_to_watchlist(user_data, movie):
    # user_data is a dict with key "watchlist"
    movies_user_wants_to_watch = user_data["watchlist"]
    if movies_user_wants_to_watch is None:
        # an empty list rep that the user has no movies in their watchlist
        movies_user_wants_to_watch = []
        # a list of dicts rep the movies the user has watched
    # append (represent) movie to list of dict
    movies_user_wants_to_watch.append(movie)

    return user_data


def watch_movie(user_data, title):
    '''
    input: user_data is a dictionary with a "watchlist" and a "watched" list of movies;
    title is a string representing the title of the movie the user has watched
    output: user_data
    '''
    # value user_data dictionary with "watchlist"
    user_watchlist_movies = user_data["watchlist"]
    # value user_data dictionary with "watched"
    watched_movies = user_data["watched"]
    # this represents the title of the movie the user has watched
    for watchlist_dict in user_watchlist_movies:
        # if this title is in the users watchlist
        # is title = title of watch_dict 
        if title == watchlist_dict['title']:
            user_watchlist_movies.remove(watchlist_dict)
            watched_movies.append(watchlist_dict)
    return user_data
            
            # value of key called title

# If the title is in a movie in the user's watchlist:
# remove that movie from the watchlist
# add that movie to watched
# return the user_data

#Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions 
# should not modify user_data. .copy() or .deepcopy() possibly

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries
    # calculate the average rating of all movies in the watched list
    # an empty "watched" list has a value of 0.0
    output: average rating 
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
    
    # #user_data is a dict with "watched" list of dict
    # user_list_of_watched_movies = user_data["watched"]
    # #calc th avg rating of all movies in the watched list
    # for i in range(len(user_data)):
    #     sum(user_list_of_watched_movies)
# }
def get_most_watched_genre(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries. 
    # each movie dictionary has a key 'genre' which is a string
    # determine which genre is the most frequently occurring in the 'watched' list 
    # if the value of 'watched' is an empty string, function should return None
    output: genre that's most frequently watched 
    ''' 
    #initialize a dictionary that will store genres of all watched movies
    genre_dict = {}
    #guard against an empty watched list
    if not user_data['watched']:
        return None

    #add genre of each watched movie as a key, adding to its frequency everytime 
    for movie in user_data['watched']:
        #get the genre of the movie
        movie_genre = movie['genre']

        #if the genre is not in genre_dict, add it as a key with a value of 1
        #else genre is in genre_dict, increase value by 1
        if not movie_genre in genre_dict:
            genre_dict[movie_genre] = 1
        else:
            genre_dict[movie_genre] += 1

    most_popular_genre = max(genre_dict, key=genre_dict.get)
    #return genre with highest value from genre_dict
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries and a "friends"
    # user_data represents a list of watched movies and a list of friends 
    # each item in "friends" is a dictionary that has a key "watched"  with a list of movie dictionaries  
    # each movie dictionary has a "title" 
    # function should determine which movies the the user has uniquely watched, friends have not watched it
    output: list of dictionaries that represents a list of movies 
    '''          
    list_watched_movies = user_data['watched']
    list_of_friends = user_data['friends']
    friend_movie_list = []
    
    for movie in list_of_friends: 
        friend_movie_list += movie["watched"]
        unique_watched_movies =  []

        for movie in list_watched_movies:
            if movie not in friend_movie_list and movie not in unique_watched_movies:
                unique_watched_movies.append(movie)
    return unique_watched_movies


def get_friends_unique_watched(user_data):
    '''
    input: user_data is a dictionary with a "watched" list of movies dictionaries and a "friends"
    # user_data represents a list of watched movies and a list of friends 
    # each item in "friends" is a dictionary that has a key "watched"  with a list of movie dictionaries  
    # each movie dictionary has a "title" 
    # function should determine which movies at least one of the friends has watched, user has not watched it
    output: list of dictionaries that represents a list of movies 
    '''
    #grab a list of all the movies the user has watched
    list_watched_movies = user_data['watched']
    #grabs a list of watched dictionaries for friends
    list_of_friends = user_data['friends']
    
    friend_movie_list = []
    
    for movie in list_of_friends: 
        #iterates through all of the movies friends have watched
        friend_movie_list += movie["watched"]
        #friend_movie_list prints all of the movies all friends have watched 
        friend_unique_watched_movies = []
        for movie in friend_movie_list:
            if movie not in list_watched_movies and movie not in friend_unique_watched_movies:
                friend_unique_watched_movies.append(movie)
    return friend_unique_watched_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

