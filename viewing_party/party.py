# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not (title and genre and rating):
        return None
    else:
        movie = { "title" : title,
                    "genre" : genre,
                    "rating" : rating}
        return movie
    
def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break

    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if not user_data["watched"]:
        return 0.0
    else:
        total_rating = sum(movie["rating"] for movie in user_data["watched"])
        # return total_rating / len(user_data["watched"])
        test = total_rating / len(user_data["watched"])
        print(f"average {test = }")
        return test
    

def get_most_watched_genre(user_data):

    if not user_data["watched"]:
        return None
    
    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    return max(genre_count, key=lambda genre: genre_count[genre])
    # values = None
    # test = max(genre_count, key=genre_count.get("genre", values))
    # test = max(genre_count, key=genre_count.get)
    # print(f"most {test = }")
    # return test


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Wave 3

# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# Return a list of dictionaries, that represents a list of movies
# For get_unique_watched:

# Get the list of movies that the user has watched.
# Create an empty set to hold the titles of all the movies that the user's friends have watched.
# For each friend in the user's "friends" list:
# For each movie that the friend has watched:
# Add the movie title to the set of movies that the user's friends have watched.
# Create an empty list to hold the movies that the user has watched but none of their friends have watched.
# For each movie that the user has watched:
# If the title of the movie is not in the set of movies that the user's friends have watched:
# Add the movie to the list of movies that the user has watched but none of their friends have watched.
# Return the list of movies.

def get_unique_watched(user_data):
    # user_movies = user_data["watched"]
    # friend_movies = user_data["friends"]
    # unique_movies = []

    # for user_movie in user_movies:
    #     movies_watched_by_friends = []
    #     for friend in friend_movies:
    #         for friend_movie in friend["watched"]:
    #             if user_movie != friend_movie:
    #                 movies_watched_by_friends.append(friend_movie)

    #     if user_movie not in movies_watched_by_friends:
    #         unique_movies.append(user_movie)

    user_movies = user_data["watched"]
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)

    unique_movies = []

    for user_movie in user_movies:
        if user_movie not in friend_movies and user_movie not in unique_movies:
            unique_movies.append(user_movie)

    print(f"{unique_movies = }")
    return unique_movies

    # user_movies = set([movie['title'] for movie in user_data['watched']])
    # friends_movies = set([movie['title'] for friend in user_data['friends'] for movie in friend['watched']])
    # unique_movies = user_movies.difference(friends_movies)
    # unique_movies = [{'title': movie} for movie in unique_movies]
    # print(f"{unique_movies = }")
    # return unique_movies

# get_unique_watched(user_data)

# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# Return a list of dictionaries, that represents a list of movies

# For get_friends_unique_watched:

# Get the list of movies that the user has watched.
# Create an empty set to hold the titles of all the movies that the user's friends have watched.
# For each friend in the user's "friends" list:
# For each movie that the friend has watched:
# Add the movie title to the set of movies that the user's friends have watched.
# Create an empty list to hold the movies that at least one of the user's friends has watched but the user has not watched.
# For each movie that the user's friends have watched:
# If the title of the movie is not in the list of movies that the user has watched:
# If the title of the movie is not already in the list of movies that at least one of the user's friends have watched:
# Add the movie to the list of movies that at least one of the user's friends have watched but the user has not watched.
# Return the list of movies.

def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
            
    unique_movies = []

    for friend_movie in friend_movies:
        if friend_movie not in user_movies and friend_movie not in unique_movies:
            unique_movies.append(friend_movie)

    # print(f"{unique_movies = }")
    return unique_movies



#     user_movies = set([movie['title'] for movie in user_data['watched']])
#     friends_movies = set([movie['title'] for friend in user_data['friends'] for movie in friend['watched']])
#     unique_movies = friends_movies.difference(user_movies)
#     return [{'title': movie} for movie in unique_movies]
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movies_not_watched = get_friends_unique_watched(user_data)
    print(f"{movies_not_watched = }")
    recommendations = []
    sub_list = user_data["subscriptions"]
    for movie in movies_not_watched:
        if movie["host"] in sub_list:
                #1. works but adds duplicates, add something here to prevent that
                #2.OR use wave 3 has a helper function? either works!
                recommendations.append(movie)
    return recommendations

# get_available_recs(user_data)


    # recommendations = []
    # friend_list = user_data["friends"]
    # user_watched_list = user_data["watched"]
    # sub_list = user_data["subscriptions"]
    # for friend in friend_list:
    #     for movie in friend["watched"]:
    #         if movie["host"] in sub_list and movie not in user_watched_list:
    #             #1. works but adds duplicates, add something here to prevent that
    #             #2.OR use wave 3 has a helper function? either works!
    #             recommendations.append(movie)
    # return recommendations

# get_available_recs(user_data)
# Wave 4




# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's "subscriptions"
# Return the list of recommended movies



# For each friend in the friends list:
# For each movie in the watched list of friend:
# If the user has not watched the movie m 
# and the movie is hosted on a streaming service that is in the user's subscriptions list:
# Check if the movie is already in the recs list. If not, add it to the recs list
# Return the recs list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Wave 5


# A movie should be added to this list if and only if:


# The "genre" of the movie is the same as the user's most frequent genre
# Return the list of recommended movies



def get_new_rec_by_genre(user_data):

    recommendations = []
    not_watched_yet = get_friends_unique_watched(user_data)
    fav_genre = get_most_watched_genre(user_data)
    # print(f"{not_watched_yet = }")
    # print(f"{fav_genre = }")

    for movie in not_watched_yet:
        if movie["genre"] == fav_genre:
            recommendations.append(movie)
    # print(f"{recommendations = }")
    return recommendations
# get_new_rec_by_genre(user_data)

def get_rec_from_favorites(user_data):
    print(f"{user_data = }")
    recommendations = []
    favorites = user_data["favorites"]
    print(f"{favorites = }")
    user_unique = get_unique_watched(user_data)

    for movie in user_unique:
            if movie in favorites:
                recommendations.append(movie)
    print(f"{recommendations = }")

    return recommendations
# get_rec_from_favorites(user_data)


# user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
# This represents the user's favorite movies
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The movie is in the user's "favorites"
# None of the user's friends have watched it get_unique_watched(user_data):
# Return the list of recommended movies