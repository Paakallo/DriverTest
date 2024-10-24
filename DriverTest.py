import time

# Start time
start_time = time.time()

# Code block you want to measure
# Example: simple loop
for i in range(1000000):
    pass  # Your code here

# End time
end_time = time.time()

# Calculate the execution time
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")

