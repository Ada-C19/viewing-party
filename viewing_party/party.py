# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if not (title and genre and rating):
        return None
    else:
        movie_dict["title"]= title
        movie_dict["genre"]= genre
        movie_dict["rating"]= rating
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data  

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0.0
    if not user_data["watched"]:
        return sum
    for movie in user_data["watched"]:
        sum += movie["rating"]
    average = sum / len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    genre_list = []
    if not user_data["watched"]:
        return None
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    # Why does this method need set in order to count the frequency? What does key=genre_list do?
    return max(set(genre_list),key=genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for friend_list in friend["watched"]:
            for friend_key, friend_value in friend_list.items():
                if friend_key == "title":
                    friend_watched_list.append(friend_value)

    user_set = set(user_watched_list)
    friend_set = set(friend_watched_list)
    unique_set = user_set - friend_set

    unique_list = []
    for title in unique_set:
        for movie in user_data["watched"]:
            if title == movie["title"]:
                unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie["title"])

    for friend in user_data["friends"]:
        for friend_list in friend["watched"]:
            for friend_key, friend_value in friend_list.items():
                if friend_key == "title":
                    friend_watched_list.append(friend_value)

    user_set = set(user_watched_list)
    friend_set = set(friend_watched_list)
    unique_set = friend_set - user_set

    unique_list = []
    for title in unique_set:
        for friend in user_data["friends"]:
            for friend_list in friend["watched"]:
                if title == friend_list["title"] and not (friend_list in unique_list):
                    unique_list.append(friend_list)
    print(unique_list)
    return list(set(unique_list))   

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

