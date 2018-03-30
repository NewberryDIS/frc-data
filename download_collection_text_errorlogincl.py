import internetarchive
import time
import sys

acceptable_file_types = ['djvu.txt','marc.xml','djvu.xml','meta.xml','pdf']

try:
  filetype = sys.argv[1]
  collection = sys.argv[2]
except:
  print '\n'
  print 'Error: this script takes two arguments \n'
  print 'Argument 1 should be an acceptable Internet Archive filetype (acceptable arguments are %s) \n' % ', '.join(acceptable_file_types)
  print 'Argument 2 should be the unique identifier for an Internet Archive collection (i.e. \'newberryfrenchpamphlets\') \n'
  print 'example: python download_collection_text_errorlogincl.py djvu.xml newberryfrenchpamphlets'
  sys.exit(0)
if filetype not in acceptable_file_types:
  print 'Error: %s is not an acceptable filetype parameter, acceptable filetypes are %s' % (filetype, ', '.join(acceptable_file_types))
  sys.exit(0)

if filetype == 'pdf':
  file_ext = '.pdf'
else:
  file_ext = '_' + sys.argv[1]

error_log = open('ia-errors.log', 'a')

search = internetarchive.search_items('collection:%s' % collection)#ia collection name 

for result in search:
    itemid = result['identifier']
    item = internetarchive.get_item(itemid)
    text = item.get_file(itemid + file_ext)#change the file extension here to change the files that are downloaded
    try:
        text.download()
    except Exception as e:
        error_log.write('Could not download '+ itemid + ' because of error: %s\n' % e)
        print ("There was an error; writing to log.")
    else:
                        
        print ("Downloading "+itemid+" ...")#in Python 2 you do not need the parenthesis around the print statements
        time.sleep(1)
