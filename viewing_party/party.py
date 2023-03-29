# WAVE 1 


# WAVE 2 

#WAVE 3 
def get_unique_watched(user_data):
    friends_watched_movie = set()
    user_watched_movie = []
    unique_movie_watched = []
    #generate a set with movie titles from friend's watched lists
    for watched_list in user_data["friends"]: 
        for movie in watched_list["watched"]:
            friends_watched_movie.add(movie["title"])
   #generate a list of dictionaries with watched user movie info
    for user_movies in user_data["watched"]: 
        user_watched_movie.append(user_movies)
    #Check to see if the user movie title is within the whole set of friend's watched list 
    for movie_info in user_watched_movie: 
        if movie_info["title"] not in friends_watched_movie:
            unique_movie_watched.append(movie_info)
    return unique_movie_watched
             
#WAVE 4 
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies
def get_available_recs(user_data):
    recommended_movies = []
    user_subscription = set()
    user_watched_movies = set()
    friends_watched_movies = []
    #find the subscriptions user has 
    for ott in user_data["subscriptions"]: 
        user_subscription.add(ott)
    print(f"subscription:{user_subscription}")
    # create a set with user's watched movie list 
    for user_movie_info in user_data["watched"]: 
         user_watched_movies.add(user_movie_info["title"])
    print(f"user movie titles:{user_watched_movies}")
    #create a list of dictionaries with friend's watched movies 
    for list in user_data["friends"]:
        for movie_info in list["watched"]:
            if movie_info not in friends_watched_movies:
                friends_watched_movies.append(movie_info)
    print(f"friends movie info: {friends_watched_movies}")
    #generate a recommended list by checking to see if user did not watch movies that the friend did and
    #if the OTT platform user subscribed to has it 
    for movie_info in friends_watched_movies: 

        # check the movie is not in user_watched_movies and its host is in user_subscription
        if movie_info["title"] not in user_watched_movies and movie_info["host"] in user_subscription: 
            recommended_movies.append(movie_info)
            # rec_with_duplicates.add(movie_info["title"])
    
    #     if movie_info["title"] in rec_with_duplicates:
    #         recommended_movies.append(movie_info)
    # print(rec_with_duplicates)
    # print(f"final:{recommended_movies}")
    return recommended_movies
    
#WAVE 5 
