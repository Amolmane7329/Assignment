# Function to suggest completions based on a prefix search
def suggest_completions(search_history, query):
    # Filter and return matching suggestions from search_history
    return [item for item in search_history if item.startswith(query)]

# Sample search history
search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

# Input from the user
query = input("Enter your partial search query: ").lower()

# Get the suggestions based on the partial query
suggestions = suggest_completions(search_history, query)

# Display the suggestions
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
