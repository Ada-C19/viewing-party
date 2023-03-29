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
    unique_user_watched_list = []
    for movie in user_data["watched"]:
        for friend in user_data["friends"]:
            for friend_list in friend:
            #    if not movie["title"] in 
                for friend_dict in friend_list:
                    for friend_watched in friend_dict:
                        for friend_watched_movie in friend_watched:
                            unique_user_watched_list.append(friend_watched_movie["title"])
                            # if not movie["watched"] in friend_watched_movie["title"]
                return unique_user_watched_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

