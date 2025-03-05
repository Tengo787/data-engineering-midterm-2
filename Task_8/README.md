# Task 8 - FastAPI and SQLite

This project sets up a FastAPI application that retrieves data from an SQLite database and exposes it via an API endpoint.

## Steps to Run

1. **Clone the Repository**  
   ```sh
   git clone <repo_url>
   cd Task_8
   ```

2. **Build Docker Image**  
   ```sh
   docker build -t task8_image .
   ```

3. **Run the Container**  
   ```sh
   docker run --rm -p 8000:8000 task8_image
   ```

4. **Access the API**  
   Open the browser or use curl to test:  
   ```sh
   curl http://127.0.0.1:8000/users
   ```

5. **Interactive Docs**  
   Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for FastAPI auto-generated documentation.
