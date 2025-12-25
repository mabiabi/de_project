from src.extract.read_sales_csv_chunked import read_sales_csv_chunked

chunks = read_sales_csv_chunked("data/sales_data_large.csv", 50000)

first_chunk = next(chunks)
print(first_chunk.head(7))  # Display first 7 rows of the first chunk
second_chunk = next(chunks)
print(second_chunk.head(7))  # Display first 7 rows of the second chunk

# You can continue to get more chunks as needed
