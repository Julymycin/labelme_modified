import os

folder = './'

# os.system('conda activate labelme')

names = os.listdir(folder)
for name in names:
    if name.endswith('.json'):
        os.system('labelme_json_to_dataset ' + os.path.join(folder,name) + ' -o ' + folder)
