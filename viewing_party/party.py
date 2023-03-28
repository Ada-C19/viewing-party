# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_info = {}
        movie_info = movie_info.fromkeys(["title", "genre", "rating"])
        movie_info["title"] = title
        movie_info["genre"] = genre
        movie_info["rating"] = rating
        print(movie_info)
        return movie_info
    else:
        return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    #print(user_data)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    # print(user_data)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in user_data["watchlist"]:
        if movie["title"] in user_data["watched"]:
            if movie["title"] == title:
                watched.append(movie)
                watchlist.remove(movie)
                return watched

        # if title in movie:
        # if movie["title"] == title:
        #     user_data["watched"].append(movie)
    # watchlist = user_data["watchlist"]
    # watched = user_data["watched"]
    # for i in range(len(user_data)):
    #     if user_data[i]["title"] == title:
    #         user_data["watched"].append(title)
    #         del user_data[i]
    # # del (user_data[movie])
    #         return user_data
    # else:
    #     return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# def get_watched_avg_rating(user_data):
    # get values from "rating" keys
    # avg values
    # return avg
    # if no movies, return None


# def get_most_watched_genre(user_data):


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# title = True
# genre = True
# rating = True
# user_data = {"watched": []}
# movie = {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#     }

# movie2 = {
#         "title": "Title B",
#         "genre": "Horror",
#         "rating": 3.5
#     }
# watch_movie(user_data, title)

# create_movie(title, genre, rating)
# add_to_watched(user_data, movie)
# add_to_watched(user_data, movie2)
# print(user_data)


# title = "MOVIE_TITLE_1"
# genre = "GENRE_1"
# rating = "RATING_1"
# create_movie(title, genre, rating)