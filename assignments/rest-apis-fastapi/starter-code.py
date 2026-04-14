from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()

# --- Models ---


class Item(BaseModel):
    id: int
    name: str
    description: str


# --- In-memory storage ---

items: list[Item] = []

# --- Task 1: Root endpoint ---

# TODO: Create a GET endpoint at "/" that returns {"message": "Welcome to my API"}

# --- Task 2: CRUD endpoints ---

# TODO: Create a GET endpoint at "/items" that returns all items

# TODO: Create a GET endpoint at "/items/{item_id}" that returns a single item or 404

# TODO: Create a POST endpoint at "/items" that adds a new item (status code 201)

# TODO: Create a PUT endpoint at "/items/{item_id}" that updates an existing item

# TODO: Create a DELETE endpoint at "/items/{item_id}" that removes an item

# --- Task 3: Query parameters and filtering ---

# TODO: Update GET "/items" to accept optional query parameters:
#   - name: filter by name (case-insensitive partial match)
#   - skip: number of items to skip (default 0)
#   - limit: max number of items to return (default 10)
