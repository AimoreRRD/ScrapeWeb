import copy
import os
import random
from shutil import copyfile
from PIL import Image as PILimage

# scraped_folder_list = ["science", "sport", "travel"]
scraped_folder_list = ["art", "film & tv", "finance & retail", "food", "music", "politics", "religion", "science", "sport", "travel"]

for scraped_folder in scraped_folder_list:
    scraped_path = r'D:\ImageRecognition\DataSets\DataSet_Scraped\Google_Images/'

    ### CREATE DATASET from SCRAPED IMAGES
    dataset = []  ### list of all datasets

    rootdir = scraped_path + scraped_folder + '='
    for subdir, dirs, files in os.walk(rootdir):
        for img_file in files:
            dataset.append((os.path.join(subdir, img_file), img_file))
    #         dataset.append(img_file)

    # ### randomize dataset
    random.shuffle(dataset)
    # print(dataset)

    # ### Divide dataset in: TRAIN, VAL and TEST
    dataset_size = len(dataset)

    ### Dataset distribution based only on training and validadtion
    # train_percent = int(0.7 * dataset_size)
    # val_percent = int(0.15 * dataset_size)

    # dataset_dict = {}
    # dataset_dict['train'] = dataset[0:train_percent]
    # dataset_dict['val'] = dataset[train_percent:train_percent + val_percent]
    # dataset_dict['test'] = dataset[train_percent + val_percent:]

    ### Dataset distribution based only on testing and validadtion
    test_percent = int(0.15 * dataset_size)
    val_percent = int(0.15 * dataset_size)

    dataset_dict = {}
    dataset_dict['val'] = dataset[0:val_percent]
    dataset_dict['test'] = dataset[val_percent:(val_percent + test_percent)]
    dataset_dict['train'] = dataset[(val_percent + test_percent):]


    # ### CREATE FOLDERS: TRAIN, VAL and TEST
    set_folders = ['train', 'val', 'test']
    set_path = r'D:\ImageRecognition\DataSets\DataSet_10_classes/'

    ### make directories and put images there:
    for set_id in set_folders:
        dst_path = set_path + set_id + '/' + scraped_folder  ### path

        ### Create directory if doesnt exists
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)

        not_saved = 0
        for img_path, img_name in dataset_dict[set_id]:
            #         print(dst_path + '/' + img_name)
            try:
                ### THIS FILTER HAS TO BE IN THE SCRAPE STEP ### Copy file if the image is readable    ### Make sure that the format of the image is RGB and has 3 channels
                copied_image = PILimage.open(img_path, 'r').convert("RGB")
                copied_image.save(dst_path + '/' + img_name, "JPEG")
                # copyfile(img_path, dst_path + '/' + img_name)
            except:
                print('Could not save image:', img_path)
                os.remove(img_path)  ### Delete Image
                print('Image Deleted = ', img_path)
                not_saved += 1

        print('Number of images that were not saved: %d' % not_saved)
        print('%s | set_id: %s = %d' % (scraped_folder, set_id, len(dataset_dict[set_id])))
    print('\nFROM: ', rootdir)
    print('TO: ', set_path)