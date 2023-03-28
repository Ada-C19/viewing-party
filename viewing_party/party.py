# ------------- WAVE 1 --------------------

# Let's start
# Hola, Laura!

def create_movie(title, genre, rating):
    title_check = isinstance(title, str)
    genre_check = isinstance(genre, str)
    rating_check = isinstance(rating, float)
    if not title_check or not genre_check or not rating_check:
        return None
    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie
    
# not modify user_data
def add_to_watched(user_data, movie):
    user_data_watched_list = user_data["watched"]
    user_data_watched_list.append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data_watchlist = user_data["watchlist"]
    user_data_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):

    # if title not in user_data["watchlist"]:
    #     return user_data
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
        else:
            return user_data
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    lengh_list = len(user_data["watched"])
    if lengh_list < 1:
        return 0.0
    rating_added = 0
    for element in user_data["watched"]:
        rating_added += element["rating"]
    average_rating = rating_added/lengh_list
    return float(average_rating)


def get_most_watched_genre(user_data):
    count_watched_genres = {}
    if user_data["watched"] == []:
        return None
    for element in user_data["watched"]:
        if element["genre"] not in count_watched_genres:
            count_watched_genres[element["genre"]] = 1
        count_watched_genres[element["genre"]] += 1
    sorted_dict = sorted(count_watched_genres.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict[0][0]

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# def get_unique_watched(user_data):


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

