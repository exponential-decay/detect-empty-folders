# detect-empty-folders

Detect empty folders in a DROID CSV through ID heuristic...

##Heuristic Used

* Create CSV list, DROIDLIST

* GRAB 'ALL' PARENT_IDs FROM DROIDLIST

* LOOK FOR UNIQUENESS IN PARENT_ID LIST

* IF FOLDER 'ID' IS NEVER A 'PARENT_ID' IT IS EMPTY

* SIMULATE REMOVAL OF THE FOLDER AND THEREFORE ID FOR THAT FOLDER

* IF WE HAVE JUST ONE EMPTY FOLDER REPEAT TO SEE IF A NEXT FOLDER BECOMES EMPTY

* ETC. RECURSE. 