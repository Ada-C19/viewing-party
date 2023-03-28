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
    if title in user_data['watchlist']:
        user_data['watched'].append(title)
        user_data['watchlist'].remove(title)
        # return user_data
    return user_data
# we need to work on it tomorrow

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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

