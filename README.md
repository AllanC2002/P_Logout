# Logout MicroService

This service is responsible for handling user logout functionality within a larger microservices architecture. It invalidates user sessions by processing JWT tokens.

## Table of Contents

- [Folder Structure](#folder-structure)
- [Backend Design Pattern](#backend-design-pattern)
- [Communication Architecture](#communication-architecture)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
  - [Locally](#locally)
  - [With Docker](#with-docker)
- [Running Tests](#running-tests)
- [Deployment](#deployment)

## Folder Structure

The project currently follows a relatively flat structure, suitable for a focused microservice:

-   **`main.py`**: The main application file containing the Flask app initialization and route definitions.
-   **`dockerfile`**: Instructions for building the Docker image for this service.
-   **`requirements.txt`**: A list of Python dependencies required for the project.
-   **`tests/`**: Contains automated tests for the application.
    -   **`test_logout.py`**: Unit tests for the logout functionality using `pytest`.
    -   **`route_test.py`**: An integration test script that interacts with this logout service and other related services (like a login service) to ensure end-to-end functionality.
-   **`.github/workflows/`**: Contains GitHub Actions workflows.
    -   **`docker-publish.yml`**: Defines the CI/CD pipeline for testing, building, and deploying the Docker image to an EC2 instance.
-   **`.gitignore`**: Specifies intentionally untracked files that Git should ignore.
-   **`__pycache__/`**: Directory for Python bytecode cache (automatically generated).

## Backend Design Pattern

This service employs a simple and direct **route-to-handler** pattern using the Flask framework. For each defined API endpoint, there's a corresponding Python function in `main.py` that handles the request and returns a response.

Given its focused nature as a microservice, more complex patterns like MVC or MVVM are not strictly necessary for this specific service but might be present in other services within the larger application ecosystem.

## Communication Architecture

-   **Protocol:** The service communicates over **HTTP/S**.
-   **Authentication:** Authentication is handled via **JSON Web Tokens (JWT)**. Clients are expected to send a Bearer token in the `Authorization` header of their requests.
-   **Microservices Interaction:** This logout service is designed to be part of a larger microservices architecture. The `tests/route_test.py` script demonstrates interaction with an external login service (to obtain a token) and implies the existence of other services (e.g., for account deletion). Communication between services is assumed to be primarily HTTP-based.

## API Endpoints

### Logout User

-   **Endpoint:** `/logout`
-   **Method:** `POST`
-   **Description:** Invalidates the provided JWT, effectively logging the user out.
-   **Headers:**
    -   `Authorization: Bearer <your_jwt_token>`
-   **Request Body:** None
-   **Responses:**
    -   **`200 OK`**: Logout successful.
        ```json
        {
          "message": "Logout successful."
        }
        ```
    -   **`401 Unauthorized`**:
        -   Token missing or invalid format.
            ```json
            {
              "error": "Token missing or invalid"
            }
            ```
        -   Token has expired.
            ```json
            {
              "error": "Token expired"
            }
            ```
        -   Token is invalid.
            ```json
            {
              "error": "Invalid token"
            }
            ```

*Note: Other services, such as a login service (e.g., `POST /login`) or an account deletion service (e.g., `DELETE /delete-account`), are part of the broader application architecture but are not hosted within this specific logout service. Please refer to their respective documentation.*

## Environment Variables

The application requires the following environment variables to be set:

-   **`SECRET_KEY`**: A secret key used for encoding and decoding JWTs. This must be kept confidential.

You can set these variables directly in your environment or use a `.env` file in the project root during local development (the application uses `python-dotenv` to load it).

Example `.env` file:
```
SECRET_KEY=your_super_secret_and_long_key_here
```
