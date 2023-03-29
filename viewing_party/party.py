import pprint
pp = pprint.PrettyPrinter(indent=4)
import copy

HORROR_1 = {
    "title": "MOVIE_TITLE_1",
    "genre": "GENRE_1",
    "rating": 1
}
FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}
FANTASY_2 = {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_3 = {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_4 = {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
}
ACTION_1 = {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}
ACTION_2 = {
    "title": "2 JavaScript 2 React",
    "genre": "Action",
    "rating": 4.2
}
ACTION_3 = {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5
}
INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}
INTRIGUE_2 = {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
INTRIGUE_3 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}
USER_DATA_3 = { "watched": [FANTASY_3,
                FANTASY_4,
                HORROR_1],
            "friends" : [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1,
            ]
        },
        {
            "watched": [
                FANTASY_1,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
            ]
        }
]}  




# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # Input validation
    if not title or not genre or not rating:
        return None
    
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # Return the dictionary
    return movie

def add_to_watched(user_data, movie):
    if not movie:
        return user_data

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    if not movie:
        return user_data
    
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    # if item in list
    for i in range(len(user_data['watchlist'])):
        title_from_dict = user_data['watchlist'][i]['title']
    # print("TITLE:", title)

    # If title is in watchlist, remove that movie from watchlist
        if title_from_dict == title:
            dict_from_list = user_data['watchlist'][i]
            user_data["watchlist"].remove(dict_from_list)
            # Add that movie to "watched"
            user_data["watched"].append(dict_from_list)
        print(user_data)
        print("USER DATA WATCHLIST:", user_data['watchlist'])
    return user_data


# print(watch_movie({
#             "watchlist": [{
#                 "title": "Scooby Doo",
#                 "genre": "GENRE_1",
#                 "rating": 1
#             }],
#             "watched": []
#         }, "Scooby Doo"))


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):

    if user_data["watched"] == []:
        return 0.0

    total_rating = 0
    
    for i in range(len(user_data["watched"])):
        rating_from_dict = user_data['watched'][i]['rating']
        total_rating += rating_from_dict
    num_of_movies = len(user_data["watched"])
    return total_rating / num_of_movies

# print(get_watched_avg_rating({'watchlist': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}], 'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]}))
    
def get_most_watched_genre(user_data):
    genres_most_watched = {}

    # Iterate through "watched" list
    for i in range(len(user_data['watched'])):
        genre = user_data['watched'][i]['genre']
        if genre in genres_most_watched:
            genres_most_watched[genre] += 1
        else:
            genres_most_watched[genre] = 1

    highest_occurence = 0
    most_watched = None

    # Iterate through out genres_most_watched dict
    for genre, num in genres_most_watched.items():
        if num > highest_occurence:
            highest_occurence = num
            most_watched = genre
            
    return most_watched


# print(get_most_watched_genre({'watchlist': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}], 'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]}))
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    copy_from_user_data = copy.deepcopy(user_data)
    
    friends_movie_titles = []
    users_movie_titles = []
    my_list = copy_from_user_data["watched"]
    friends_list = copy_from_user_data["friends"]
    
    for i in range(len(friends_list)):
        values_of_watched = friends_list[i]["watched"]
        print(values_of_watched)
        for j in range(len(values_of_watched)):
            titles = values_of_watched[j]["title"]
            friends_movie_titles.append(titles)

    for i in range(len(my_list)):
        users_movie_titles.append(my_list[i]["title"])

    user_unique_movies = set(users_movie_titles) - set(friends_movie_titles)
    users_unique_movies_list = list(user_unique_movies)
    print(users_unique_movies_list)
    
    result_list = []

    for movie_title in users_unique_movies_list:
        for movie in my_list:
            if movie["title"] == movie_title:
                result_list.append(movie)

    return result_list

# print(get_unique_watched(USER_DATA_3))

