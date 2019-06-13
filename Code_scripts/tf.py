import pandas as pd
import numpy as np
import os
import  random
import sys

import imageio
import skimage
import skimage.io
import skimage.transform
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import  tools
from plotly.offline import  download_plotlyjs, plot
import scipy
from sklearn.model_selection import train_test_split
from sklearn import metrics
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPool2D, Dropout, BatchNormalization, LeakyReLU
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping, ReduceLROnPlateau, LearningRateScheduler
from keras.utils import to_categorical
import tensorflow

#we will be using tensorflow as backend.

IMAGE_PATH = 'Q:\\tensorflow\\datasets\\bee_imgs\\bee_imgs\\'
IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100
IMAGE_CHANNELS = 3
RANDOM_STATE = 2018
TEST_SIZE = 0.2
VAL_SIZE = 0.2
CONV_2D_DIM_1 = 16
CONV_2D_DIM_2 = 16
CONV_2D_DIM_3 = 32
CONV_2D_DIM_4 = 64
MAX_POOL_DIM = 2
KERNEL_SIZE = 3
BATH_SIZE = 32
NO_EPOCHS_1 = 5
NO_EPOCHS_2 = 10
NO_EPOCHS_3 = 50
PATIENCE = 5
VERBOSE = 1

msg = os.listdir("Q:/tensorflow/d")
print(msg)

honey_bee_df = pd.read_csv('Q:/tensorflow/input/bee_data.csv')
print(honey_bee_df.sample(100).head())
variables = honey_bee_df.isnull().sum()
tmp = honey_bee_df.groupby(['zip code'])['location'].value_counts()
df = pd.DataFrame(data = {'Images': tmp.values}, index=tmp.index).reset_index()
print(df)

locations = (honey_bee_df.groupby(['location'])['location'].nunique()).index

def draw_category_images(var, cols=5):
    categories = (honey_bee_df.groupby([var])[var].nunique()).index
    f, ax = plt.subplots(nrows=len(categories), ncols=cols, figsize=(2*cols, 2*len(categories)))
    #draw a number of images for each location
    for i, cat in enumerate(categories):
        sample = honey_bee_df[honey_bee_df[var]==cat].sample(cols)
        for j in range(0,cols):
            file = IMAGE_PATH + sample.iloc[j]['file']
            im = imageio.imread(file)
            ax[i,j].imshow(im, resample=True)
            ax[i,j].set_title(cat, fontsize = 9)
        plt.tight_layout()
        plt.show()

draw_category_images("location")



