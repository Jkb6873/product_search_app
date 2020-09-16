--------------------
Description
--------------------

This is a Daily Harvest coding challenge app.
It provides endpoints to query a product.json file via ingredients.

--------------------
Requirements/ Startup
--------------------
- Requires Python 3.8
- run with
```
./startup.sh
```

---------------------
Endpoints
--------------------
```
/search
```
Http Method: GET
Parameters: ingredient => String
Response: Json
Response Codes: 200, 404

Sample 200 Response:
```
{
  "ingredient_id": 87,
  "ingredient_name": "Oregano"
  "products": [
    {
      "id": 56,
      "name": "Lentil + Tomato Bolonese"
    },
    {
      "id": 17,
      "name": "Tomato + Zucchini Minestrone"
    }
  ]
}
```
Sample 404 Response:
```
{
  "ingredient_name": "asdfddf",
  "msg": "No ingredient found named asdfddf"
}
```

--------------------
Further Information
--------------------

Writing this app, there seemed to be two main challenges.
1- to map the user's input to a valid ingredient.
2- to efficiently find each product with said ingredient.

The simple solution to the first problem would be to only match the ingredient name 100% literally. This is very simple, but leads to the problem of possibly not matching "Banana" to the valid ingredient "Organic Banana". So we opted to do lazy matching.

The second issue is more complex.
We could leave the data as is, meaning every time we look up products related to an ingredient, we do an O(n*k) lookup time search, with n being the amount of products, and k being the ingredients in each product.
This isn't too bad for now, when we only have 87 products, but as time goes on and products are added, it becomes more and more cumbersome.
Because of this, a little preprocessing should be done. On start up of the process, we read in the products.json file, and map every ingredient to a set of products.
This leads to a lookup time of O(1).
The downside is holding all the products in memory.
The ideal solution would be to refactor the imaginary database we have to use a many-to-many relationship between ingredients and products.

ie:
product_id  | ingredient_id
18  | 112
18  | 81
18  | 90
...

this would lead to ideal lookup times.
