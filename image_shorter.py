import os
import shutil
import pandas as pd

# test_folder = 'DrowsinessDetection/test'
# train_folder = 'DrowsinessDetection/train'
valid_folder = 'DrowsinessDetection/valid'
csv_file = valid_folder+'/_classes.csv'

total_files = [f for f in os.listdir('DrowsinessDetection/valid/image') if os.path.isfile(os.path.join("DrowsinessDetection/valid/image", f))]
print(f'Total Gambar: {len(total_files)}')

df = pd.read_csv(csv_file)
print(df.columns)

for index, row, in df.iterrows():
    file_name = row['filename']
    closed_eye = row[' closed_eye']
    open_eye = row[' open_eye']

    src_path = os.path.join(valid_folder, 'image', file_name)
    
    if closed_eye == 1:
        dst_path = os.path.join(valid_folder, 'close')
    else:
        dst_path = os.path.join(valid_folder, 'open')

    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)
    else:
        print(f"File {src_path} not found")

close_files = [f for f in os.listdir('DrowsinessDetection/valid/close') if os.path.isfile(os.path.join("DrowsinessDetection/valid/close", f))]
print(f'Total Gambar Close : {len(close_files)}')

open_files = [f for f in os.listdir('DrowsinessDetection/valid/open') if os.path.isfile(os.path.join("DrowsinessDetection/valid/open", f))]
print(f'Total Gambar Open : {len(open_files)}')

print('Pemindahan Selesai')


