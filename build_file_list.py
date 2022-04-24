import os
import os.path as osp
import glob



def build_file_list(src_dir, list_dir, filename):
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
    dirs = glob.glob(osp.join(src_dir,'*'))
    #dirs = os.listdir(src_dir)
    cls_dict = {}
    idx = 0
    for dir in dirs:
        if '.txt' in dir:
            continue
        cls_name = osp.basename(dir)
        cls_name = cls_name.split('.')
        cls_name = cls_name[0].split('_')
        cls_name = cls_name[0]
        if cls_name not in cls_dict:
            cls_dict[cls_name] = idx
            idx += 1
        cls_label = cls_dict[cls_name]
        flows = sorted(os.listdir(osp.join(dir,'exr_f')))
        imgs = sorted(os.listdir(osp.join(dir, 'png')))
        for flow, img in zip(flows, imgs):
            flow_path = osp.join(osp.basename(dir), 'exr_f', flow)
            img_path = osp.join(osp.basename(dir), 'png', img)
            file_list = (flow_path, img_path, cls_name)
            with open(osp.join(list_dir, filename), 'a') as f:
                f.writelines(f'{flow_path}, {img_path}, {cls_name}, {cls_label}\n')


if __name__ == '__main__':
    list_dir = "/home/zexin/Documents/my_experiment/"
    src_dir = "/mnt/dst_datasets2/own_omni_dataset/omniflow/"
    filename = 'train_list2.txt'
    build_file_list(src_dir, list_dir, filename)



