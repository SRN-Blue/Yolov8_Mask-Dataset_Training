import os
import xml.etree.ElementTree as ET


def convert_voc_to_yolo(voc_folder, yolo_folder):
    # Create YOLO folder if it doesn't exist
    os.makedirs(yolo_folder, exist_ok=True)

    for xml_file in os.listdir(voc_folder):
        if not xml_file.endswith('.xml'):
            continue

        # Parse XML file
        tree = ET.parse(os.path.join(voc_folder, xml_file))
        root = tree.getroot()

        # Get image size
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # Open YOLO annotation file
        img_name = os.path.splitext(xml_file)[0] + '.txt'
        with open(os.path.join(yolo_folder, img_name), 'w') as yolo_file:
            for obj in root.findall('object'):
                # Get class label
                class_name = obj.find('name').text

                # Get bounding box coordinates
                bbox = obj.find('bndbox')
                x_min = int(bbox.find('xmin').text)
                y_min = int(bbox.find('ymin').text)
                x_max = int(bbox.find('xmax').text)
                y_max = int(bbox.find('ymax').text)

                # Convert coordinates to YOLO format
                x_center = (x_min + x_max) / (2.0 * width)
                y_center = (y_min + y_max) / (2.0 * height)
                box_width = (x_max - x_min) / width
                box_height = (y_max - y_min) / height

                # Write to YOLO annotation file
                yolo_file.write(f"{class_name} {x_center} {
                                y_center} {box_width} {box_height}\n")


voc_folder = r'.\archive_3\annotations'
yolo_folder = r'.\Mask_Dataset\Annotations'
convert_voc_to_yolo(voc_folder, yolo_folder)
