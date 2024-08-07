# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

## IMPLEMENTED BASIC AUTHENTICATION

- Basic Authentication
This project includes an implementation of Basic Authentication to secure access to the API endpoints. Basic Authentication requires users to provide a valid username and password in the request headers to authenticate their identity.

- How It Works
Client Requests Access:

The client sends a request to the server, including an Authorization header with the format: Authorization: Basic <credentials>.
<credentials> is the Base64-encoded string of the format username:password.
Server Validates Credentials:

The server decodes the Base64 string to retrieve the username and password.
The server checks these credentials against the stored user data (e.g., a database or an in-memory list).
Access Granted or Denied:

If the credentials are valid, the server processes the request and returns the appropriate response.
If the credentials are invalid, the server returns a 401 Unauthorized response.
Usage
To implement Basic Authentication in your requests:

Encode your username and password in Base64 format:

bash
Copy code
echo -n "username:password" | base64
Include the encoded string in the Authorization header of your HTTP request:

http
Copy code
GET /secure-endpoint HTTP/1.1
Host: example.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
Security Considerations
Encryption: Always use Basic Authentication over HTTPS to ensure credentials are encrypted during transmission.
Credential Storage: Avoid hard-coding credentials in your source code. Use environment variables or secure vaults to manage sensitive information.
Token Management: Consider implementing more secure authentication mechanisms like OAuth2 for production applications, especially if sensitive data is involved.
Testing
To test Basic Authentication locally, use tools like Postman, curl, or any HTTP client that allows setting custom headers.

Example using curl:

bash
Copy code
curl -u username:password https://example.com/secure-endpoint

Session Authentication
Session authentication is a method of managing user sessions securely by creating a unique session identifier (session ID) for each user when they log in. This session ID is stored on the client side, typically in a cookie, and is used to authenticate the user for subsequent requests.

Key Components
Session Management: Upon successful login, a session ID is generated and associated with the user. This session ID is stored in a secure cookie on the client side.

Session Validation: For each request, the server checks the session ID in the incoming cookie to validate the user's session. If the session is valid, the user is granted access to the requested resource.

Session Expiry: Sessions have a limited lifespan for security purposes. After a certain period of inactivity, the session will expire, requiring the user to log in again.

Implementation Details
Login Endpoint: The user submits their credentials (e.g., username and password) to the login endpoint. Upon successful authentication, a session ID is generated and returned in a cookie.

Protected Endpoints: Subsequent requests to protected endpoints must include the session ID in the cookie. The server checks this ID against its records to verify the session.

Logout Endpoint: The user can log out, which invalidates their session ID, making it unusable for future requests.

Example Usage
User Login:

POST /login
Body: { "username": "user", "password": "pass" }
Response: A cookie with the session ID.
Access Protected Resource:

GET /protected-resource
Include the session ID in the cookie.
User Logout:

POST /logout
The session ID is invalidated.
Security Considerations
Secure Cookies: Ensure session cookies are marked as HttpOnly and Secure to prevent client-side access and to only send them over HTTPS.

Session Expiry: Implement a reasonable session timeout to reduce the risk of session hijacking.

Regenerate Session ID: Consider regenerating the session ID after each login to mitigate session fixation attacks.
