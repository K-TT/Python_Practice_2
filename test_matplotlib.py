Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x=np.linspace(0,7,20)
>>> y=np.linspace(0,9,20)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x7fc5d863c2e0>]
>>> plt.show()
>>> plt.plot(x,y, 'o')
[<matplotlib.lines.Line2D object at 0x7fc5d8fa8ee0>]
>>> plt.show()
>>> plt.plot(x+1,y+1, '_')
[<matplotlib.lines.Line2D object at 0x7fc5d8353f70>]
>>> plt.show()
>>> import math
>>> plt.plot(x, np.sin(x))
[<matplotlib.lines.Line2D object at 0x7fc5d83cf130>]
>>> plt.show()
>>> 
