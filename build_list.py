import os
import os.path as osp
import glob
import random
from pathlib import Path



def build_file_list(src_dir, list_dir):
    """Build file list for source data.
    args:
        src_dir, type=str, help='root directory for the data'
        list_dir, type=str, help='root directory for the data lists'
        filename, the path will be saved in this file. (train_list&val_list&test_list) 
    Returns:
        train_list includes 
            path of the flow in format of exr, 
            corresponding first raw image in format of png,
            and class label of the action.
        the name of actions with respect class label store in another file.
    """
    #dirs = glob.glob(osp.join(src_dir,'*'))
    #dirs = os.listdir(src_dir)
    cls_dict = {}
    idx = 0
    dirs = [d for d in Path(src_dir).iterdir() if d.is_dir()]
    random.shuffle(dirs)
    split = int(len(dirs)*0.8)
    train_dirs = dirs[:split]
    val_dirs = dirs[split:]

    for dir in train_dirs:
        cls_name = osp.basename(dir)
        cls_name = cls_name.split('.')
        cls_name = cls_name[0].split('_')
        cls_name = cls_name[0]
        if cls_name not in cls_dict:
            cls_dict[cls_name] = idx
            with open(osp.join(list_dir, 'classlabel.txt'), 'a') as f:
                f.write(f'{cls_name}: {idx}\n')
            idx += 1
        cls_label = cls_dict[cls_name]
        
        flows_n = len(os.listdir(osp.join(dir,'exr_f')))
        #flows_n = 74
        #imgs_n = len(os.listdir(osp.join(dir, 'png')))
        dir_names = osp.basename(dir)

        #flow_path = osp.join(osp.basename(dir), 'exr_f')
        #img_path = osp.join(osp.basename(dir), 'png')
        #file_list = (img_path,imgs_n,cls_label)
        with open(osp.join(list_dir, 'train_list.txt'), 'a') as f:
            f.writelines(f'{dir_names} {flows_n} {cls_label}\n')

    for dir in val_dirs:
        cls_name = osp.basename(dir)
        cls_name = cls_name.split('.')
        cls_name = cls_name[0].split('_')
        cls_name = cls_name[0]
        if cls_name not in cls_dict:
            cls_dict[cls_name] = idx
            with open(osp.join(list_dir, 'classlabel.txt'), 'a') as f:
                f.write(f'{cls_name}: {idx}\n')
            idx += 1
        cls_label = cls_dict[cls_name]
        
        flows_n = len(os.listdir(osp.join(dir,'exr_f')))
        #imgs_n = len(os.listdir(osp.join(dir, 'png')))
        dir_names = osp.basename(dir)

        #flow_path = osp.join(osp.basename(dir), 'exr_f')
        #img_path = osp.join(osp.basename(dir), 'png')
        #file_list = (img_path,imgs_n,cls_label)
        
        with open(osp.join(list_dir, 'val_list.txt'), 'a') as f:
            f.writelines(f'{dir_names} {flows_n} {cls_label}\n')

if __name__ == '__main__':
    list_dir = "/home/zexin/Documents/my_experiment/"
    src_dir = "/mnt/dst_datasets2/own_omni_dataset/omniflow/"
    build_file_list(src_dir, list_dir)



