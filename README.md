# Compare-and-delete-images
This Python code allows to compare images, compute difference using arbitrary multiple hash sizes, and keep only those with interesting difference. 
Was written to keep only interesting ones to create some Timelapse video.<p>
The problem with some Timelapse is that so many images has nothing of interesting to show. If you can delete similar images you can get a more active and interesting Timelapse video.<p>

Launch with: <p>
python imagepath hashlist --removesimilarimages<p>
imagepath=path and pattern of the file to scan, alphabetically sortable (img-00001.jpg, img-00002.jpg, ...) as in F:/photos/img-*.jpg<p>
hashlist=List of preferred hash size to evaluate image difference (6,8,20,50) NO SPACES ALLOWED  (integer comma separated)<p>
--removesimilarimages=optional parameter to remove (rename) images. With this parameter the program will delete similar images using the first hash size you specified. Please initially use the program wihout this parameter to get a report about the number of image that will kept using different hash sizes. <p><p>

The result will be a list of images with interesting difference to be glued to a Timelapse video via ffmpeg or you preferred video making program
