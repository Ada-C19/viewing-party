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


print(watch_movie({
            "watchlist": [{
                "title": "Scooby Doo",
                "genre": "GENRE_1",
                "rating": 1
            }],
            "watched": []
        }, "Scooby Doo"))


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

print(get_watched_avg_rating({'watchlist': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}], 'watched': [{'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]}))
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

