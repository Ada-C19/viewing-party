# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # check if title, genre, or rating is falsy
    if (not title) or (not genre) or (not rating):
        # return None
        return None
    # check if title_value and genre_value are string, rating is a float
    if (not isinstance(title, str)) or (not isinstance(genre, str)) or (not isinstance(rating, float)):
        # raise ValueError("Invalid input")
        return None
    # initialize empty dictionary
    new_movie = {}

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = float(rating)

    return new_movie


# create_movie("Scream 6", "Horror", 4.0)


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


movie = {
    "title": "Lion King",
    "genre": "Family",
    "rating": 5.0
}
user_data = {"watched": []}

# add_to_watched(user_data, movie)


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


movie = {
    "title": "Title A",
    "genre": "Horror",
    "rating": 3.5
}
user_data = {
    "watchlist": []
}
# add_to_watchlist(user_data, movie)


def watch_movie(user_data, title):
    # iterate through each movie dictionary in the list
    for movie in user_data["watchlist"]:
        # checks if the title entered is found inside of the watchlist
        # Changed "in" to "=="" to avoid title being seen as a substring of
        # a similar movie title (e.g. Super Man vs Super Man 2)
        if title == movie["title"]:
            # move_movie captures the current movie found to be moved
            move_movie = movie
            # updates user_data to remove current movie from watchlist
            user_data["watchlist"].remove(movie)
            # updates user_data to add current movie to watched
            user_data["watched"].append(move_movie)
    # returns updated user_data
    return user_data


janes_data = {
    "watchlist": [{
        "title": "Super Man 2",
        "genre": "Action",
        "rating": 4.0
    }],
    "watched": []
}
# watch_movie(janes_data, "Super Man")

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    sum = 0
    if not user_data["watched"]:
        return 0.0

    for movie in user_data["watched"]:
        try:
            sum += movie["rating"]
        except TypeError:
            return f"The rating for {movie['title']} is invalid"

    return sum/len(user_data["watched"])


def get_most_watched_genre(user_data):
    genre_list = []

    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        if isinstance(movie["genre"], str):
            genre_list.append(movie["genre"])
        else:
            return f"Invalid genre for {movie['title']}"

    return max(genre_list, key=genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    friend_watched = set()
    user_watched = []

    for friend_dict in user_data["friends"]:
        for movie_dict in friend_dict["watched"]:
            friend_movie_title = movie_dict["title"]
            friend_watched.add(friend_movie_title)

    for user_dict in user_data["watched"]:
        user_title = user_dict["title"]
        if user_title not in friend_watched:
            user_watched.append(user_dict)

    return user_watched


def get_friends_unique_watched(user_data):
    friend_watched = []
    friend_watched_titles = []
    user_watched = []

    for user_dict in user_data["watched"]:
        user_title = user_dict["title"]
        user_watched.append(user_title)

    for friend_dict in user_data["friends"]:
        for movie_dict in friend_dict["watched"]:
            friend_movie_title = movie_dict["title"]
            if (friend_movie_title not in friend_watched_titles and
                    friend_movie_title not in user_watched):
                friend_watched_titles.append(friend_movie_title)
                friend_watched.append(movie_dict)

    return friend_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []
    friend_only_watched = get_friends_unique_watched(user_data)
    for movie in friend_only_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommendations = []
    most_watched_genre = get_most_watched_genre(user_data)
    friend_only_watched = get_friends_unique_watched(user_data)

    for movie in friend_only_watched:
        if movie["genre"] == most_watched_genre:
            recommendations.append(movie)
    print(recommendations)
    return recommendations


sonyas_data = sonyas_data = {
    "watched": [{
        "title": "Recursion",
        "genre": "Intrigue",
        "rating": 2.0,
        'host': 'hulu'
    }],
    "friends": [
        {
            "watched": []
        },
        {
            "watched": []
        }
    ]
}

get_new_rec_by_genre(sonyas_data)


def get_rec_from_favorites(user_data):
    recommendations = []
    only_user_watched = get_unique_watched(user_data)

    for fave_movie in user_data['favorites']:
        for movie in only_user_watched:
            if movie["title"] == fave_movie["title"]:
                recommendations.append(fave_movie)
    return recommendations


user_data = {'favorites': [{'genre': 'Fantasy',
                            'host': 'netflix',
                            'rating': 4.8,
                                     'title': 'The Lord of the Functions: The Fellowship '
                                     'of the Function'},
                           {'genre': 'Fantasy',
                               'host': 'netflix',
                               'rating': 4.0,
                               'title': 'The Lord of the Functions: The Two '
                            'Parameters'},
                           {'genre': 'Intrigue',
                            'host': 'hulu',
                            'rating': 2.0,
                            'title': 'Recursion'},
                           {'genre': 'Intrigue',
                            'host': 'disney+',
                            'rating': 4.5,
                            'title': 'Instructor Student TA Manager'}],
             'friends': [{'watched': [{'genre': 'Fantasy',
                                       'host': 'netflix',
                                       'rating': 4.8,
                                       'title': 'The Lord of the Functions: '
                                       'The Fellowship of the '
                                       'Function'},
                                      {'genre': 'Fantasy',
                                       'host': 'amazon',
                                       'rating': 4.0,
                                       'title': 'The Lord of the Functions: '
                                       'The Return of the Value'},
                                      {'genre': 'Fantasy',
                                       'host': 'hulu',
                                       'rating': 4.0,
                                       'title': 'The Programmer: An '
                                       'Unexpected Stack Trace'},
                                      {'genre': 'Horror',
                                       'host': 'netflix',
                                       'rating': 3.5,
                                       'title': 'It Came from the Stack '
                                       'Trace'}]},
                         {'watched': [{'genre': 'Fantasy',
                                       'host': 'netflix',
                                       'rating': 4.8,
                                       'title': 'The Lord of the Functions: '
                                       'The Fellowship of the '
                                       'Function'},
                                      {'genre': 'Fantasy',
                                       'host': 'hulu',
                                       'rating': 4.0,
                                       'title': 'The Programmer: An '
                                       'Unexpected Stack Trace'},
                                      {'genre': 'Action',
                                       'host': 'amazon',
                                       'rating': 2.2,
                                       'title': 'The JavaScript and the '
                                       'React'},
                                      {'genre': 'Intrigue',
                                       'host': 'hulu',
                                       'rating': 2.0,
                                       'title': 'Recursion'},
                                      {'genre': 'Intrigue',
                                       'host': 'disney+',
                                       'rating': 3.0,
                                       'title': 'Zero Dark Python'}]}],
             'subscriptions': ['netflix', 'hulu'],
             'watched': [{'genre': 'Fantasy',
                          'host': 'netflix',
                          'rating': 4.8,
                          'title': 'The Lord of the Functions: The Fellowship of '
                          'the Function'},
                         {'genre': 'Fantasy',
                          'host': 'netflix',
                          'rating': 4.0,
                          'title': 'The Lord of the Functions: The Two '
                          'Parameters'},
                         {'genre': 'Fantasy',
                          'host': 'amazon',
                          'rating': 4.0,
                          'title': 'The Lord of the Functions: The Return of the '
                          'Value'},
                         {'genre': 'Action',
                          'host': 'amazon',
                          'rating': 2.2,
                          'title': 'The JavaScript and the React'},
                         {'genre': 'Intrigue',
                          'host': 'hulu',
                          'rating': 2.0,
                          'title': 'Recursion'},
                         {'genre': 'Intrigue',
                          'host': 'disney+',
                          'rating': 4.5,
                          'title': 'Instructor Student TA Manager'}]}
get_rec_from_favorites(user_data)
