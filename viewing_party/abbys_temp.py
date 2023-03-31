def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends = user_data["friends"]
    friends_watched = []
    
    # Create list with everyone else's movies
    for friend in range(0, len(friends)):
        friend_watched_movies = friends[friend]["watched"]
        for movie in friend_watched_movies:
            friends_watched.append(movie)

    # Loop through friends' movies, compare with user's movies
    for film in friends_watched:
        if film in user_watched:
            user_watched.remove(film)
        # for entertainment in user_watched:
        #     if entertainment == film:
        #         user_watched.remove(entertainment)
    
    print(f"user_watched: {user_watched}")
    return user_watched

def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends = user_data["friends"]
    friends_watched = []
    friends_unique = []
    
    for friend in range(0, len(friends)):
        friend_watched_movies = friends[friend]["watched"]      
        for movie in friend_watched_movies:
            if movie in friends_watched:
                continue
            friends_watched.append(movie)
    
    for film in friends_watched:
        if film not in user_watched:
            friends_unique.append(film)
    
    print(f"friends_unique: {friends_unique}")
    return friends_unique

me_and_my_friends = {
    "watched": [{"title": "Spirited Away"}, {"title": "Sharknado"}, {"title": "Dinosaurs"}, {"title": "Jurassic Park"}, {"title": "Jaws"}],
    "friends": [{"watched": [{"title": "Jurassic Park"}, {"title": "Dinosaurs"}]},
                {"watched": [{"title": "Spirited Away"}, {"title": "My Neighbor Totoro"}, {"title": "Princess Mononoke"}, {"title": "Eraserhead"}]},
                {"watched": [{"title": "Eraserhead"}]}]
}

# get_unique_watched(me_and_my_friends)
# get_friends_unique_watched(me_and_my_friends)

friends_unique_movies = get_friends_unique_watched(me_and_my_friends)
print(f"{friends_unique_movies=}")
friends_unique_deduplicated = list(set(friends_unique_movies))

print(f"{friends_unique_movies=}")
print(f"{friends_unique_deduplicated=}")