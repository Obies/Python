#Program shows random jokes from list
#by importing random module
import random

#list of jokes to display
jokes_list = ["What do you call a boomerang that won’t come back? A stick!", "How does a cucumber become a pickle? It goes through a jarring experience!",
"Why did the kid bring a ladder to school? Because she wanted to go to high school!", "What do you call two birds in love? Tweethearts",
"How are false teeth like stars? They come out at night."]

#prints out random joke from the jokes list
print(random.choice(jokes_list))
