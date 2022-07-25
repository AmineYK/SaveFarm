
# -----------------------------------------------------------
# --------------------- F U N C T I O N S -------------------
# -----------------------------------------------------------

import numpy as np
import pathlib
import cv2
import tensorflow as tf
from tensorflow import keras 


def get_X_and_Y(path,values):
    
    data_dir = pathlib.Path(path)

     
    indexes = ["value"+str(i) for i in range(len(values))]
    somes = [list(data_dir.glob(values[v]+"/*")) for v in range(len(values))]
    labels = [v for v in range(len(values))]
    
    dire_images = dict(zip(indexes, somes))
    dire_labels = dict(zip(indexes, labels))
    
    
    X = []
    Y = []

    for name,images in dire_images.items():
        for image in images:
            img = cv2.imread(str(image))
            X.append(img)
            Y.append(dire_labels[name])
            
    return np.array(X),np.array(Y)

def augmentation(layer):
    return tf.keras.Sequential([layer]) 


def data_augmentation(X,Y):
    augm1 = augmentation(tf.keras.layers.experimental.preprocessing.RandomRotation(0.9))
    augm2 = augmentation(tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"))
    augm3 = augmentation(tf.keras.layers.experimental.preprocessing.RandomZoom(0.2))
    augm4 = augmentation(tf.keras.layers.experimental.preprocessing.RandomFlip("horizontal"))
    augm5 = augmentation(tf.keras.layers.experimental.preprocessing.RandomFlip("vertical"))
    
    X_aug = np.concatenate((X,augm1(X),augm2(X),augm3(X),augm4(X),augm5(X)))
    Y_aug = np.concatenate((Y,Y,Y,Y,Y,Y))
    
    return X_aug,Y_aug

def AddImages(path,values,X_aug,Y_aug):
    lbl = ""
    for index in range(X_aug.shape[0]):
        lbl = values[Y_aug[index]]
        finalpath = path+lbl+"/image"+str(index)+".jpg"
        cv2.imwrite(finalpath,X_aug[index])



# -----------------------------------------------------------
# ------------------------ S C R I P T 01 -------------------
# -----------------------------------------------------------

# Using Deep Learning layers

# PEPPER
# ------
path = "PlantVillage/Pepper/"
values = ["Pepper__bell___Bacterial_spot","Pepper__bell___healthy"]

X1,Y1=get_X_and_Y(path,values)
X_aug,Y_aug = data_augmentation(X1,Y1)

AddImages(path,values,X_aug,Y_aug)


# Potato
# ------
path = "PlantVillage/Potato/"
values = ["Potato___Early_blight","Potato___Late_blight","Potato___healthy"]

X1,Y1=get_X_and_Y(path,values)
X_aug,Y_aug = data_augmentation(X1,Y1)

AddImages(path,values,X_aug,Y_aug)



# -----------------------------------------------------------
# ------------------------ S C R I P T 02 -------------------
# -----------------------------------------------------------

# Using the library ImageDataGenerator


from tensorflow.keras.preprocessing.image import ImageDataGenerator


datagen = ImageDataGenerator(
    rescale = 1./255,
    horizontal_flip = True,
    rotation_range = 10
)

gen = datagen.flow_from_directory(
    'PlantVillage',
    target_size = (256,256),
    batch_size = 32,
    class_mode = "sparse",
    save_to_dir = "Augmented_Images"
)