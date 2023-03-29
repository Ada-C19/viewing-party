# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dictionary = {}
    if title and genre and rating:
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
    else:
        return None
    
    return movie_dictionary

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    copy_user_data = user_data
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            copy_user_data["watched"].append(movie)
            copy_user_data["watchlist"].remove(movie)
        user_data = copy_user_data

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    sum = 0
    length = len(user_data["watched"])

    if user_data["watched"]:
        for movie in user_data["watched"]:
            sum += movie["rating"]
        avg_rating = sum / length
    
    return avg_rating
def get_most_watched_genre(user_data):
    dict_count_genre = {}
    if user_data["watched"]:
       for movie in user_data["watched"]:
           if not movie["genre"] in dict_count_genre:
              dict_count_genre[movie["genre"]] = 1
           else:
              dict_count_genre[movie["genre"]] += 1
       maximum = max(dict_count_genre, key= dict_count_genre.get)
       return maximum
    return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    unique_watched = []
    for movie in user_data["watched"]:
        title = movie["title"]
        for friend in user_data["friends"]:
            if title in list(movie["title"] for movie in friend["watched"]):
                break
        else:
            unique_watched.append(movie)
            
    
    return unique_watched

def get_friends_unique_watched(user_data):
   friend_unique = []
   user_watched = list(movie["title"] for movie in user_data["watched"])
   for friend in user_data["friends"]:
     for movie in friend["watched"]:
         title = movie["title"]
         if  movie in friend_unique:
             continue
         if not title in user_watched:
             friend_unique.append(movie)
   return friend_unique

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

