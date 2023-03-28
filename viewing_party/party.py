# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title == None or genre == None or rating == None:
        return None

    return {"title" : title, "genre" : genre, "rating" : rating}

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
            return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0 
    if len(user_data["watched"]) == 0:
        return 0.0
    for movie in user_data["watched"]:
        sum += movie["rating"] 
    average = sum / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    # keep count of genres in watched list
        # maybe a dictionary
    if len(user_data["watched"]) == 0:
        return None
    
    genre_dictionary = {}
    max_count = 0
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dictionary:
            genre_dictionary[movie["genre"]] = 1
        else:
            genre_dictionary[movie["genre"]] += 1

    # gets max value from dictioanry and returns the key
    max_genre = max(genre_dictionary, key = genre_dictionary.get)
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched_set = set()
    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])
    # print(user_watched_set)

    user_friends_watched_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            user_friends_watched_set.add(movie["title"])
       # user_friends_watched_set.add(movie["title"])
    print(user_friends_watched_set)
    unique_set = user_watched_set.difference(user_friends_watched_set)
    print(unique_set)

    unique_list = []

    for movie in user_data["watched"]:
        user_watched_set.add(movie["title"])

        if movie["title"] in unique_set:
            unique_list.append(movie)
    return unique_list  


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

