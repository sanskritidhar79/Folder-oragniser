import os
files = os.listdir()
files.remove("main.py")

def create(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

create('IMAGES')
create('DOCUMENTS')
create('MEDIA')
create('OTHERS')

imgsExtensions =['.png','.jpg','jpeg']
docsExtensions=['.doc','.docx','.txt','.pdf','.csv','.xls']
mediaExtensions =['.mp3' ,'.mp4']

images = [i for i in files if os.path.splitext(i)[1].lower() in imgsExtensions ]
documents = [i for i in files if os.path.splitext(i)[1].lower() in docsExtensions]
media=[i for i in files if os.path.splitext(i)[1].lower() in mediaExtensions ]
all_extensions=[imgsExtensions,docsExtensions,mediaExtensions]


others=[]
flatten_all_ext=[]

for sub_extension in all_extensions:
    for val in sub_extension:
        flatten_all_ext.append(val)

for i in files:
    ext = os.path.splitext(i)[1].lower() 
    if ext not in flatten_all_ext and os.path.isfile(i):
        others.append(i)
  
def move_to_folder(folderName , files):
    for i in files:
        os.replace(i,f"{folderName}/{i}")

move_to_folder('IMAGES',images)
move_to_folder('DOCUMENTS',documents)
move_to_folder('MEDIA',media)
move_to_folder('OTHERS',others)