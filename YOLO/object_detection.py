import numpy as np
import urllib.request
import cv2

url = 'http://192.168.1.16/cam.jpg'

whT = 320
confThreshold = 0.5
nmsThreshold = 0.3
classesfile = 'coco.names.txt'
classNames = []

with open(classesfile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfig = 'yolov31.cfg'
modelWeights = 'yolov3.weights'
net = cv2.dnn.readNetFromDarknet(modelConfig, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def findObject(outputs, im):
    hT, wT, cT = im.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

    if len(indices) > 0:
        for i in indices.flatten():
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]

            if classNames[classIds[i]] == 'bird':
                found_bird = True
            elif classNames[classIds[i]] == 'cat':
                found_cat = True

            # Dessiner le rectangle
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 255), 2)

            # Préparer le texte
            text = f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%'

            # Calculer la taille du texte
            (text_width, text_height), baseline = cv2.getTextSize(
                text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)

            # === CORRECTION ICI ===
            # Position Y : toujours garder le texte dans le cadre
            if y - text_height - 15 >= 0:
                # Il y a assez d'espace en haut
                text_y = y - 10
            elif y + h + text_height + 15 <= hT:
                # Afficher en dessous du rectangle
                text_y = y + h + text_height + 10
            else:
                # Afficher à l'intérieur en haut du rectangle
                text_y = y + text_height + 10

            # Position X : toujours garder le texte dans le cadre
            if x + text_width + 5 > wT:
                # Le texte dépasse à droite, le décaler à gauche
                text_x = wT - text_width - 5
            elif x < 5:
                # Le texte dépasse à gauche
                text_x = 5
            else:
                # Position normale
                text_x = x

            # Ajouter un fond rectangulaire pour une meilleure lisibilité
            padding = 3
            cv2.rectangle(im,
                          (text_x - padding, text_y - text_height - padding),
                          (text_x + text_width + padding, text_y + baseline + padding),
                          (255, 0, 255), -1)

            # Afficher le texte en blanc
            cv2.putText(im, text, (text_x, text_y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

while True:
    while True:
        try:
            img_resp = urllib.request.urlopen(url)
            imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
            im = cv2.imdecode(imgnp, -1)

            if im is None:
                print("Erreur: Impossible de lire l'image")
                continue

            blob = cv2.dnn.blobFromImage(im, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
            net.setInput(blob)

            layernames = net.getLayerNames()

            try:
                outputNames = [layernames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            except:
                outputNames = [layernames[i - 1] for i in net.getUnconnectedOutLayers()]

            outputs = net.forward(outputNames)
            findObject(outputs, im)

            # NOUVELLE LIGNE : Redimensionner l'image
            im_resized = cv2.resize(im, (0, 0), fx=0.5, fy=0.5)

            # Afficher l'image redimensionnée
            cv2.imshow('ESP32-CAM Detection', im_resized)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        except Exception as e:
            print(f"Erreur: {e}")
            continue

    cv2.destroyAllWindows()
