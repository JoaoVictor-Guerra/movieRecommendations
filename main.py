import requests

print(f'[\033[33m============== Welcome ================\033[m]')
numberOfRecommendations = int(input("How many movies do you want to get recommended? "))

# API Call
response = requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key=a99c516afeb73b4ae05aea918068ca57&language=en-US&sort_by=vote_count.desc&include_adult=false&include_video=false&page=1&with_watch_monetization_types=flatrate')
movies = response.json()

for c in range(numberOfRecommendations):
    selected = movies.get("results")[c]
    print(f'\033[34m============== Movie {c + 1} ================\033[m]')
    print(f'\033[92m{selected.get("original_title")}:\033[m {selected.get("overview")}')
    print(f'Image: {selected.get("poster_path")}; Score: {selected.get("vote_average")}')
    print(f'\033[34m============== End ================\033[m]\n')

print(f'[\033[33m============== Have a great watch ================\033[m]')

