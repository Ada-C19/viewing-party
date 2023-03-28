# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {}
    if not (title and genre and rating):
        return None 
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating 
    return new_movie
    

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data['watchlist']:
        if movie['title'] == title:  
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0.0
    average = 0.0 
    for movies in user_data["watched"]:
        if not movies["rating"]:
           return average
        sum += movies["rating"]
    if len(user_data["watched"]) > 0:
        average = sum / len(user_data["watched"])      
        
    return average
            
def get_most_watched_genre(user_data):
    frequency_genre = {}

    if not user_data['watched']:
        return None 
    for movie in user_data['watched']:
        genre = movie['genre']
        if genre in frequency_genre:
            frequency_genre[genre] += 1
        else:
            frequency_genre[genre] = 1
    
    max_frequency = max(frequency_genre.values())
    most_common_genre = None   
    for genre, frequency in frequency_genre.items():
        if frequency == max_frequency:
            most_common_genre = genre
            break

    return most_common_genre  


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_user_titles(user_data):
    user_titles  = []
    for movie in user_data["watched"]:
        user_titles.append(movie["title"])
    return user_titles

def get_friend_titles(user_data):
    friend_titles = []
    for friend_movie in user_data["friends"]:
        for watched_dict in friend_movie['watched']:
            friend_titles.append(watched_dict["title"])
    return friend_titles

def get_unique_watched(user_data):
    user_titles = get_user_titles(user_data)
    friend_titles = get_friend_titles(user_data)
    
    user_unique_list = []
  
    set_difference = set(user_titles) - set(friend_titles)
   
    for movie in user_data["watched"]:
        for title in set_difference:
            if movie["title"] == title:
                user_unique_list.append(movie)
    return user_unique_list

def get_friends_unique_watched(user_data):
    user_titles = get_user_titles(user_data)
    friend_titles = get_friend_titles(user_data)

    friend_unique_list = []
    set_difference = set(friend_titles) - set(user_titles)
    

    for friend_movie in user_data["friends"]:
        for friends_watched_dict in friend_movie['watched']:
            for title in set_difference:
                if friends_watched_dict["title"] == title:
                    friend_unique_list.append(friends_watched_dict)
    no_duplicates_friends_list = []
    for item in friend_unique_list:
        if item not in no_duplicates_friends_list:
            no_duplicates_friends_list.append(item)
   
    
    return no_duplicates_friends_list



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

