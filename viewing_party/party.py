# ------------- WAVE 1 --------------------

def create_movie(title, genre , rating):
    if title and genre and rating:
        return {"title": title, "genre": genre, "rating": rating}
    else:
        return None
    
def add_to_watched(user_data, movie):
    add_watched = user_data["watched"]
    add_watched.append(movie)
    return user_data
 

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data
    # user_data["watchlist"].append(movie)
    # return user_data


def watch_movie(user_data, title):
    watched_movie = user_data['watched']
    movie_to_watchlist = user_data['watchlist']

    for item in movie_to_watchlist:
        if title == item['title']:
            watched_movie.append(item)
            movie_to_watchlist.remove(item)
    return user_data
    
    #print(movie_watched)
    # user_data = {
    #         "watchlist": [{
    #             "title": "It Came from the Stack Trace",
    #             "genre": "Horor",
    #             "rating": 5
    #         }],
    #         "watched": []
    #     }
    # title = "It Came from the Stack Trace"


    # # return user_data["watchlist"][0]["title"]
    # if title in user_data["watchlist"][0]["title"]:
    #     user_data["watchlist"].remove()
    #     user_data["watched"] = user_data["watchlist"][0]
    
    #     print(user_data)
    #     # if title == user_data["watchlist"][0]["title"]:

            

            
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating():
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
    ACTION_1 = {
        "title": "The JavaScript and the React",
        "genre": "Action",
        "rating": 2.2
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
    user_data ={
        "watched": [
        FANTASY_1,
        FANTASY_2,
        FANTASY_3,
        ACTION_1,
        INTRIGUE_1,
        INTRIGUE_2
        ]}
    total_ratings = 0
    number_movies = len(user_data["watched"])
    for i in range(len(user_data["watched"])):
        total_ratings +=user_data["watched"][i]["rating"]
        average_ratings = total_ratings / number_movies
    return average_ratings
print(get_watched_avg_rating())


def get_most_watched_genre(user_data):















   
   
    #calculate the average rating of all movies in the watched list
    #return avg rating

#    "watched": [
#         FANTASY_1, 
#         FANTASY_2, 
#         FANTASY_3, 
#         ACTION_1, 
#         INTRIGUE_1, 
#         INTRIGUE_2
#         ],    
# }

#     1. Create a function named `get_watched_avg_rating`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries
#     - This represents that the user has a list of watched movies
# - Calculate the average rating of all movies in the watched list
#   - The average rating of an empty watched list is `0.0`
# - return the average rating

# 2. Create a function named `get_most_watched_genre`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. Each movie dictionary has a key `"genre"`.
#     - This represents that the user has a list of watched movies. Each watched movie has a genre.
#     - The values of `"genre"` is a string.
# - Determine which genre is most frequently occurring in the watched list
# - return the genre that is the most frequently watched
# - If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

#print(watch_movie())