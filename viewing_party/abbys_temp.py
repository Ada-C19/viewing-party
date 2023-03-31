# def get_unique_watched(user_data):
#     unique_watched = []
#     # so you need to access the nested data structure.
#     # you are comparing elements. you are comparing the elements
#     # that can be found at user_data["friends"][n]["watched"][n]["title"] on the one hand,
#     # with the data at user_data["watched"][n]["title"]

# so. maybe write a loop?
# user_watched = user_data["watched"].values()
# for movie in user_data["watched"].values():
#   
    
#     return unique_watched

def get_unique_watched(user_data):
#    unique_watched = []
    user_watched = user_data["watched"]
    friends = user_data["friends"]
    friends_watched = []
    #print(friends_watched)
    
    # Create list with everyone else's movies
    for friend in range(0, len(friends)):
        friend_watched_list = friends[friend]["watched"]
        for movie in range(0, len(friend_watched_list)):
            friends_watched.append(friend_watched_list[movie]["title"])
            
        print(f"friends_watched: {friends_watched}")
    # for friend in friends:
    #     print user_data["friends"]["watched"].values
    
    # # for my_movie in user_watched:
    # #     print(f"BEGINNING OF {my_movie} LOOP")
    # #     for friend in range(0, len(friends)):
    # #         print(f"BEGINNING OF {friend} LOOP")
    # #         print(user_data["watched"][friend]["title"])

            
    #print(user_watched)

me_and_my_friends = {
    "watched": [{"title": "Spirited Away"}, {"title": "Sharknado"}, {"title": "Dinosaurs"}, {"title": "Jurassic Park"}, {"title": "Jaws"}],
    "friends": [{"watched": [{"title": "Jurassic Park"}, {"title": "Dinosaurs"}]},
                {"watched": [{"title": "Spirited Away"}, {"title": "My Neighbor Totoro"}, {"title": "Princess Mononoke"}]},
                {"watched": [{"title": "Eraserhead"}]}]
}

get_unique_watched(me_and_my_friends)