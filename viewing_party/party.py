# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #create and empty dictionary to store title, genre and rating of the movie
    movie_dictionary = {}
    #this if statement evaluate that title, genre and rating
    #have some value different from None
    #besides checking if this parameters are truthy we also evaluate that they're the 
    #appropiate type of data
    if type(title) == str and type(genre) == str and type(rating) == float:
        #if the parameters are truthy then we add title,genre and rating
        #to movie_dictionary
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
        return movie_dictionary
    return None

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    user_data["watched"] = watched_list
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    #nested for loop to loop through the outer dictionary first "user_data"
    #and look for the key "watchlist"
    for watch in user_data.keys():
        if watch == "watchlist":
            #inner for loop check if the title of the movie is in the list of dictionaries
            #stored in "watchlist key"
            for movie in user_data[watch]:
                if movie["title"] == title:
                    temp_movie = user_data[watch].pop()
                    add_to_watched(user_data, temp_movie)
                    
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    sum = 0.0
    count = 0.0

    for movie in user_data["watched"]:
        sum += movie["rating"]
        count += 1
    
    try:
        avg_rating = sum / count 
    
    except ZeroDivisionError:
        return 0.0
    
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list = []
    watched_list = user_data["watched"]
    genre_count = 0
    max_genre = None

    if not watched_list:
        return None
    
    for movie in watched_list:
        genre = movie["genre"] 
        genre_list.append(genre)

    for genre in genre_list:
        current_genre_count = genre_list.count(genre)
        if current_genre_count > genre_count:
            genre_count = current_genre_count
            max_genre = genre
            
    return max_genre




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    user_watched_titles = []
    friends_watched_titles = []
    unique_watched_movies = []

    for movie in user_data["watched"]:
        title = movie["title"]
        user_watched_titles.append(title)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            friends_watched_titles.append(title)

    for movie in user_data["watched"]:
        if movie["title"] in user_watched_titles:
            if movie["title"] not in friends_watched_titles:
                unique_watched_movies.append(movie)

    return unique_watched_movies



def get_friends_unique_watched(user_data): 
    user_watched_titles = []
    friends_watched_titles = []
    friends_unique_watched_movies = []


    for movie in user_data["watched"]:
            title = movie["title"]
            user_watched_titles.append(title)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            friends_watched_titles.append(title)


    for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie["title"] not in user_watched_titles:
                    if movie not in friends_unique_watched_movies:
                        friends_unique_watched_movies.append(movie)

    return friends_unique_watched_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movie_list = []
    subscriptions = user_data["subscriptions"]
    user_watched = get_unique_watched(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    
    for movie in friends_watched:
        if movie not in user_watched and movie["host"] in subscriptions:
            recommended_movie_list.append(movie)
            
            
    return recommended_movie_list



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    pass

# Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

# 2. Create a function named  `get_rec_from_favorites`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies