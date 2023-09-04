import os
import nibabel as nib
import numpy as np
from tqdm import tqdm

path='./new_dataset/trainset/'



for index,i in enumerate(os.listdir(path)):
    data=nib.load(path+i+'/label.nii')
    data=np.asarray(data.get_fdata())
    # data[data==1]=0
    # data[data==2]=0
    # data[data == 3] = 1
    # data[data == 4] = 2
    # data[data == 5] = 3
    print(np.unique(data))
    # img = nib.Nifti1Image(data, np.eye(4))  # 将 nrrd 文件转换为 .nii 文件
    # nib.save(img, path+i+'/label.nii')  # 保存 nii 文件

