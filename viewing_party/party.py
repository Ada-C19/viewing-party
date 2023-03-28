from collections import Counter
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None  or rating == None:
        movie_dict = None
    else:
        movie_dict = {"title":title,"genre":genre,"rating":rating}
    return movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

user_data = {"watchlist":[{"title": "lord of rings", "genre" : "horrpr","rating": 5}]}
movie = {"title" : "game of thrones","genre":"fantasy","rating":5}
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

user_input = {"watchlist":[{"title": "harry potter", "genre" : "horrpr","rating": 5},{"title": "lord of rings", "genre" : "horrpr","rating": 5}],"watched":[]}

def watch_movie(user_data, title):
    for index in range(len(user_data["watchlist"])):
        if title in user_data["watchlist"][index].values():
            res = user_data["watched"].insert(0, user_data["watchlist"].pop(index))
            # print(user_data["watchlist"])
            # print(user_data["watched"])
        else:
            continue
    return user_data  
# title = "lord of rings"
# watch_movie(user_input,title)



# -----------------------------------------
# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    # could make simpler using counter import
    average_rate = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie_dict in user_data["watched"]:
        average_rate += movie_dict["rating"]
    count = len(user_data["watched"])

    rate = average_rate / count
    print(rate)
    return rate
    

def get_most_watched_genre(user_data):
    
    if user_data["watched"] == []:
        return None
    else: 
        genres_dict = {}

        for index in range(len(user_data["watched"])):
            genre = user_data["watched"][index]["genre"]
            if genre in genres_dict:
                genres_dict[genre] += 1
            else:
                genres_dict[genre] = 1

        most_popular = max(genres_dict, key = genres_dict.get)

        return most_popular
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

user_data = {"watched":[{"title":"meep","genre":"horror","rating":5},{"title":"Ghost","genre":"horror","rating":5},{"title":"Hehe","genre":"horror","rating":5}], "friends": [{"watched":[{"title":"Bionicles"},{"title":"Ghost"}, {"title":"Paranormal"} ]}]}
# make list of friend movies 
# print(user_data["friends"][0]["watched"][0]["title"])
# print(user_data)
# user_data = {"watched":[{"title":"Ghost","genre":"horror","rating":5},{"title":"Ghost","genre":"horror","rating":5},{"title":"The well","genre":"horror","rating":3},{"title":"Wednesday","genre":"comedy","rating":5},{"title":"Wednesday","genre":"comedy","rating":5},{"title":"The car","genre":"horror","rating":3}]}
def get_unique_watched(user_data):
    unique_movies = []
    friends_watched_set = set()
    user_watched_set = set()
    unique_movies = []
    
    for index in range(len(user_data["friends"][0]["watched"])):
        friends_watched_set.add(user_data["friends"][0]["watched"][index]["title"])

    for index in range(len(user_data["watched"])):
        user_watched_set.add(user_data["watched"][index]["title"])

    differences = user_watched_set.difference(friends_watched_set)
    
    for item in differences:
        dict = {}
        dict["title"]=item
        unique_movies.append(dict)

    output_dict = {}
for val,item in enumerate(input_set):
    output_dict[item] = val
    print(unique_movies)
    # # make list of friends movies
    # for index in range(len(user_data["watched"])):
    #     title = user_data["watched"][index]["title"]
    #     print(title)
    #     for position in range(len(user_data["friends"][0]["watched"])):
    #         if title in user_data["friends"][0]["watched"][position]:
    #             continue
    #         else:
    #             unique_movies.append(user_data["watched"][index])
    # print(unique_movies)
    
    
    
    
    
get_unique_watched(user_data)
# set.union(*my_dict.values())
#1. convert friend title into set

#2. convert user watched titles into set 
#3. user.different to compare the two sets
# 4. return differences in list of dictionaries 


# 1. Create a function named `get_unique_watched`. This function should...

#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

