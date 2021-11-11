# -*- coding: utf-8 -*-  
""" 
* file description 
    - Copyright ⓒ 2021 KCNET, All rights reserved.
    - fileName : ``model.py``
    - author : ``이서용 (Lee Seo Yong)``
    - date : ``2021-11-11 오후 11:51``
    - comment : `` ``
       
* revision history 
    - 2021-11-11    Lee Seo Yong    최초 작성
"""
from dataclasses import dataclass

@dataclass
class Model_Setting_value():

    layer = None,
    window = None,
    activation = None,
    shape = None


@dataclass
class data_directory():
    directory = 'C:\\Users\\0614_\\Desktop\\root\\train',
    target_size = (430, 180),
    batch_size = 20,
    class_mode = 'categorical'
