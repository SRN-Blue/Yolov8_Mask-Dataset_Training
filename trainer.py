from ultralytics import YOLO

if __name__ == '__main__':
    # Load the model.
    model = YOLO('yolov8n.pt')

    # Training.
    results = model.train(
        data=r'.\train.yaml',
        imgsz=640,
        epochs=10,
        batch=8,
        device='cpu',
        name='yolov8n_Mask_detector')
