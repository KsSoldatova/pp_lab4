from typing import List
from cv2 import DFT_COMPLEX_INPUT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

pd.options.mode.chained_assignment = None


def create_DataFrame() -> pd.DataFrame:
    """This function takes data from 2 annotations and create dataframe with 2 columns:abs path and class"""
    df1=pd.read_csv(r"C:\Users\kssol\PycharmProjects\pythonProject2\annotation_rose.csv",sep=',', header=None,encoding='UTF-16')
    df2=pd.read_csv(r"C:\Users\kssol\PycharmProjects\pythonProject2\annotation_tulip.csv",sep=',', header=None,encoding='UTF-16')
    df = pd.concat([df1, df2], ignore_index=True)
    df.drop(1, axis=1, inplace=True)
    df.rename(columns={0: 'absolute_path', 2: 'dataset_class'}, inplace=True)
    return df
    
    


def add_mark(df: pd.DataFrame) -> None:
    """This function adds third column in dataframe - mark of image(1 or 0)"""
    value = []
    for item in df['dataset_class']:
        if item == 'rose':
            value.append(0)
        else:
            value.append(1)
    df['mark'] = value


def add_hwc_columns(df: pd.DataFrame) -> None:
    """This function adds to dataframe 3 columns: height, width and channels of the image"""
    img_width = []
    img_height = []
    img_channel = []
    for item in df['absolute_path']:
        img = cv2.imread(item)
        img_height.append(img.shape[0])
        img_width.append(img.shape[1])
        img_channel.append(img.shape[2])
    df['height'] = img_height
    df['width'] = img_width
    df['channel'] = img_channel
