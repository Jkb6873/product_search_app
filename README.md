--------------------
Description
--------------------

This is a Daily Harvest coding challenge app.
It provides endpoints to query a product.json file via ingredients found in an ingredients.json file.

--------------------
Requirements/ Startup
--------------------
- Requires Python 3.7.2, tested on macOS Mojave
- run with
```
sh startup.sh
```

--------------------
Testing
--------------------
- run unit/ integration tests with
```
sh startup.sh test
```

--------------------
Endpoints
--------------------
```
/search
```
Http Method: GET
Parameters: ingredient => String
Response: JSON
Response Codes: 200, 400

Sample 200 Response:
```
[
    {
        "collection": "Soup",
        "id": 17,
        "name": "Tomato + Zucchini Minestrone"
    },
    {
        "collection": "Harvest Bowl",
        "id": 56,
        "name": "Lentil + Tomato Bolognese"
    }
]
```
Sample 400 Response:
```
{
    "error": "No products found containing ingredient 'asdadfasd'"
}
```

--------------------
Further Information
--------------------

Writing this app, there seemed to be two main challenges.
1- to map the user's input to a valid ingredient.
2- to efficiently find each product with said ingredient.

The first problem has three solutions.
- We can match only to the exact ingredient name, ie "Organic Banana" only matches "Organic Banana" but not "Banana". We can recommend valid keywords similar enough to the user input, but that might be exploited.
- We can do a regex check to see if the word contains any of the user input. This has the issue of requiring results from both "Organic Coconut" and "Coconut Water" on the input "coconut", but even more worrying, most records would be returned on the input "a". This was avoided, even though it would be a good solution if we wanted to recommend "nearby" ingredients.
- We can match based on Levensthein Distance, which is the difference between two strings. This has good results for things like "Banana" matching "bananas" or "bsnana" but poor results with multiple word strings.

The simplest solution was chosen.

The second issue is more complex, but also had three solutions.
- Search through the json on every request. This is the worst solution, because it means searching through every product, and every ingredient in the product's ingredientIds. It can be improved by using caching, but it is still very inefficient if the input is varied.
- Preprocess by creating a map from ingredients to products. This is a better solution because it has a one time cost on startup, and has constant time lookups afterwards. The downside is that it is not extensible, meaning if we wanted to add more functionality to the api, we would have to make a more and more complicated mapping to maintain the speed benefits.
- Preprocess by loading the json files into an in-memory relational database, which lets us use efficient b-tree indexing for fast lookups via name or id. This is the ideal solution in case we want to add more functionality to the api, though solution 2 is faster if we only care about the current task.

The last solution was chosen.
