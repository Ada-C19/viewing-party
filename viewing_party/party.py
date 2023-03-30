# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {'title': title, 'genre': genre, 'rating': rating}
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data['watchlist'])):
        if user_data['watchlist'][i]['title'] == title:
            user_data['watched'].append(user_data['watchlist'][i])
            user_data['watchlist'].pop(i)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    ratings_total = 0
    watched_list = user_data["watched"]
    if len(watched_list) == 0:
            return 0
    

    for num in watched_list:
        num = num.get('rating')
        ratings_total += num
    average = ratings_total / len(watched_list)
    return average
    


def get_most_watched_genre(user_data):
    genres_list = []
    popular_genre = None
    watched_list = user_data["watched"]
    if len(watched_list) == 0:
            return None
    
    
    for genre in watched_list:
        genre = genre.get('genre')
        genres_list.append(genre)
    popular_genre = max(genres_list, key = genres_list.count)
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies_user_watched = []
    friends_watched = []

    for friend in user_data["friends"]:
        for movie_info in friend["watched"]:
            friends_watched.append(movie_info)
    
        
    for watched_movie in user_data["watched"]:
        if watched_movie not in friends_watched:
            unique_movies_user_watched.append(watched_movie)
    return unique_movies_user_watched


def get_friends_unique_watched(user_data):
    unique_friend_watched = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in unique_friend_watched:
                unique_friend_watched.append(movie)
    return unique_friend_watched

    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):    
    recommendations = []
    friend_list = user_data["friends"]
    
    
    for friend in friend_list: 
        user_watched_list = user_data["watched"]
        for movie in friend["watched"]:
            subscription_list = user_data["subscriptions"]
            if movie["host"] in subscription_list and movie not in user_watched_list and movie not in recommendations:
                    recommendations.append(movie)
    return recommendations




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass
