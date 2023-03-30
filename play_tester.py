# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
# print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

# print("\n-----Wave 03 user_data-----")
# pp.pprint(clean_wave_3_data())
# user_data = clean_wave_3_data()

# def get_friends_unique_watched(user_data):
#     friends_unique_watched = []
#     friends_watched_set = set()
#     user_watched_set = set()

#     for friend in user_data["friends"]:
#         for movie in friend["watched"]:
#             friends_watched_set.add(movie["title"])

#     for i in range(len(user_data["watched"])):
#         user_watched_set.add(user_data["watched"][i]["title"])

#     differences = friends_watched_set.difference(user_watched_set)

#     for friend in user_data["friends"]:
#         for movie in friend["watched"]:
#             if movie["title"] in differences and movie not in friends_unique_watched:
#                 friends_unique_watched.append(movie)
#                 continue
#     print("unique friends", friends_unique_watched)
#     return friends_unique_watched
# get_friends_unique_watched(user_data)

# Wave 04 user data
print("\n-----Wave 04 user_data-----")
pp.pprint(clean_wave_4_data())
user_data = clean_wave_4_data()
get_available_recs(user_data)

# Wave 05 user data
print("\n-----Wave 05 user_data-----")
pp.pprint(clean_wave_5_data())
