"""
FastAPI REST API Starter Code

This starter file provides the basic structure for building a REST API with FastAPI.
Students should implement the endpoints and data models according to the assignment.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI(title="My REST API", version="1.0.0")

# TODO: Define your Pydantic model here
# Example structure:
# class Item(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None
#     price: float

# TODO: Create in-memory storage (list or dict)
# items = []
# or
# items = {}

# Task 1: Health Check Endpoint
@app.get("/")
def read_root():
    """Root endpoint - returns welcome message"""
    # TODO: Implement this endpoint to return a welcome message
    pass

@app.get("/health")
def health_check():
    """Health check endpoint"""
    # TODO: Implement this endpoint to return {"status": "healthy"}
    pass

# Task 2: CRUD Endpoints
@app.get("/items")
def get_all_items():
    """Retrieve all items"""
    # TODO: Return all items from storage
    pass

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a single item by ID"""
    # TODO: Return item by ID or raise HTTPException(status_code=404)
    pass

@app.post("/items")
def create_item(item: dict):  # TODO: Replace dict with your Pydantic model
    """Create a new item"""
    # TODO: Add item to storage and return it
    pass

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):  # TODO: Replace dict with your Pydantic model
    """Update an existing item"""
    # TODO: Update item in storage or raise HTTPException(status_code=404)
    pass

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item"""
    # TODO: Remove item from storage or raise HTTPException(status_code=404)
    pass

# To run the server:
# uvicorn starter_code:app --reload
