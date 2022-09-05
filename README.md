# Compare-and-delete-images
This Python code allows to compare images, compute difference using arbitrary multiple hash sizes, and keep only those with interesting difference. 
Was written to keep only interesting ones doing some Timelapse video.

Launch with: 
python imagepath hashlist --removesimilarimages<p>
imagepath=path and pattern of the file to scan, alphabetically sortable (img-00001.jpg, img-00002.jpg, ...) as in F:/photos/img-*.jpg
hashlist=List of preferred hash size to evaluate image difference (6,8,20,50) NO SPACES ALLOWED  (integer comma separated)
--removesimilarimages=optional parameter to remove (rename) images. With this parameter the program will delete similar images using the first hash size you specified

The result will be a list of images with interesting difference to be glued to a Timelapse video via ffmpeg or you preferred video making program
