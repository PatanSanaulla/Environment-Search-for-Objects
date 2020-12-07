import shutil, os


def movefiles():
     for i in range(1, 3460, 15):
          try:
               shutil.move("../Dataset_1/700_5/image"+str(i)+".jpg", "../evironmentDataset/Test/")
          except:
               continue
          print(i)


def renameAllFiles():
     for count, filename in enumerate(os.listdir("../evironmentDataset/Train/")):
          dst = "trainData" + str(count) + ".jpg"
          src = '../evironmentDataset/Train/' + filename
          dst = '../evironmentDataset/Train/' + dst

          # rename() function will
          # rename all the files
          os.rename(src, dst)


renameAllFiles()