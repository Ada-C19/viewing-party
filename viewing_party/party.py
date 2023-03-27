# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if title != None and genre != None and rating != None:
        movies= {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movies
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


    # user_data = {
    #     "watched": [
    #         movie
    #         ]
    #     }

    # user_data["watched"] += movie
    # print(user_data)

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    #we want to move the movies (title, genre, rating) into the user_data["watch"]

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_avg_rating = 0.0

    if len(user_data["watched"]) == 0:
        return sum_avg_rating
    else:
        for movie in user_data["watched"]:
            sum_avg_rating += movie["rating"]
            avg_rating = sum_avg_rating / len(user_data["watched"])
        return avg_rating
    
def get_most_watched_genre(user_data):
    freq = {}
    highest_count = 0

    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] in freq:
            freq[movie["genre"]] += 1
        else: 
            freq[movie["genre"]]= 1

    for genre, count in freq.items():
        if count > highest_count:
            highest_count = count
            highest_genre = genre
    return highest_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

