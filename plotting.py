import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Load the Data
df = pd.read_csv('skiplist_results.csv') # Ensure headers in CSV match: N, Insert, Search, Delete

# 2. Create the Plot
plt.figure(figsize=(15, 5))


# --- INSERTION PLOT ---
plt.subplot(1, 3, 1)
plt.plot(df['Operations'], df[' Insertion Time (ms)'], marker='o', color='blue', label='Skip List')
plt.title('Insertion Time Analysis')
plt.xlabel('Input Size (N)')
plt.ylabel('Time (microseconds)')
plt.grid(True)
plt.legend()

# --- SEARCH PLOT ---
plt.subplot(1, 3, 2)
plt.plot(df['Operations'], df[' Search Time (ms)'], marker='o', color='green', label='Skip List')
plt.title('Search Time Analysis')
plt.xlabel('Input Size (N)')
plt.grid(True)
plt.legend()

# --- DELETION PLOT ---
plt.subplot(1, 3, 3)
plt.plot(df['Operations'], df[' Deletion Time (ms)'], marker='o', color='red', label='Skip List')
plt.title('Deletion Time Analysis')
plt.xlabel('Input Size (N)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
