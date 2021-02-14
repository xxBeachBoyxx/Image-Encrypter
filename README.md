# Image-Encrypter

In the Image Encrypter folder only the brain.py and the decryp.py files are related to the projects the others are rough files.

# How it works
Open the brain.py file and type a 8 word message separated by spaces.
Which can be increased but for simplicity and non-redundancy of code I kept it to 8.
The key for the images is stored in a json file.
It creates a image final.png which is taken by the decryp.py file and the images are splited and according to the key that is stored in the json file the message is restored and displayed.
The key has important stuff, the idea is the collage of images would not seem very suspicious to anyone it can be uploaded to a website as design of as a image in a ppt and many more things like this can be done.
# Unless someone has the key, there is no possible way(I think so) that the message can decrypted(Also each image represents a word and not a letter making it exceptionally hard, I don't think frequency analysis would help(Please don't prove me wrong, just don't))
