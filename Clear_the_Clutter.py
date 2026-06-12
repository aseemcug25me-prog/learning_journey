import os
files = os.listdir("Cluttered Folder")
i = 1
for file in files:
    if file.endswith('.png'):
        os.rename(f"Cluttered Folder/{file}", f"Cluttered Folder/{i}.png")
        i = i + 1
j = 1
for file in files:
    if file.endswith('.pdf'):
        os.rename(f"Cluttered Folder/{file}", f"Cluttered Folder/{j}.pdf")
        j = j + 1