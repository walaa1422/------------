import os
import numpy as np
import tensorflow
from tensorflow import keras

from PIL import Image, ImageOps


if __name__ == '__main__':
    data_dir = 'C:/Users/SHAHAD/Dropbox/PC/Desktop/TM/data-Gproject/mnist_png'
    testing_dir = os.path.join(data_dir, 'C:/Users/SHAHAD/Dropbox/PC/Desktop/TM/data-Gproject/testing')  # mnist_png/testing

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = tensorflow.keras.models.load_model('C:/Users/SHAHAD/Dropbox/PC/Desktop/TM/converted_keras/keras_model.h5')

    correct = 0
    for i in range(2):  
        filenames = os.listdir(os.path.join(testing_dir, str(i)))  # mnist_png/testing/1

        for filename in filenames:
            # Create the array of the right shape to feed into the keras model
            # The 'length' or number of images you can put into the array is
            # determined by the first position in the shape tuple, in this case 1.
            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

            # Replace this with the path to your image
            image = Image.open(os.path.join(testing_dir, str(i), filename))  # mnist_png/testing/1/37.png

            # resize the image to a 224x224 with the same strategy as in TM2:
            # resizing the image to be at least 224x224 and then cropping from the center
            size = (224, 224)
            image = ImageOps.fit(image, size, Image.LANCZOS) 

            # turn the image into a numpy array
            image_array = np.asarray(image)

            # display the resized image
            # image.show()

            # Normalize the image
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
            normalized_image_array = np.squeeze(normalized_image_array)  

            # Load the image into the array
            data[0] = normalized_image_array

            # run the inference
            prediction = np.argmax(model.predict(data)[0])

            if prediction == i:
                correct += 1

    print(f'Accuracy: {round(correct / 720 * 100, 2)}%')  