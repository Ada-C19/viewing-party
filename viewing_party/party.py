# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    movie = {}
    if not title or not genre or not rating:
        return None
    else:
        movie.update({"title" : title, "genre" : genre, "rating" : rating})
        return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# # Diana's Implementation : Doesn't pass #9
# def watch_movie(user_data, title):
#     print(user_data)
#     watchlist_list_of_dict = user_data.get("watchlist")
#     print(watchlist_list_of_dict)

#     for watchlistDict in watchlist_list_of_dict:
#         if watchlistDict.get("title") == title:
#             watchlist_list_of_dict.remove(watchlistDict)
#             user_data["watched"].append(watchlistDict)
#             print(user_data)
#     return user_data

# Celina's Implementation: Doesn't pass #9 or #10
def remove_from_watchlist(user_data, movie):
    if movie in user_data["watchlist"]:
        user_data["watchlist"].remove(movie)
    return user_data

def remove_from_watched(user_data, movie):
    if movie in user_data["watched"]:
        user_data["watched"].remove(movie)
    return user_data

def watch_movie(user_data, title):
    # example used_data structure
    # user_data = {
    #     "watchlist" : [{"title" : "Ferngully", "genre": "kids", "rating": 10}],
    #     "watched" : [{"title" : "Avatar", "genre": "white savior", "rating": 1},
    #                  {"title" : "The Blind Side", "genre": "white savior", "rating": 8}]
    # }
    # so as to not modify the OG user_data as per the instructions
    modified_user_data = user_data
    for movie in modified_user_data["watchlist"]:
        if title == movie["title"]:
            add_to_watched(modified_user_data, movie)
            remove_from_watchlist(modified_user_data, movie)
            return modified_user_data
    return user_data

# # A mix of the two?
# def watch_movie(user_data, title):
#     modified_user_data = user_data
#     for movie in modified_user_data["watchlist"]:
#         if title == movie["title"]:
#             modified_user_data["watchlist"].remove(movie)
#             modified_user_data["watched"].append(movie)
#             return modified_user_data
#     return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

