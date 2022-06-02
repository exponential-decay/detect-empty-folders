# detect-empty-folders

Detect empty folders in a DROID CSV through ID heuristic...

## Heuristic for spotting empty folders

* Create CSV list, DROIDLIST
* GRAB 'ALL' PARENT_IDs FROM DROIDLIST
* LOOK FOR UNIQUENESS IN PARENT_ID LIST
* IF FOLDER 'ID' IS NEVER A 'PARENT_ID' IT IS EMPTY
* SIMULATE REMOVAL/DELETION OF THE FOLDER AND THE 'ID' FOR THAT FOLDER
* IF WE FIND EVEN ONE EMPTY FOLDER, REPEAT TO SEE IF A NEXT FOLDER BECOMES EMPTY - RECURSE

## Using Denylists

A denylist allows you to simulate the deletion of non-record objects. Deletion of these objects may render a folder thusly empty. In this case, it supports reporting where it is necessary to record all deletions from a collection.

The heuristic doesn't change. Denylist items are removed from the DROIDLIST first. Folders are then checked using the
method above.

Denylists currently allow:

* Listing PUIDs - these will only be removed if matched using Signature or Container identification
* Listing File Paths - a useful way to override Signature or Container identification for alt. file types
* Deletion of zero byte objects - operating on the 'SIZE' column in the DROID CSV output

The config file might look like follows:

    [denylist]

    #e.g. False or C:\Documents and Settings\spencero\Desktop\test-empty-folders\folder-becomes-empty-one-file\thumbs.db
    filepaths=False

    #e.g. False or fmt/682
    puids=False

    #e.g. False or True
    zerobytefiles=False
    
Use of the config file is not yet bullet-proof, and so expect undefined results if it isn't correctly used. 

#### N.b. The heuristics used here can be implemented in any language using the DROID CSV. This is my first implementation. It happens to be Python.
