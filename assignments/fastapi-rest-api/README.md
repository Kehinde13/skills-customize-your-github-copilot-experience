# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using FastAPI that demonstrates core API concepts including route handling, request/response validation, and HTTP methods. This assignment reinforces understanding of web APIs, data structures, and modern Python web frameworks.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Application and Health Check

#### Description
Set up a basic FastAPI application with a root endpoint that returns a health check status. This establishes the foundation for the REST API and verifies that FastAPI is running correctly.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at `/` that returns a JSON response with a status message
- Include a `/health` endpoint that returns `{"status": "healthy"}`
- Run the server using `uvicorn` on `localhost:8000`

### 🛠️ Task 2: Create CRUD Endpoints for a Resource

#### Description
Implement full CRUD (Create, Read, Update, Delete) functionality for a simple resource such as tasks or books. Use in-memory storage with a Python list or dictionary.

#### Requirements
Completed program should:

- Define a GET `/items` endpoint that returns all stored items
- Define a GET `/items/{id}` endpoint that returns a single item by ID
- Define a POST `/items` endpoint that accepts JSON data and adds a new item
- Define a PUT `/items/{id}` endpoint that updates an existing item
- Define a DELETE `/items/{id}` endpoint that removes an item
- Return appropriate HTTP status codes (200 for success, 201 for created, 404 for not found)

### 🛠️ Task 3: Add Data Validation with Pydantic Models

#### Description
Refactor the CRUD endpoints to use Pydantic models for request and response validation. This ensures data integrity and provides automatic documentation in the Swagger UI.

#### Requirements
Completed program should:

- Define a Pydantic model for your resource (e.g., `Item`, `Task`, `Book`) with at least 3 fields
- Use the model in POST and PUT endpoints to validate incoming JSON
- Return properly typed responses using the model
- Use Pydantic's field validators to enforce constraints (e.g., non-empty strings, positive numbers)
- Test the API using the interactive `/docs` endpoint provided by FastAPI

### 🛠️ Task 4: Enhance with Error Handling and Status Codes (Stretch Goal)

#### Description
Add robust error handling and return meaningful HTTP status codes for edge cases such as missing items, invalid input, and duplicate entries.

#### Requirements
Completed program should:

- Return 404 when an item is not found (use `HTTPException`)
- Return 400 for invalid input (Pydantic handles this automatically)
- Return 409 (Conflict) or 400 for duplicate entries if applicable
- Include custom error messages in the response body
- Demonstrate proper HTTP status code semantics throughout the API
