import tensorflow as tf

class VGG16(tf.keras.Model):
    """ Implement VGG16 arch"""

    def __init__(self, arch='vgg16'):
        super(VGG16, self).__init__()
