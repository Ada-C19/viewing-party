
def create_movie(title, genre, rating):
    if title and genre and rating: 
        return {"title": title, "genre": genre, "rating": rating}
    else: 
        return None

def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i]["title"])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data

    
def get_watched_avg_rating(user_data):
    if len(user_data['watched']) == 0:
        return 0
    avg_total = 0
    counter = 0
    for dict in user_data["watched"]:
        avg_total += dict['rating']
        counter += 1
    avg_rating = avg_total / counter
    return avg_rating

def get_most_watched_genre(user_data):
    counter = {}
    most_genre = ""
    score = 0 
    if len(user_data['watched']) == 0:
        return None
    for dict in user_data["watched"]:
        if dict['genre'] not in counter:
            counter[dict['genre']] = 1
        else:
            counter[dict['genre']] += 1
    for key, values in counter.items():
        if values >= score:
            score = values
            most_genre = key
    return most_genre


def get_unique_watched(user_data):
    friends_list = []
    user_list = []
    diff_list = []
    for i in range(len(user_data["watched"])):
        user_list.append(user_data["watched"][i])
    for j in range(len(user_data["friends"])):
        for dict in (user_data["friends"][j]["watched"]):
            friends_list.append(dict)
    for dict in user_list: 
        if dict not in friends_list:
            diff_list.append(dict)
    return diff_list

def get_friends_unique_watched(user_data):
    friends_list = []
    user_list = []
    diff_list = []
    for i in range(len(user_data["watched"])): 
        user_list.append(user_data["watched"][i])
    for j in range(len(user_data["friends"])):
        for dict in (user_data["friends"][j]["watched"]):
            friends_list.append(dict)
    for dict in friends_list: 
        if dict not in user_list and dict not in diff_list:
            diff_list.append(dict)
    return diff_list
        



def get_available_recs(user_data):
    reccomendation_list = []
    for friend_watched in (user_data['friends']):
        for movie in friend_watched['watched']: 
            if movie not in user_data["watched"] and movie['host'] in user_data["subscriptions"]:                
                if movie not in reccomendation_list:
                    reccomendation_list.append(movie)
    return reccomendation_list 

def get_friend_watchlist(user_data):
    friend_watched_list = []
    for watched_list in user_data["friends"]:
        for movie in watched_list["watched"]:
            friend_watched_list.append(movie)
    return friend_watched_list

def get_new_rec_by_genre(user_data):
    friends_watched_list = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)
    rec_list = []
    for movie in friends_watched_list:
        if movie["genre"] == favorite_genre and movie not in user_data["watched"]:
            rec_list.append(movie) 
    return rec_list


# realized there's two of the same helper function... commenting out for redundancy
# def get_friends_watched_list(user_data):
#     movies_friends_watched = []
#     friends = user_data["friends"]
#     for dict in friends:
#         watched = dict["watched"]
#         for movie in watched:
#             if movie not in movies_friends_watched:
#                 movies_friends_watched.append(movie)
#     return movies_friends_watched




def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    recommended_by_user = []
    friends_watched = get_friend_watchlist(user_data)
    for movie in favorites:
        if movie not in friends_watched and movie not in recommended_by_user:
            recommended_by_user.append(movie)
    return recommended_by_user


