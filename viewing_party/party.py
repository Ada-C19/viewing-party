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
    #append movie dictionary to the list "watched_list" in user_data dictionary
    watched_list.append(movie)
    user_data["watched"] = watched_list
    return user_data

def add_to_watchlist(user_data, movie):
    #append movie dictionary to the key "watchlist" in user_data dictionary
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
    #for loop to loop through "watched" key in user data and add up "rating" of any movie on the list to the variable sum
    for movie in user_data["watched"]:
        sum += movie["rating"]
        count += 1
    
    #Handling division by zero exception. In this case when the dictionary is empty it must return 0.0
    try:
        avg_rating = sum / count 
    
    except ZeroDivisionError:
        return 0.0
    
    return avg_rating

def get_most_watched_genre(user_data):
    #create a list to store any genre of any movie in the user_data dictionary
    genre_list = []
    #list to store every movie in "watched" key in user_data dictionary
    watched_list = user_data["watched"]

    genre_count = 0
    max_genre = None
    #for loop to loop through watched_list and get the genre of every movie in the list to store in genre_list
    for movie in watched_list:
        genre = movie["genre"] 
        genre_list.append(genre)
    
    #for loop to loop through genre_list and count how many times each genre occurs in the list
    #get the most watched genre by comparing how many times the same genre appears using .count()
    #store the most whatched genre in variable max_genre
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
    user_watched = []
    friends_watched = []
    unique_watched = []
    #for loop to loop through the movies the user watched and to store each movie's title in a list
    for movie in user_data["watched"]:
        title = movie["title"]
        user_watched.append(title)
    #for loop to loop through the movies friends watched and to store each movie's title in friends_watched list
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            friends_watched.append(title)
    #We use this for loop to compare if some of all the titles stored in user_watched are in friends_watched
    #the ones that only exist in user_watched are then stored in unique_watched that is a list of dictionaries
    for movie in user_data["watched"]:
        if movie["title"] in user_watched:
            if movie["title"] not in friends_watched:
                unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    user_watched = []
    friends_watched = []
    friends_unique_watched = []
    #for loop to loop through the movies the user watched and to store each movie's title in a list
    for movie in user_data["watched"]:
        title = movie["title"]
        user_watched.append(title)
   #for loop to loop through the movies friends watched and to store each movie's title in friends_watched list
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            friends_watched.append(title)
    #We use this for loop to compare if some of all the titles stored in friends_watched are in user_watched
    #the ones that only exist in user_watched are then stored in friends_unique_watched that is a list of dictionaries
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in friends_watched:
                if movie["title"] not in user_watched:
                    friends_unique_watched.append(movie)
    #this for loop evaluates that there's no duplicate movies before returning the list of dictionaries
    for movie in friends_unique_watched:
        current_movie = friends_unique_watched.count(movie)
        if current_movie > 1:
            friends_unique_watched.remove(movie)

    return friends_unique_watched




# Create a function named `get_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies

# 2. Create a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


#def get_available_recs(user_data):
#    subscriptions = user_data["subscriptions"] 




# Create a function named `get_available_recs`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

#def get_new_rec_by_genre(user_data):

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