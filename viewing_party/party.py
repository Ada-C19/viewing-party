# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    Function creates a movie dictionairy
    '''
    if title is None or genre is None or rating is None:
        return None
    return {"title": title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    '''
    Function appends movie dictionairy to user_data "watched" list
    '''
    user_data["watched"].append(create_movie(movie["title"], movie["genre"], movie["rating"]))
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Function appends movie dictionairy to user_data "watchlist" list
    '''
    user_data["watchlist"].append(create_movie(movie["title"], movie["genre"], movie["rating"]))
    return user_data

def watch_movie(user_data, title):
    '''
    Function moves a movie from user_data "watchlist" list to "watched" list
    '''
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = 0
    try:
        for i in range(len(user_data["watched"])):
            rating += user_data["watched"][i]["rating"]
        return rating/len(user_data["watched"])   
    except ZeroDivisionError:
        return 0.0
    
def get_most_watched_genre(user_data):
    genre_list = []
    try:
        for i in range(len(user_data["watched"])):
                genre_list.append(user_data["watched"][i]["genre"])
        
        sorted_genre_list = sorted(genre_list,key=genre_list.count,reverse=True)
        return sorted_genre_list[0]
    except IndexError:
        return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    same_movies = []
    unique_movies = []

    for i in range(len(user_data["watched"])):
        for j in range(len(user_data["friends"])):
            for k in range(len(user_data["friends"][j]["watched"])):
                if user_data["watched"][i]["title"] == user_data["friends"][j]["watched"][k]["title"]:
                    same_movies.append(user_data["watched"][i])

    
    for i in range(len(user_data["watched"])):
        if i not in same_movies:
            unique_movies.append(user_data["watched"][i])

    return unique_movies


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

