# -*- coding: utf-8 -*-
"""FaceNet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N2A52dCKjBLCWFrwYLG8C3cUqNgNy6LV
"""

import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
from google.colab.patches import cv2_imshow

# !unzip "/content/drive/MyDrive/data images/FEC_dataset.zip" -d "/content/drive/MyDrive/data images"

#df = pd.read_csv('/content/drive/MyDrive/data images/FEC_dataset/faceexp-comparison-data-train-public.csv', error_bad_lines=False, header=None)
df_cleaned = pd.read_csv('/content/drive/MyDrive/data images/FEC_dataset/faceexp-comparison-data-train-public_cleaned.csv', error_bad_lines=False, nrows=13000)

df_cleaned.head()

# header = ['index',
#           'link1',
#  'x11',
#  'x21',
#  'y11',
#  'y21',
#  'link2',
#  'x12',
#  'x22',
#  'y12',
#  'y22',
#  'link3',
#  'x13',
#  'x23',
#  'y13',
#  'y23',
#  'triplet type',
#  'annotator1_id',
#  'annotation1',
#  'annotator2_id',
#  'annotation2',
#  'annotator3_id',
#  'annotation3',
#  'annotator4_id',
#  'annotation4',
#  'annotator5_id',
#  'annotation5',
#  'annotator6_id',
#  'annotation6',
#  ]

# #df.columns = header
# df_cleaned.columns = header

## Importing Necessary Modules

import requests # to get image from the web
import shutil # to save it locally
import os

d = 0

for i in range(len(df)):
  flag = False
  for j in range(1, 4):
    if flag == True:
      continue
    
    image_url = df.iloc[i]['link'+str(j)]
    filename = '/content/drive/MyDrive/face images/'+'triplet'+str(d)+' img'+str(j)+'.jpg'
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

  
    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
    
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
        print('Image sucessfully Downloaded: ',filename)

    else:
        flag = True
        for k in range(1, j):
          filename = '/content/drive/MyDrive/face images/'+'triplet'+str(d)+' img'+str(k)+'.jpg'
          os.remove(filename)
          print('Image Deleted', d, k)
          
        
  
  if flag == True:
    
    df_cleaned = df_cleaned.drop(d)
    df_cleaned = df_cleaned.reset_index(drop=True)
    d = d-1
    

  d += 1

## export the cleaned df
df_cleaned.to_csv('/content/drive/MyDrive/data images/FEC_dataset/faceexp-comparison-data-train-public_cleaned.csv')

len(df_cleaned)

# ## visulaizing the triplets
# for i in range(40):
#   print()
#   print()
#   try :
#     for j in range(1, 4):
#       img = cv2.imread('/content/drive/MyDrive/face images/'+'triplet' + str(i) + ' img' + str(j)+ '.jpg')
#       x1 = df_cleaned.iloc[i]['x1'+str(j)]
#       x2 = df_cleaned.iloc[i]['x2'+str(j)] ## coordinates for face crop from image
#       y1 = df_cleaned.iloc[i]['y1'+str(j)]
#       y2 = df_cleaned.iloc[i]['y2'+str(j)]
#       height, width,channels = img.shape
#       crop = img[int(height*y1): int(height*y2), int(width*x1) : int(width*x2)]
#       crop = cv2.resize(crop, (299, 299))
#       plt.figure()
#       plt.imshow(crop)
#   except:
#     continue

def get_triplet(start, end):
  X = []
  for  i in range(start, end):
    print(i, end=' ')
     # this function will be used to iterate over triplets
    df_cleaned_i = df_cleaned.iloc[i]
    triplet = []
    for j in range(1, 4): # iterating over a triplet
      img = cv2.imread('/content/drive/MyDrive/face images/'+'triplet' + str(i) + ' img' + str(j)+ '.jpg') # reading the image
      x1 = df_cleaned_i['x1'+str(j)]
      x2 = df_cleaned_i['x2'+str(j)] ## coordinates for face crop from image
      y1 = df_cleaned_i['y1'+str(j)]
      y2 = df_cleaned_i['y2'+str(j)]

      height, width,channels = img.shape

      crop = img[int(height*y1): int(height*y2), int(width*x1) : int(width*x2)]
      crop = cv2.resize(crop, (299, 299))
      triplet.append(crop)
  
    annot = []
    for k in range(1, 7):
      annot.append(df_cleaned_i['annotation'+str(k)])

    dissimilar_img_index = int(np.median(annot))-1 # finding dissimalr image in a triplet

    #aligning the triplet in such a way that similar images occurs first then dissimilar this will help us after in triplet loss function

    triplet[2], triplet[dissimilar_img_index] = triplet[dissimilar_img_index], triplet[2] #swapping with last image

    X.append(triplet)

  return np.array(X)

X_val = get_triplet(12001, 12200)





