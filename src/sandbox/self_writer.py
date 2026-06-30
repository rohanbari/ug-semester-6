import os
import sys

COUNT_DIR = "counter.txt"

# Create counter file if missing
if not os.path.exists(COUNT_DIR):
    with open(COUNT_DIR, "w") as f:
        f.write("0")

# Read and increment counter
with open(COUNT_DIR, "r+") as f:
    currentCount = int(f.read())
    f.seek(0)
    f.write(str(currentCount + 1))
    f.truncate()

# Build new file name
NEW_FILE_NAME = sys.argv[0] + f"_{currentCount + 1}"

# Read original script
with open(sys.argv[0], "r") as f:
    lines = f.read()

# Write to new file
with open(NEW_FILE_NAME, "w") as f:
    f.write(lines)

print("Write successful:", NEW_FILE_NAME)
