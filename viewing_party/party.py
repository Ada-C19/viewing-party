# WAVE 1
def create_movie(title, genre, rating):
    movie = {}
    if title is None or genre is None or rating is None:
        return None
    if title is False or genre is False or rating is False:
        return None
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    print(movie)
    return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movies in user_data["watchlist"]:
        if title == movies["title"]:
            user_data["watched"].append(movies)
            user_data["watchlist"].remove(movies)
    return user_data

# WAVE 2

# WAVE 3


def get_unique_watched(user_data):
    friends_watched_movie = set()
    user_watched_movie = []
    unique_movie_watched = []
    # generate a set with movie titles from friend's watched lists
    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            friends_watched_movie.add(movie["title"])
   # generate a list of dictionaries with watched user movie info
    for user_movies in user_data["watched"]:
        user_watched_movie.append(user_movies)
    # Check to see if the user movie title is within the whole set of friend's watched list
    for movie_info in user_watched_movie:
        if movie_info["title"] not in friends_watched_movie:
            unique_movie_watched.append(movie_info)
    return unique_movie_watched

# WAVE 4
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
    # find the subscriptions user has
    for ott in user_data["subscriptions"]:
        user_subscription.add(ott)
    print(f"subscription:{user_subscription}")
    # create a set with user's watched movie list
    for user_movie_info in user_data["watched"]:
         user_watched_movies.add(user_movie_info["title"])
    print(f"user movie titles:{user_watched_movies}")
    # create a list of dictionaries with friend's watched movies
    for list in user_data["friends"]:
        for movie_info in list["watched"]:
            if movie_info not in friends_watched_movies:
                friends_watched_movies.append(movie_info)
    print(f"friends movie info: {friends_watched_movies}")
    # generate a recommended list by checking to see if user did not watch movies that the friend did and
    # if the OTT platform user subscribed to has it
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

# WAVE 5
# 1. Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then,
# determine a list of recommended movies.
# A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies


def get_new_rec_by_genre(user_data):

    print("user_data", user_data)

    recommended_movies_by_genre = []
    most_watched_genre = {}

    if 'favorites' not in user_data:
        return recommended_movies_by_genre

    # to count the occurrences of each genre in user_data
    for user_movie_info in user_data['favorites']:
        genre = user_movie_info["genre"]
        if genre not in most_watched_genre:
            most_watched_genre[genre] = 1
        elif genre in most_watched_genre:
            most_watched_genre[genre] += 1
    # to find out which genre is the highest

    # gets the max count in most_watched_genre
    max_count = 0
    for genre_and_count in most_watched_genre:
        if most_watched_genre[genre_and_count] > max_count:
            max_count = most_watched_genre[genre_and_count]

    # get the genre with the most frequent watch
    most_fre_genre = set()
    for genre_and_count in most_watched_genre:
        if most_watched_genre[genre_and_count] == max_count:
            most_fre_genre.add(genre_and_count)

    user_sub = set()
    for sub in user_data['subscriptions']:
        user_sub.add(sub)

    # add user's watched moveies in a set
    user_watched_movies = set()
    for watched_movie in user_data['watched']:
        user_watched_movies.add(watched_movie['title'])

    # iterate through friends_watched_moveies and check if user has not watched
    # and the genre
    has_seen = set()
    friends_watched_movies = user_data['friends']
    for friends_watched_movie in friends_watched_movies:
        for movie in friends_watched_movie['watched']:
            if movie['title'] not in user_watched_movies and movie['genre'] in most_fre_genre and movie['host'] in user_sub:
                if movie['title'] not in has_seen:
                    recommended_movies_by_genre.append(movie)
                    has_seen.add(movie['title'])

    return recommended_movies_by_genre


def get_rec_from_favorites(user_data):
   recommended_movies = []

   # if "favorites" is not in user_data
   if 'favorites' not in user_data:
        return recommended_movies
   
   # if "friends" is not in user_data
   if 'friends' not in user_data:
        return recommended_movies

   # add all friends' watched movies in a set
   friend_fav_mov = set()
   for movies in user_data['friends']:
       for movie in movies['watched']:
           friend_fav_mov.add(movie['title'])

   # check if the movie is in user's fav list
   for movie in user_data['favorites']:
       if movie['title'] not in friend_fav_mov: 
           recommended_movies.append(movie)
    
   return recommended_movies
