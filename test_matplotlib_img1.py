Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> image=np.random.rand(30,30)
>>> plt.imshow(image)
<matplotlib.image.AxesImage object at 0x7feaf847ab50>
>>> plt.show()
>>> plt.imshow(image, cmap=plt.cm.Accent)
<matplotlib.image.AxesImage object at 0x7feaf91680d0>
>>> plt.show()
plt.imshow(image, cmap=plt.cm.hot)
>>> plt.show()
>>> plt.imshow(image, cmap=plt.cm.hot)
<matplotlib.image.AxesImage object at 0x7feaf924ea60>
>>> plt.show()
>>> plt.imshow(image, cmap=plt.cm.Pastell)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    plt.imshow(image, cmap=plt.cm.Pastell)
AttributeError: module 'matplotlib.cm' has no attribute 'Pastell'
>>> plt.imshow(image, cmap=plt.cm.Pastel)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    plt.imshow(image, cmap=plt.cm.Pastel)
AttributeError: module 'matplotlib.cm' has no attribute 'Pastel'
>>> plt.imshow(image, cmap=plt.cm.Pastel1)
<matplotlib.image.AxesImage object at 0x7feaf94566a0>
>>> plt.show()
>>> plt.colorbar()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    plt.colorbar()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/pyplot.py", line 2352, in colorbar
    raise RuntimeError('No mappable was found to use for colorbar '
RuntimeError: No mappable was found to use for colorbar creation. First define a mappable such as an image (with imshow) or a contour set (with contourf).
>>> plt.imshow(image, cmap=plt.cm.Pastel1)
<matplotlib.image.AxesImage object at 0x7feafaf58fa0>
>>> plt.colorbar()
<matplotlib.colorbar.Colorbar object at 0x7feafaf7e490>
>>> plt.show()
>>> 