# Task 7 - Docker and Python
This project reads a CSV file, processes it (filtering, grouping, aggregation), and saves the results in a new CSV file.

## Steps to Run
1. **Clone the Repository**
   ```sh
   git clone <repo_url>
   cd Task_7
   ```
2. **Build Docker Image**
   ```sh
   docker build -t task7_image .
   ```
3. **Run the Container**
   ```sh
   docker run --rm -v $(pwd):/app task7_image
   ```
4. **Check the Processed File**
   The results will be saved in `output.csv`.
