# -*- coding: utf-8 -*-  
""" 
* file description 
    - Copyright ⓒ 2021 KCNET, All rights reserved.
    - fileName : ``repository.py``
    - author : ``이서용 (Lee Seo Yong)``
    - date : ``2021-11-11 오후 11:51``
    - comment : `` ``
       
* revision history 
    - 2021-11-11    Lee Seo Yong    최초 작성
"""
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt

from keras.preprocessing.image import ImageDataGenerator

from keras import layers
from keras import models
from keras import optimizers

from api.resource.v1.Img_classify import model


def Model_setting():  # layer, window, activation, shape 모두 객체화 해서 model에 저장

    motion_model = models.Sequential()
    motion_model.add(layers.Conv2D(32, (7, 7), activation='relu', input_shape=(430, 180, 3)))
    motion_model.add(layers.MaxPooling2D((2, 2)))
    motion_model.add(layers.Conv2D(64, (7, 7), activation='relu'))
    motion_model.add(layers.MaxPooling2D((2, 2)))
    motion_model.add(layers.Conv2D(128, (7, 7), activation='relu'))
    motion_model.add(layers.MaxPooling2D((2, 2)))
    motion_model.add(layers.Conv2D(128, (7, 7), activation='relu'))
    motion_model.add(layers.MaxPooling2D((2, 2)))

    motion_model.add(layers.Flatten())
    motion_model.add(layers.Dense(512, activation='relu'))
    motion_model.add(layers.Dense(4, activation='softmax'))

    motion_model.compile(loss='categorical_crossentropy',
                         optimizer=optimizers.SGD(lr=0.005),  # lr=학습률
                         metrics=['acc'])

    print(model.summary)

    return model


########

def Generator_history(model):
    train_datagen = ImageDataGenerator(rescale=1. / 255)
    test_datagen = ImageDataGenerator(rescale=1. / 255)

    # x_train,y_train(훈련이미지, 훈련라벨)

    train_generator = train_datagen.flow_from_directory(
        'C:\\Users\\0614_\\Desktop\\root\\train',
        target_size=(430, 180),
        batch_size=20,
        class_mode='categorical')  # 디렉토리 객체화 해서 config에 추가예정

    # x_test,y_test(검증이미지, 검증라벨)

    validation_generator = test_datagen.flow_from_directory(
        'C:\\Users\\0614_\\Desktop\\root\\test',
        target_size=(430, 180),
        batch_size=20,
        class_mode='categorical')  # 디렉토리 객체화 해서 config에 추가예정

    for data_batch, labels_batch in train_generator:
        print('배치 데이터 크기', data_batch.shape)
        print('배치 레이블 크기', labels_batch.shape)
        break

    history = model.fit_generator(
        train_generator,
        steps_per_epoch=106,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=26)

    return history


############
def model_save(model):  # 모델저장
    model.save('Motion Classify CNN_small_1.h5')
    return


##############

def Model_test_result(history):  # 모델의 테스트 결과 출력
    acc = history.history['acc']
    vall_acc = history.history['val_acc']
    loss = history.history['loss']
    vall_loss = history.history['val_loss']

    epochs = range(1, len(acc) + 1)

    plt.plot(epochs, acc, 'bo', label='Trainging acc')
    plt.plot(epochs, vall_acc, 'b', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()

    plt.figure()

    plt.plot(epochs, loss, 'bo', label='Trainging loss')
    plt.plot(epochs, vall_loss, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()

    plt.show()
    return