def get_friends_unique_watched(user_data):

    copy_from_user_data = copy.deepcopy(user_data)
    
    friends_movie_titles = []
    users_movie_titles = []
    friends_movies = []
    my_list = copy_from_user_data["watched"]
    friends_list = copy_from_user_data["friends"]
    
    for i in range(len(friends_list)):
        values_of_watched = friends_list[i]["watched"]
        print(values_of_watched)
        for j in range(len(values_of_watched)):
            titles = values_of_watched[j]["title"]
            friends_movie_titles.append(titles)
            friends_movies.append(values_of_watched[j])

    for i in range(len(my_list)):
        users_movie_titles.append(my_list[i]["title"])

    friends_unique_movies = set(friends_movie_titles) - set(users_movie_titles)
    friends_unique_movies_list = list(friends_unique_movies)
    print(friends_unique_movies_list)
    
    result_list = []

    for movie_title in friends_unique_movies_list:
        for movie in friends_movies:
            if movie["title"] == movie_title:
                result_list.append(movie) 
                break

    return result_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    friends_list = user_data["friends"]
    user_watched = user_data["watched"]
    user_watched_titles = []

    # Iterate through user's watched dicts and get the titles user has watched
    for i in range(len(user_watched)):
        user_watched_titles.append(user_watched[i]["title"])

    movie_recs = []
    for dict in friends_list:
        for value in dict.values():
            for movie in value:
                friends_title = movie["title"]

                for user_dict in user_watched:
                    if friends_title not in user_watched_titles and movie["host"] in user_data["subscriptions"]:
                        # print("FRIEND'S TITLE: ", friends_title)
                        # print()
                        # print("USER DICT TITLE: ", user_dict["title"])
                        # print()
                        # print("################")
                        # print()
                        movie_recs.append(friends_title)

    movie_recs = list(set(movie_recs))
    
    return movie_recs
    # print(user_data["watched"])

CLEAN_WAVE_4_DATA = {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}, {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'netflix'}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'amazon'}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2, 'host': 'amazon'}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0, 'host': 'hulu'}, {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5, 'host': 'disney+'}], 'friends': [{'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'amazon'}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'hulu'}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5, 'host': 'netflix'}]}, {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0, 'host': 'hulu'}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2, 'host': 'amazon'}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0, 'host': 'hulu'}, {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0, 'host': 'disney+'}]}], 'subscriptions': ['netflix', 'hulu']}

#print(get_available_recs(CLEAN_WAVE_4_DATA))
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Main function will return a list of recommended movies => 
## User has not watched!, At least 1 friend has watched!, genre of the movie is
### the same as the most watched movie!

USER_DATA = {"favorites": [{"genre": "horror", "host":"netflix", "rating": 4, "title": "parasite"}, {"genre": "fantasy", "host":"netflix", "rating": 4, "title": "cinderella"}], "friends": [{"watched": [{"genre": "horror", "host":"netflix", "rating": 4, "title": "parasite"}]}, {"watched": [{"genre": "horror", "host": "yyyyyy", "rating": 6, "title": "zzzzz"}]}], "subscriptions": ["netflix", "hulu"], "watched": [{"genre": "horror", "host":"netflix", "rating": 4, "title": "parasite"}, {"genre": "horror", "host": "vvvvvv", "rating": 7, "title": "bbbbbb"}, {"genre": "rrrrrrr", "host": "ffffff", "rating": 9, "title": "dddddd"}]}


def get_new_rec_by_genre(user_data):
    # New dict will hold the most watched genre
    user_watched_list = user_data["watched"]
    most_watched_genre = {}
    for movie in user_watched_list:
        value_genre = movie["genre"]
        if value_genre in most_watched_genre:
            most_watched_genre[value_genre] += 1
        else:
            most_watched_genre[value_genre] = 1

    # Max_watched_genre hold the value of the most watched genre by user
    max_watched_genre = ""
    max_watched = 0
    for genre, num in most_watched_genre.items():
        if num > max_watched:
            max_watched = num
            max_watched_genre = genre
    
    # Create a dict that'll hold the titles of user's watched movies
    user_watched_movies = {}
    for movie in user_watched_list:
        key = movie["title"]
        user_watched_movies[key] = 1

    # List of recommended movies by most watched genre and user hasn't watched it.
    rec_movies_by_gender = {}
    friends_list = user_data["friends"]
    for dict in friends_list:
        for value in dict.values():
            for movie in value:
                watched_by_friend = movie["title"]
                genre_movie_friend = movie["genre"]
                # La agrego si yo no la he visto y si es del genero que mas veo
                if watched_by_friend in rec_movies_by_gender:
                    continue
                if watched_by_friend not in user_watched_movies and genre_movie_friend == max_watched_genre:
                    rec_movies_by_gender[watched_by_friend] = movie

    return list(rec_movies_by_gender.values())

#print(get_new_rec_by_genre(USER_DATA))

def get_rec_from_favorites(user_data):

    # New list will hold the titles of the favorite movies.
    list_favs = []
    favorites_list = user_data["favorites"]
    for title in favorites_list:
        list_favs.append(title["title"])




    return None
print(get_rec_from_favorites(USER_DATA))