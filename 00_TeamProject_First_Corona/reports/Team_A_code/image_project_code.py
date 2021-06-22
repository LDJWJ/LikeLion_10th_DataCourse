# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:24:18 2019

@author: LGULTRA
"""

#%% 라이브러리 가져오기
from sklearn import model_selection
from sklearn.model_selection import train_test_split
from PIL import Image
import os, glob
import numpy as np

#%% 데이터 불러오기
root_dir = "C:\\Users\\LGULTRA\\Desktop\\kfood\\"  #나중에 디렉토리 수정하기!

#%% 카테고리 지정해주기

categories = ["Airplane", "Bicycle", "Bus",
              "Car", "Helicopter", "HotAirBallon",
              "MotorBike", "Ship", "Train", "Truck"]

nb_classes = len(categories)

#%% 이미지 크기 지정해주기
image_width = 64
image_height = 64

#%% 이미지 데이터 X, 레이블 Y
X = [] # 이미지 데이터
Y = [] # 레이블 데이터

for idx, category in enumerate(categories):
    image_dir = root_dir + category
    files = glob.glob(image_dir + '/' + '*.jpg) #png는 어떻게 하지? files를 2개로 나누나?
    print(image_dir + "/" + "*.jpg")
    
    for i, f in enumerate(files):
        #이미지로딩
        img = Image.open(f)
        img = img.convert('RGB')
        img = img.resize((image_width, image_height))
        data = np.asarray(img)
        X.append(data)
        Y.append(idx)

X = np.array(X)
Y = np.array(Y)
print(X.shape, Y.shape)
        
#%% 데이터 셋 나누기
X_train, X_test, y_train, y_test = train_test_split(X, Y)
xy = (X_train, X_test, y_train, y_test)

#%% 데이터 파일 저장
np.save(root_dir+ "transportation.npy", xy)

#%% 모델링 시작하기: 필요한 라이브러리 불러오기

import sys, os
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Activation
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np

#%% 데이터 불러오고 def 로 정리해주기

def load_dataset():
    x_train, x_test, y_train y_test = np.load(root_dir + "transportation.npy", allow_pickle = True)
    x_train = x_train.astype('float')/256
    x_test = x_test.astype('float')/256
    y_train = np_utils_to_categorical(y_train, nb_classes)
    y_test = np_utils_to_categorical(y_test, nb_classes)
    return x_train, x_test, y_train, y_test

#%% 모델 구성하기
    
def build_model(in_shape):
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, border_mode = 'same',
                            input_shape=in_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))
    
    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='binary_crossentropy',
                  optimizer = 'rmsprop',
                  metrics = ['accuracy'])
        
    return model

#%% 모델 학습 수행 후, 모델을 파일로 저장하기
    
def model_train(x,y):
    model = build_model(x.shape[1:])
    model.fit(x, y, batch_size=32, epochs=20)
    
    return model 

#%% 모델 평가하기
    
def model_eval(model, x, y):
    score = model.evaluate(x, y)
    print("loss=", score[0])
    print("accuracy=", score[1])

#%% 모델 학습/평가/저장

x_train, x_test, y_train, y_test = load_dataset()
model = model_train(x_train, y_train)
model_eval(model, x_test, y_test)
    
#%% 모델 저장
model.save(root_dir + "transportation_model.h5")

#%% 모델 테스트 - 우선 라이브러리 불러오기
import sys, os
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
from keras.models import load_model
from PIL import Image
import numpy as np

#%% 테스트 파일 루트 디렉토리 설정하기
root_dir = "to_be_updated!"

#%% 테스트파일 디렉토리 설정

test_dir = root_dir + 'test_img/'
image_list = os.listdir(test_dir)

#%%
image_files = []

for i in image_list:
    test_sample = root_dir + "test_img/" + i
    image_files.append(test_sample)

#%%
image_size = 64
nb_classes = len(image_files) # 여기서 왜 다시 nb_classes 설정 해주는 것임?
categories = ["Airplane", "Bicycle", "Bus",
              "Car", "Helicopter", "HotAirBallon",
              "MotorBike", "Ship", "Train", "Truck"]

#%%
X = []
files = []
#이미지 불러오기
for fname in image_files:
    print(fname)
    img = Image.open(fname)
    img = img.convert('RGB')
    img = img.resize((image_size, image_size))
    in_data = np.asarray(img)
    in_data = in_data.astype('float') / 256
    X.append(in_data)
    files.append(fname)

print(X)
print(files)

#%%
X = np.array(X)

# 모델 파일 읽어오기
model = load_model(root_dir + 'transportation_model.h5')

# 예측실행
pre = model.predict(X)

# 예측결과 출력
for i, p in enumerate(pre):
    y = p.argmax()
    print('입력:', files[i])
    print('예측:', "[", y, "]", categories[y], "/score", p[y])


#%%
X = np.array(X)

#모델 파일 읽어오기
model = load_model(root_dir + "koreanfood01_model.h5")

#예측실행
pre = model.predict(X)

#예측 결과 출력
for i, p in enumerate(pre):
    y = p.argmax()
    print('입력:', files[i])
    print('예측:', "[", y, "]", categories[y], "/Score", p[y])

    
#%%








