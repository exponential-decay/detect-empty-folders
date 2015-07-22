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
   puidblacklist = False
   pathblacklist = False
   zerobytefiles = False

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

   def registerblacklists(self, pathblacklist, puidblacklist, zerobytefiles):
      if pathblacklist != False:
         self.pathblacklist = pathblacklist.split(',')
      if puidblacklist != False:
         self.puidblacklist = puidblacklist.split(',')
      if zerobytefiles:
         self.zerobytefiles = True

   #primary function, create a full list from DROID CSV
   #create a list of IDs belonging to just folders...
   def detectEmpties(self, csv, pathblacklist, puidblacklist, zerobytefiles):
      droidcsv = droidCSVHandler()
      droidlist = droidcsv.readDROIDCSV(csv)
      folderIDlist = []
      for row in droidlist:
         if row['TYPE'] == 'Folder':
            folderIDlist.append(row['ID'])
      
      self.registerblacklists(pathblacklist, puidblacklist, zerobytefiles)
      self.recurse_delete(droidlist, folderIDlist)
      self.outputEmptyList()

   def outputEmptyList(self):
      for file in self.emptylist:
         sys.stdout.write(file + " or its siblings contains zero FILE objects.\n") 