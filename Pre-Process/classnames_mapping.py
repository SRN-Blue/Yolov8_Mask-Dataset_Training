import os

# Define the class mapping
class_mapping = {"without_mask": 0, "with_mask": 1, "mask_worn_incorrectly": 2}

# Directory containing annotation files
annotations_dir = r".\Mask_Dataset\val"

# Loop through each annotation file
for filename in os.listdir(annotations_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(annotations_dir, filename)
        updated_lines = []

        # Read lines from the annotation file
        with open(filepath, "r") as f:
            lines = f.readlines()

        # Replace class names with numeric class IDs
        for line in lines:
            parts = line.strip().split()
            class_name = parts[0]
            if class_name in class_mapping:
                class_id = class_mapping[class_name]
                parts[0] = str(class_id)
                updated_lines.append(" ".join(parts) + "\n")

        # Write updated lines back to the annotation file
        with open(filepath, "w") as f:
            f.writelines(updated_lines)

print("Class names replaced with numeric IDs in annotation files.")
