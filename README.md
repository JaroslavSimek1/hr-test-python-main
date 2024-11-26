# DESO applicant test for Python back-end position

This test consists of two parts. 

The first part will test your general knowledge about databases. 

The second part focuses on some key feature of python.

During the implementation please use basic git features to show your steps through the completion of this test. And of course, follow all the best-practices that you know.


## Database

In the file [database.sql](./database.sql) prepare the script in your preferred SQL dialect.

The script should create a database structure with anything you deem necessary for storing data for a book shop, so there should information about the following:
- Genres
- Books/authors
- Inventory information
- Prices
- Orders

You do not have to go into details with the entity attributes, use as little as possible.
For example in the case of a book, all you need to know is the name, brief description, cover image, author, price, and availability.


## Python

In this part we will build upon the database you have created. You will have to prepare the bare minimum to work with the database.

There is a `ConnectionSimulator` dummy class implemented in [connection_simulator](./connection_simulator.py), so you can use that to simulate the database connection and execute queries. 

The `execute_query` function **always returns an empty list**. Please work with the assumption that the **result** is a **list of dicts**, where each dict represents one row from the result and has a format of `{ "column_name": column_value }`.  

Your tasks are:
1. In the file [entities](./entities.py) please create class definitions for your database entities as you would map them for a client
2. In the file [data](./data.py) please implement function that will cover CRUD operations for the entities, allowing for basic filtering and returning the entities themselves (or their lists) (for the queries use the same SQL dialect as you used to create the database structure)


