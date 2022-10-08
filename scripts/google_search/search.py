from googlesearch import search

query = input("Enter the query here: ")
results = search(query, num_results=10)

i = 1
for link in results:
    print("\n", i, ")", link)
    i += 1
