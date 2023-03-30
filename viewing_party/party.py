# WAVE 1
def create_movie(title, genre, rating):
    movie = {}
    if not title or not genre or not rating:
        return None
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
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

def get_watched_avg_rating(user_data):
    ratings = 0.0
    count_movies = 0
    if not user_data["watched"]:
        return ratings 
    for movie_info in user_data["watched"]:
        if isinstance(movie_info.get("rating"),float):
            ratings += movie_info.get("rating")
            count_movies += 1
    return ratings/count_movies

# 2. Create a function named `get_most_watched_genre`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. Each movie dictionary has a key `"genre"`.
#     - This represents that the user has a list of watched movies. Each watched movie has a genre.
#     - The values of `"genre"` is a string.
# - Determine which genre is most frequently occurring in the watched list
# - return the genre that is the most frequently watched
# - If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.

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

def get_friends_unique_watched(user_data): 
    movie_friend_watched = []
    only_friends_watched = []
    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            if movie not in movie_friend_watched:
                movie_friend_watched.append(movie)
    
    for movie_info in movie_friend_watched:
        if movie_info not in user_data["watched"]:
            only_friends_watched.append(movie_info)
    return only_friends_watched
        
# WAVE 4
def get_available_recs(user_data):
    rec_movies_by_friends = []
    friends_only = get_friends_unique_watched(user_data)
    for movie_info in friends_only: 
        if movie_info["host"] in user_data["subscriptions"]: 
            rec_movies_by_friends.append(movie_info)
    return rec_movies_by_friends

# WAVE 5

# def get_new_rec_by_genre(user_data): 
#     rec_movies_by_genre = []

#     if 'favorites' not in user_data:
#         return recommended_movies_by_genre

#     # to count the occurrences of each genre in user_data
#     for user_movie_info in user_data['favorites']:
#         genre = user_movie_info["genre"]
#         if genre not in most_watched_genre:
#             most_watched_genre[genre] = 1
#         elif genre in most_watched_genre:
#             most_watched_genre[genre] += 1
#     # to find out which genre is the highest

#     # gets the max count in most_watched_genre
#     max_count = 0
#     for genre_and_count in most_watched_genre:
#         if most_watched_genre[genre_and_count] > max_count:
#             max_count = most_watched_genre[genre_and_count]

#     # get the genre with the most frequent watch
#     most_fre_genre = set()
#     for genre_and_count in most_watched_genre:
#         if most_watched_genre[genre_and_count] == max_count:
#             most_fre_genre.add(genre_and_count)

#     user_sub = set()
#     for sub in user_data['subscriptions']:
#         user_sub.add(sub)

#     # add user's watched moveies in a set
#     user_watched_movies = set()
#     for watched_movie in user_data['watched']:
#         user_watched_movies.add(watched_movie['title'])

#     # iterate through friends_watched_moveies and check if user has not watched
#     # and the genre
#     has_seen = set()
#     friends_watched_movies = user_data['friends']
#     for friends_watched_movie in friends_watched_movies:
#         for movie in friends_watched_movie['watched']:
#             if movie['title'] not in user_watched_movies and movie['genre'] in most_fre_genre and movie['host'] in user_sub:
#                 if movie['title'] not in has_seen:
#                     recommended_movies_by_genre.append(movie)
#                     has_seen.add(movie['title'])

#     return recommended_movies_by_genre


# def get_rec_from_favorites(user_data):
#    recommended_movies = []
#    if 'favorites' not in user_data:
#         return recommended_movies
#    if 'friends' not in user_data:
#         return recommended_movies
   
#    # add all friends' watched movies in a set
#    friend_fav_mov = set()
#    for movies in user_data['friends']:
#        for movie in movies['watched']:
#            friend_fav_mov.add(movie['title'])

#    # check if the movie is in user's fav list
#    for movie in user_data['favorites']:
#        if movie['title'] not in friend_fav_mov: 
#            recommended_movies.append(movie)
    
#    return recommended_movies
