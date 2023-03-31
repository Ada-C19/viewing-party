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

user_data = {
    "watched" : [{
                    "title": "Movie 4",
                    "genre": "Fantasy",
                    "rating": 4.8
                    },
                    {
                    "title": "Movie 5",
                    "genre": "SF",
                    "rating": 4.0
                    },
                    {
                    "title": "Movie 6",
                    "genre": "Horror",
                    "rating": 4.0
                    },
                    {
                    "title": "Movie 7",
                    "genre": "Fantasy",
                    "rating": 3.0
                    },
                    {
                    "title": "Movie 8",
                    "genre": "SF",
                    "rating": 4.8
                    },
                    {
                    "title": "Movie 9",
                    "genre": "SF",
                    "rating": 4.4
                    },
                    {
                    "title": "Movie 10",
                    "genre": "SF",
                    "rating": 4.0
                    },
                    {
                    "title": "Movie 11",
                    "genre": "SF",
                    "rating": 4.1
                    }
                    ],
    "watchlist" : [{
                    "title": "Movie 1",
                    "genre": "SF",
                    "rating": 4.0
                    },
                    {
                    "title": "Movie 2",
                    "genre": "SF",
                    "rating": 5.0
                    },
                    {
                    "title": "Movie 3",
                    "genre": "SF",
                    "rating": 4.0
                    }]
}

def get_watched_avg_rating(user_data):

    if not user_data["watched"]:
        return 0.0
    else:
        total_rating = sum(movie["rating"] for movie in user_data["watched"])
        # return total_rating / len(user_data["watched"])
        test = total_rating / len(user_data["watched"])
        print(f"average {test = }")
        return test
    
get_watched_avg_rating(user_data)

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
    # return max(genre_count, key=lambda genre: genre_count[genre])
    # values = None
    # test = max(genre_count, key=genre_count.get("genre", values))
    test = max(genre_count, key=genre_count.get)
    print(f"most {test = }")
    return test

get_most_watched_genre(user_data)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Wave 3
# Create a function named get_unique_watched. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
# This represents that the user has a list of watched movies and a list of friends
# The value of "friends" is a list
# Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
# Each movie dictionary has a "title".
# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# Return a list of dictionaries, that represents a list of movies
# Create a function named get_friends_unique_watched. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
# This represents that the user has a list of watched movies and a list of friends
# The value of "friends" is a list
# Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
# Each movie dictionary has a "title".
# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
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
    user_movies = set([movie['title'] for movie in user_data['watched']])
    friends_movies = set([movie['title'] for friend in user_data['friends'] for movie in friend['watched']])
    unique_movies = user_movies.difference(friends_movies)
    return [{'title': movie} for movie in unique_movies]


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
    user_movies = set([movie['title'] for movie in user_data['watched']])
    friends_movies = set([movie['title'] for friend in user_data['friends'] for movie in friend['watched']])
    unique_movies = friends_movies.difference(user_movies)
    return [{'title': movie} for movie in unique_movies]
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

user_data = {
    "watched": [
        {"title": "fury", "genre": "action", "rating": 4.5, "host": "amazon"},
        {"title": "love", "genre": "romance", "rating": 4, "host": "netflix"}
    ],
		"subscriptions": ["netflix", "amazon", "hulu"], 
    "friends": [
        {
            "name": "Amy",
            "watched": [
                {"title": "love", "genre": "romance", "rating": 3, "host": "netflix"},
				{"title": "stars", "genre": "fantasy", "rating": 3, "host": "amazon"},
                {"title": "horror movie", "genre": "horror", "rating": 5, "host": "hulu"}
            ]
        },
        {
            "name": "Matt",
            "watched": [
                {"title": "fury", "genre": "action", "rating": 4, "host": "amazon"},
                {"title": "silly", "genre": "comedy", "rating": 3, "host": "disney+"}
            ]
        },
        {
            "name": "Will",
            "watched": [
                {"title": "fury", "genre": "action", "rating": 4.5, "host": "amazon"},
                {"title": "love", "genre": "romance", "rating": 3.5, "host": "netflix"},
								{"title": "stars", "genre": "fantasy", "rating": 3, "host": "amazon"}
            ]
        }
    ]
}

def get_available_recs(user_data):
    recommendations = []
    friend_list = user_data["friends"]
    user_watched_list = user_data["watched"]
    sub_list = user_data["subscriptions"]
    for friend in friend_list:
        for movie in friend["watched"]:
            if movie["host"] in sub_list and movie not in user_watched_list:
                #1. works but adds duplicates, add something here to prevent that
                #2.OR use wave 3 has a helper function? either works!
                recommendations.append(movie)
    return recommendations

# get_available_recs(user_data)
# Wave 4
# Create a function named get_available_recs. This function should...
# take one parameter: user_data
# user_data will have a field "subscriptions". The value of "subscriptions" is a list of strings
# This represents the names of streaming services that the user has access to
# Each friend in "friends" has a watched list. Each movie in the watched list has a "host", which is a string that says what streaming service it's hosted on
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's "subscriptions"
# Return the list of recommended movies

# iterate over FRIENDS:
# check to see if any of their movies != movies in watched
# if their movies are NOT in watched (True)
# check to see if the value to host is in SUBS?
# add those movies to recommended movies
# return recommended movies


# For each friend f in the friends list:
# For each movie m in the watched list of friend f:
# If the user has not watched the movie m 
# and the movie m is hosted on a streaming service that is in the user's subscriptions list:
# Check if the movie m is already in the recs list. If not, add it to the recs list
# Return the recs list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Wave 5
# Create a function named get_new_rec_by_genre. This function should...
# take one parameter: user_data
# Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "genre" of the movie is the same as the user's most frequent genre
# Return the list of recommended movies
# Create a function named get_rec_from_favorites. This function should...
# take one parameter: user_data
# user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
# This represents the user's favorite movies
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The movie is in the user's "favorites"
# None of the user's friends have watched it
# Return the list of recommended movies

def get_new_rec_by_genre(user_data):




    available_recs = []
    user_watchlist = get_unique_watched(user_data)

    # for i in range(len(user_data["favorites"])):
    #     if user_data["favorites"][i] in user_watchlist:
    #         available_recs.append(user_data["favorites"][i])
    # return available_recs
    return user_watchlist




