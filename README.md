# Open CV Face Detection

This is a simple face detection code snippet written in python and making use of the Haar feature-based cascade pre-trained classifiers. The Haar Cascade classifiers can be found on Open CV github repo here      https://github.com/opencv/opencv/tree/master/data/haarcascades

### A Screenshot

![Screenshot](https://github.com/ItsCosmas/face_detector/blob/master/detected.JPG) <br />

### To Run This Code

I personally used Pipenv to manage my env workflow.
Its a wonderful virtual env manager read about it here https://pipenv.readthedocs.io.
It can be installed easy via pip
```sh
$ pip install pipenv
```
Then navigate to the project directory to run it .
```sh
$ cd face_detector
$ pipenv shell
$ pipenv install
$ python face_detector.py
```

You can also: 
  - Use your own Photograph for face detection
  -         # Use your own Photo for detection
            # Change this path to your img path
            img = cv2.imread(r"cozy.jpg")
            
  - Make Some tweaks on your code to improve face detection by playing around with the scaleFactor
  -         # Play around with the scaleFactor below
            faces = face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.125,
                                    minNeighbors=5)         
That's it.
The OpenCV docs contains other great examples and tutorials on the haar cascade find them here https://docs.opencv.org/3.4.3/d7/d8b/tutorial_py_face_detection.html.
