# 📘 Assignment: Testing Python Code with pytest

## 🎯 Objective

Learn how to write automated tests using `pytest` for simple Python functions, including both normal behavior and edge cases.

## 📝 Tasks

### 🛠️ Task 1: Install pytest and run a sample test

#### Description
Install `pytest` and run a starter test file so you can see how pytest reports passing and failing tests.

#### Requirements
Completed program should:

- Install `pytest` in the local environment or verify it is available.
- Run `pytest` from the assignment folder.
- Observe that test results show passed and failed cases.
- Use the output to understand the test report.

### 🛠️ Task 2: Write tests for simple functions

#### Description
Write tests for a set of simple utility functions using pytest assertions.

#### Requirements
Completed program should:

- Implement tests for `is_palindrome()`, `calculate_discount()`, and `format_full_name()`.
- Cover normal cases and at least one edge case per function.
- Use `assert` statements to verify expected results.
- Include descriptive test function names.

### 🛠️ Task 3: Add fixtures and parameterized tests

#### Description
Use pytest fixtures and parameterized tests to reduce repetition and test multiple input values cleanly.

#### Requirements
Completed program should:

- Add a `pytest` fixture for shared input data.
- Use `@pytest.mark.parametrize` for at least one function.
- Confirm the parameterized test runs multiple cases.
- Keep tests readable and maintainable.

### 🛠️ Task 4: Make tests pass by implementing the functions

#### Description
Complete the function implementations in `src/utils.py` so the tests pass.

#### Requirements
Completed program should:

- Implement `is_palindrome(text: str) -> bool`.
- Implement `calculate_discount(price: float, discount_percent: float) -> float`.
- Implement `format_full_name(first_name: str, last_name: str) -> str`.
- Run `pytest` successfully with all tests passing.
