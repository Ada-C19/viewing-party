# ------------- WAVE 1 --------------------
# 1st function in wave_01
def create_movie(title, genre, rating):
    movie = {}

    # checks to see if all values are truthy
    if title and genre and rating: 
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

    return None
# 2nd function in wave_01
def add_to_watched(user_data, movie):      
    user_data["watched"].append(movie)
    return user_data

# 3rd function in wave_01
def add_to_watchlist(user_data, movie): 

    user_data["watchlist"].append(movie)
    return user_data

#4th funcyion in wave_01
def watch_movie(user_data, title):
    index = 0
    for index in range(len(user_data["watchlist"])):
        if title in (user_data["watchlist"][index]["title"]):
            move_movie = user_data["watchlist"].pop(index)
            #to move to end of list
            user_data["watched"].append(move_movie)
            #to move to begiiniing of list
            # user_data["watched"].insert(0, move_movie)
            return user_data
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# 1st function in wave_02 
def get_watched_avg_rating(user_data): 
    rating_sum = 0.0
    
    if not user_data["watched"]:
        return rating_sum
    
    for movie in user_data["watched"]:
        rating_sum += movie["rating"]
    
    length = len(user_data["watched"])
    return rating_sum / length

# 2nd funct=ion in wave_02
def get_most_watched_genre(user_data): 
    
    if not user_data["watched"]:
        return None
    
    genres = {}
    for movie in user_data["watched"]: 
        if movie["genre"] not in genres: 
            genres[movie["genre"]] = 0
        else: 
            genres[movie["genre"]] += 1 
    
    return max(genres, key = genres.get)



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
#1st function in wave_03
def get_unique_watched(user_data):
    user_unique_movies = []
    my_friends_movies = set() 

    for movie in user_data["friends"]:
        for num in range(len(movie["watched"])): 
            my_friends_movies.add(movie["watched"][num]["title"])
    
    for pelicula in user_data["watched"]:
        
        if pelicula["title"] not in my_friends_movies: 
            user_unique_movies.append(pelicula)
        
    return user_unique_movies

# 2nd function in wave_03 
def get_friends_unique_watched(user_data):
    friends_unique_movies = {}
    user_movies = {}

    for movie in user_data["watched"]:
        user_movies[movie["title"]] = movie

    for pelicula in user_data["friends"]:
        for num in range(len(pelicula["watched"])):
            title = pelicula["watched"][num]["title"]
            if title not in user_movies and title not in friends_unique_movies: 
                friends_unique_movies[title] = pelicula["watched"][num]
    
    result = list(friends_unique_movies.values())

    return result

    #         title = pelicula["watched"][num]["title"]
    #         if title not in user_movies and title not in friends_unique_movies:
    #             friends_unique_movies.append(pelicula["watched"][num])
    # return friends_unique_movies
            
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# 1st function for wave  04 
def get_available_recs(user_data): 
    movie_recs = []
    unique_movies = get_friends_unique_watched(user_data)

    for movie in unique_movies: 
        if movie["host"] in user_data["subscriptions"]: 
            movie_recs.append(movie)
    
    return movie_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


