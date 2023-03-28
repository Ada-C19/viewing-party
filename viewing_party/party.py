# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating}
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for index in range(len(user_data["watchlist"])):
        if user_data["watchlist"][index]["title"] == title:
            add_to_watched(user_data, user_data["watchlist"][index])
            del user_data["watchlist"][index]
            break

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if user_data["watched"]:
        watched_list = user_data["watched"]
        ratings_total = 0

        for movie in watched_list:
            ratings_total += movie["rating"]
        
        avg = ratings_total / len(watched_list)

        return avg
    return 0.0


def get_most_watched_genre(user_data):
    # first validate that user_data["watched"] is truthy, else return None
    if user_data["watched"]:
        
        # store the nested list in its own variable for ease of access
        watched_list = user_data["watched"]

        # declare total rating variables for each genre
        fantasy_ratings_total = 0
        action_ratings_total = 0
        intrigue_ratings_total = 0

        # declare counter variables for the amount of movies in each genre
        num_fantasy_movies = 0
        num_action_movies = 0
        num_intrigue_movies = 0

        # iterate through the watched list to add ratings and genres to their respective variables
        for movie in watched_list:
            if movie["genre"] == "Fantasy":
                fantasy_ratings_total += movie["rating"]
                num_fantasy_movies += 1
            elif movie["genre"] == "Action":
                action_ratings_total += movie["rating"]
                num_action_movies += 1
            elif movie["genre"] == "Intrigue":
                intrigue_ratings_total += movie["rating"]
                num_intrigue_movies += 1
            
        # calculate the averages for each genre type
        fantasy_avg = fantasy_ratings_total / num_fantasy_movies
        action_avg = action_ratings_total / num_action_movies
        intrigue_avg = intrigue_ratings_total / num_intrigue_movies

        # retrieve the max rating across all genre averages
        highest_avg_rating = max(fantasy_avg, action_avg, intrigue_avg)

        # find the corresponding genre to the max rating
        if fantasy_avg == highest_avg_rating:
            return "Fantasy"
        elif action_avg == highest_avg_rating:
            return "Action"
        elif intrigue_avg == highest_avg_rating:
            return "Intrigue"
    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

