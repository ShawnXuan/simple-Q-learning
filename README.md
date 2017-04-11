# A simple Q-learning Implementation

Q-learning([wiki](https://en.wikipedia.org/wiki/Q-learning)) is a model-free reinforcement learning technique. The post "[A Painless Q-learning Tutorial](http://blog.csdn.net/pi9nc/article/details/27649323)" provides a clear description and detail steps which give me inspiration to implement it. 
_note: the original address of the post is expired, I choose a reposted one instead. _

To be more general, I use following algorithm to update Q table. 
![enter image description here](https://wikimedia.org/api/rest_v1/media/math/render/svg/7a2a11876f4a2bef1198beb780a769cfa5c21af3)
In the original post, learning rate is 1 as default.
