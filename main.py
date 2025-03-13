def penguhop_search(query):
    """
    Simulates a penguin search engine.

    Args:
        query: The search query (string).

    Returns:
        A list of matching documents.
    """

    search_index = {
        "Emperor Penguins": "These penguins are the largest and live in Antarctica.",
        "Fish": "Penguins love to eat fish, krill, and squid.",
        "Migration": "Some penguins migrate long distances to find food.",
        "Ice Slides": "Penguins often slide on their bellies across the ice.",
        "Nesting": "Penguins build nests out of pebbles and ice.",
    }

    results = []
    query_lower = query.lower() #makes the search case insensitive.

    for topic, document in search_index.items():
        if query_lower in topic.lower() or query_lower in document.lower():
            results.append(document)

    return results

# Example usage:
search_query = "fish"
search_results = penguhop_search(search_query)

if search_results:
    print(f"Search results for '{search_query}':")
    for result in search_results:
        print(f"- {result}")
else:
    print(f"No results found for '{search_query}'.")

search_query = "ice slides"
search_results = penguhop_search(search_query)

if search_results:
    print(f"Search results for '{search_query}':")
    for result in search_results:
        print(f"- {result}")
else:
    print(f"No results found for '{search_query}'.")

search_query = "warm weather"
search_results = penguhop_search(search_query)

if search_results:
    print(f"Search results for '{search_query}':")
    for result in search_results:
        print(f"- {result}")
else:
    print(f"No results found for '{search_query}'.")
