# ------------- WAVE 1 -------------------- 
# ========================================= wave 01- # 1. create_movie ========== RC/ SJ

def create_movie(title, genre, rating):
    # movies = {}
    
    # If those three attributes are truthy, 
    # then return a dictionary. 
    # This dictionary should...
    if title and genre and rating:
        # movies.update(new_movies)
        return {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    else:
    # - If `title` is falsy, `genre` is falsy, 
    # or `rating` is falsy, this function should return `None`
        return None
    # return movies


# ========================================= wave 01- # 2. add to watched ========== SJ

# take two parameters: user_data, movie 
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    # print(user_data)
    return user_data

# ========================================= wave 01- # 3. add to watchlist ========== SJ
# take two parameters: user_data, movie

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
            
# ========================================= wave 01- # 4. watch movie ========== RC

def watch_movie(user_data, title):
    # if there's a movie dictionary in watchlist with the title fleabag, remove it from watchlist and add it to watched
    for movie in user_data["watchlist"]:
    # check the title for each element
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            print(user_data)  
            return user_data
    if title not in user_data["watchlist"]:
        return user_data
            

# ========================================= wave 02- # 2. get_most_watched_genre ========== RC

def get_most_watched_genre(user_data):
    # keep the var the same
    watched = user_data["watched"]
    # if movie title not watched, return none
    if not watched:
        return None
    
    # iterate thru each "genre" key's value for the entire length of nested dictionary
    genres_watched = [watched[i]["genre"] for i in range(len(watched))]
    
    # get the most watched genre with max function
    return max(genres_watched, key=genres_watched.count)

# ========================================= wave 02- # 2. get_watched_avg_rating ========== SJ

def get_watched_avg_rating(user_data): 
    
    #  initialize a variable for ratings  set to 0     
    ratings_total = 0
    average_rating = 0

    #  if the length of the user_ data( "watched") is empty  
    if len(user_data["watched"]) == 0: 
        average_rating == 0.0
        return average_rating
    
    else: 
        # loop through movies in the the watched list in user_data
        for movie in user_data["watched"]: 
                            
            #  add the rating to the ratings total 
            ratings_total += movie["rating"]
            print(ratings_total)
            
            #  average rating is ratings_total / length (user_data["watched"]) 
            average_rating = ratings_total/ len(user_data["watched"])
                
    return average_rating

    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# ========================================= wave 03- # 1. get_unique_watched ========== RC

def get_unique_watched(user_data):
    # movies that friends have watched
    friends_watched = {movie['title'] for friend in user_data['friends'] for movie in friend['watched']}

    # movies that ONLY user has watched 
    unique_movies = [movie for movie in user_data['watched'] if movie['title'] not in friends_watched]

    # Return the list of unique movies
    return unique_movies
    
# ========================================= wave 03- # 2. get_friends_unique_watched ========== SJ

# 1. Consider the movies that the user has watched, 
# 2. consider the movies that their friends have watched. 

# Determine which movies at least one of the user's friends have watched, 
# but the user has not watched.

def get_friends_unique_watched(user_data):
    
    # all the movies the user has watched
    user_movies_watched = user_data["watched"]
    
    # the return in the helper function get_friends_movies
    # will return all the movies the friends have watched in a list
    friends_watched_movies = get_friends_movies(user_data)
    
    # if the movie is not in the list of user_movies_watched,
    # then return those movies in a list
    if not user_movies_watched: 
        return []

    #Compare friends' watched movies to own watched movies
    return create_unique_list(friends_watched_movies, user_movies_watched)


# 3. Helper function to compare friends watched to user watched
def create_unique_list(friends_watched_movies, user_movies_watched):
    #Return a list of dictionaries that represent a list of movies 
    # each item in movies that are not in comparison
    
    #  set a variable to an empty list to house 
    # the unique movies the user hasn't watched
    unique_movies = []
    
    # for each movie dictionary that is in the list of friends watched movies, 
    for movie_dict in friends_watched_movies:
        
        # if that movie dictionary is NOT in the list of movies dicts the user watched
        if movie_dict not in user_movies_watched: 
            
            # then add that movie to the list of unique movies
            unique_movies.append(movie_dict)
            
    #  return the list of unique movie dicts
    return unique_movies



#  2. Helper function to get a list of all the movies friends have watched. 
def get_friends_movies(user_data):
    # Return list of movies watched by friends (no duplicates)
    # initialize an empty list for movies the friend has watched. 
    friends_watched = []
    
    # loop through each element in the list 
    # that is set to the value user_data["friends"]
    for list_of_movies in user_data["friends"]:
        
        # so for each movie dictionary in the list of movies your friends have watched, 
        for movie_dict in list_of_movies["watched"]:
            
            # if that movie is NOT in the list the friends have watched
            if movie_dict not in friends_watched: 
                # add it/ append the friends_wacthed list with that movie
                friends_watched.append(movie_dict)
    # return a list with all the movies friends have watched
    return friends_watched



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# ========================================= wave 04- # 1. get_available_recs ========== SJ

# 1. get_available_recs function takes in 1 parameter- user_data
def get_available_recs(user_data):
    
    # 2. initialize the empty list of recommended movies
    #    the goal of the function is to get a list of recommended movies 
    #    so only movies the user has NOT watched will be added to this list
    #    so we initialize a nempty list to have something to hold the 
    #    recommneded movie dicts
    recommended_movies = []
    
    # 3. for the recommended movies-- there are some stipulations: 
    #   the user has NOT watched the movie
    #   At least one of the user's friends has watched the movie
    
    #  4. feel like we did this for the get_friends_unique_watched() function in w3
    #     it returned a list of movies the friends watched that the user had not
    #     so we are looping through each of those unique movies...
    for movie in get_friends_unique_watched(user_data):   
    
        # 5. and if the "host" of the moive is one on the subscription services the user has
        if movie["host"] in user_data["subscriptions"]:
            
            # 6. then we add that movie to the recommended list of movies
            recommended_movies.append(movie)
            
    # 7. return the list of recommended movies. 
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# ========================================= wave 05- # 1.  get_new_rec_by_genre ========== SJ & RC

# Return the list of recommended movies

# Create a function named get_new_rec_by_genre. 
# takes in one parameter: user_data

def get_new_rec_by_genre(user_data):
    # Consider the user's most frequently watched genre.
    # the function get_most_wacthed_genre does this for us....
    users_most_freq_watched_genre = get_most_watched_genre(user_data)
    
    # Then, determine a list of recommended movies. 
    list_of_recommended = []

    
    # to get a list of recommended movies: 
    # - 1. movies the user has NOT watched
    # - 2. movie one of the friends has watched 
    # - 3. the genre of the recommended movies is the same as users most frequent genre

    
    # the function get_friends_unique_watched returns a list of movies
    #  the user's friends have watched but the user has not seen...
    movies_not_watched = get_friends_unique_watched(user_data)
    
    
    # for each movie dictionary in the list of movies not watched, 
    for movie in movies_not_watched:
        
        # if the key "genre" in the movie dictionary is the same genre
        # that is returned in the users_movst_freq_wateched_genre
        if movie["genre"] in users_most_freq_watched_genre:
            
            # add the movie to the list of recs
            list_of_recommended.append(movie)
    
    # then return list of recomneded movies
    return list_of_recommended
    
    
# 2. Create a function named  `get_rec_from_favorites`. This function should...
def get_rec_from_favorites(user_data):
    # Create set of all movies that the user's friends have watched
    friends_watched = set()
    # for each friend's data in user_data.get()
    #  use .get() to get key value
    for friend_data in user_data.get("friends", []):
        # loop through each friend's watched list to extract the movie titles
        friends_watched.update(set(movie["title"] for movie in friend_data.get("watched", [])))
    
    # initialize empty list of recommended movies
    rec_movies = []
    # loop thru each movie in user's faves list
    for movie in user_data.get("favorites", []):
        # Check if movie is not watched by any of user's friends
        if movie["title"] not in friends_watched:
            rec_movies.append(movie)
    
    return rec_movies