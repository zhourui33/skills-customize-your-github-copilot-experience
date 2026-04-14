# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using Python's FastAPI framework. You will create a simple API with endpoints for managing a collection of items, learning about HTTP methods, request handling, and response models along the way.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI Application

#### Description
Set up a new FastAPI project and create a basic application with a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Define a `GET /` endpoint that returns `{"message": "Welcome to my API"}`
- Run successfully with `uvicorn main:app --reload`


### 🛠️	Build CRUD Endpoints for an Items Collection

#### Description
Create a full set of CRUD (Create, Read, Update, Delete) endpoints to manage a list of items stored in memory. Each item should have an `id`, `name`, and `description`.

#### Requirements
Completed program should:

- Define a Pydantic model `Item` with fields `id` (int), `name` (str), and `description` (str)
- Implement `GET /items` to return all items
- Implement `GET /items/{item_id}` to return a single item by ID, or a 404 error if not found
- Implement `POST /items` to add a new item and return it with a 201 status code
- Implement `PUT /items/{item_id}` to update an existing item by ID
- Implement `DELETE /items/{item_id}` to remove an item by ID


### 🛠️	Add Query Parameters and Filtering

#### Description
Enhance the `GET /items` endpoint to support optional query parameters for filtering and pagination.

#### Requirements
Completed program should:

- Accept an optional `name` query parameter to filter items by name (case-insensitive partial match)
- Accept optional `skip` (default 0) and `limit` (default 10) query parameters for pagination
- Return the filtered and paginated list of items
