import shutil, os


def movefiles():
     for i in range(0, 750, 5):
          try:
               shutil.move("./image"+str(i)+".jpg", "../videoData/")
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


movefiles()