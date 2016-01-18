import sys
from droidcsvhandlerclass import *

#Create CSV list, DROIDLIST
#GRAB 'ALL' PARENT_IDs FROM DROIDLIST
#LOOK FOR UNIQUENESS IN PARENT_ID LIST
#IF FOLDER 'ID' IS NEVER A 'PARENT_ID' IT IS EMPTY
#SIMULATE REMOVAL OF THE FOLDER AND THEREFORE ID FOR THAT FOLDER
#IF WE HAVE JUST ONE EMPTY FOLDER REPEAT TO SEE IF A NEXT FOLDER BECOMES EMPTY
#ETC. RECURSE.

class DetectEmpties:
   #Consider merging into DROIDCSVHANDLER class...

   emptylist = []
   blacklist = False

   #simulate deletion of file structure...
   def recurse_delete(self, droidlist, folderIDlist):
      empties = False

      #if folder does not appear in PARENT_ID list it is empty
      parentIDs = []
      for row in droidlist:
         parentIDs.append(row['PARENT_ID'])

      uniqueIDs = set(parentIDs)
      for id in folderIDlist:
         if id not in uniqueIDs:
            for row in list(droidlist):
               if row['ID'] == id:
                  empties = True
                  self.emptylist.append(row['FILE_PATH'])
                  droidlist.remove(row)   #remove empty folder
                  for folderid in list(folderIDlist):
                     if row['ID'] == folderid:
                        folderIDlist.remove(folderid)
                        
      if empties == True:
         self.recurse_delete(droidlist, folderIDlist)

   def removeblacklistitems(self, droidlist, folderIDlist, pathblacklist, puidblacklist, zerobytefiles):
      if pathblacklist:
         sys.stderr.write("Note: Using file path blacklists.\n")
         for file in pathblacklist:
            for item in list(droidlist):
               if item['FILE_PATH'] == file:
                  droidlist.remove(item)
                  break
      if puidblacklist:
         sys.stderr.write("Note: Using puid blacklists.\n")
         for puid in puidblacklist:
            for item in list(droidlist):
               if item['PUID'] == puid and item['METHOD'] == 'Signature' or item['METHOD'] == 'Container':
                  droidlist.remove(item)
      if zerobytefiles:
         sys.stderr.write("Note: Using zero byte file blacklists.\n")
         for item in list(droidlist):
            if item['SIZE'] == '0':
               droidlist.remove(item)

   def createFolderList(self, droidlist):
      folderIDlist = []
      for row in droidlist:
         if row['TYPE'] == 'Folder':
            folderIDlist.append(row['ID'])
      return folderIDlist
      
   #primary function, create a full list from DROID CSV
   #create a list of IDs belonging to just folders...
   def detectEmpties(self, csv, pathblacklist=False, puidblacklist=False, zerobytefiles=False):
      droidcsv = droidCSVHandler()
      droidlist = droidcsv.readDROIDCSV(csv)
      folderIDlist = self.createFolderList(droidlist)
      
      if pathblacklist or puidblacklist or zerobytefiles:
         self.blacklist = True
         self.removeblacklistitems(droidlist, folderIDlist, pathblacklist, puidblacklist, zerobytefiles)
      
      self.recurse_delete(droidlist, folderIDlist)
      self.outputEmptyList()

   def outputEmptyList(self):
      outputtext = " or its siblings contains zero FILE-objects." + "\n"
      if self.blacklist:
         outputtext = " or its siblings contains or will contain no FILE-objects once blacklist destructions have been implemented." + "\n"
      if len(self.emptylist) > 0:
         for file in self.emptylist:
            sys.stdout.write(file + outputtext) 
      else:
         sys.stderr.write("There are no empty folders." + "\n")