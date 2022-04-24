import os
import os.path as osp
import glob

def class_mapping():
    src_dir = '/mnt/dst_datasets2/own_omni_dataset/omniflow/'
    dir_names = os.listdir(src_dir)
    cls_dict = {}
    idx = 0
    for dir in dir_names:
        cls = dir.split('.')
        cls = cls[0].split('_')
        cls = cls[0]
        if cls not in cls_dict:
            cls_dict[cls] = idx
            idx += 1
    print(cls_dict)
       
if __name__ == '__main__':
    class_mapping()




