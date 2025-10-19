# Fenwick Tree (Binary Indexed Tree) Example

# Original array (0-indexed)
arr = [1, 2, 3, 4, 5]

# Size of array
n = len(arr)

# Fenwick tree array (1-indexed, so size n+1)
fenwick = [0] * (n + 1)  # fenwick[0] is unused

# -------------------------------
# Function to update the tree
# Add 'val' to index 'i' in the original array
# -------------------------------
def update(fenwick, i, val):
    """
    fenwick: Fenwick tree array
    i: index in tree (1-indexed)
    val: value to add
    """
    while i < len(fenwick):
        fenwick[i] += val       # Add val to current node
        print(f"Update: Added {val} to fenwick[{i}], now fenwick = {fenwick}")
        i += i & -i             # Move to next responsible node

# -------------------------------
# Function to get prefix sum
# Sum of first i elements (1-indexed)
# -------------------------------
def prefix_sum(fenwick, i):
    result = 0
    while i > 0:
        result += fenwick[i]    # Add value at current node
        print(f"Sum: Adding fenwick[{i}] = {fenwick[i]}, partial sum = {result}")
        i -= i & -i             # Move to parent node
    return result

# -------------------------------
# Build the Fenwick tree
# -------------------------------
for idx, val in enumerate(arr):
    update(fenwick, idx + 1, val)  # +1 because tree is 1-indexed

print("\nInitial Fenwick Tree:", fenwick)

# -------------------------------
# Test prefix sums
# -------------------------------
print("\nPrefix sums:")
for i in range(1, n + 1):
    print(f"Sum of first {i} elements = {prefix_sum(fenwick, i)}")

# -------------------------------
# Test update
# -------------------------------
print("\nUpdating arr[1] (2nd element) by +5")
update(fenwick, 2, 5)  # arr[1] += 5

print("\nFenwick Tree after update:", fenwick)

print("\nPrefix sums after update:")
for i in range(1, n + 1):
    print(f"Sum of first {i} elements = {prefix_sum(fenwick, i)}")
