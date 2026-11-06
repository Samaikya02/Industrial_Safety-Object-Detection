import pyttsx3

CLASSES = {
    0: 'Hardhat', 1: 'Mask', 2: 'NO-Hardhat', 3: 'NO-Mask',
    4: 'NO-Safety Vest', 5: 'Person', 6: 'Safety Cone',
    7: 'Safety Vest', 8: 'machinery', 9: 'vehicle'
}

engine = pyttsx3.init()

def speak_alerts(detected_classes):
    for label in detected_classes:
        if label == 'NO-Hardhat':
            engine.say("Please wear a hardhat.")
        elif label == 'NO-Mask':
            engine.say("Please wear a mask.")
        elif label == 'NO-Safety Vest':
            engine.say("Please wear a safety vest.")
    engine.runAndWait()

def get_violations(results):
    labels = []
    for box in results.boxes:
        if box.conf < 0.3:
            continue
        cls = int(box.cls)
        label = CLASSES.get(cls)
        if label in ['NO-Hardhat', 'NO-Mask', 'NO-Safety Vest']:
            labels.append(label)
    return labels
