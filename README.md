# centuriazione
## downloader.py
The current example downloads a tiff image, 1500 X 1500 px and 1.5km X 1.5 km.
top_left and bottom_right coordinates and zoom are chosen accordingly.


## splitarea.py
Downloads n images that cover a square area from top_left origin with distance as edge length. It splits the area in images which cover 1.5km X 1.5 km.
The division in tiles of the images sometimes use 7 or 8 tiles per edge. It means that images are not always 1500 px X 1500 px.

## splitimage.py
It dowloads one image that covers a square area from top_left origin with distance as edge length.
It splits the image in tiles 1500 X 1500 px using the imagemagik linux program.
On the borders some tiles can be not 1500 X 1500 px.
>
>
>
>
# Google-Map-Downloader
![Google-Map-Downloader](https://geospatialmedia.s3.amazonaws.com/wp-content/uploads/2016/07/google-earth.jpg)
## 中文：  
[downloader_1.1](https://github.com/zhengjie9510/Google-Map-Downloader/blob/master/downloader_1.1.py)：  
    一个小工具，你只需要输入空间范围、地图缩放等级就可以实现Google地图的下载，并输出为TIFF格式，含空间坐标系。  
[downloader_1.2](https://github.com/zhengjie9510/Google-Map-Downloader/blob/master/downloader_1.2.py)：  
    是在1.1版本上的改进。由于python的多线程中存在GIL锁，导致python的多线程不能利用多核，考虑到现在的计算机是多核的，为了充分利用计算机的多核资源，提高下载速度，尝试利用多进程+多线程的方式来实现地图切片下载，最终速度得到极大提高。但该部分还没有实现进度条功能。  
## English:  
[downloader_1.1](https://github.com/zhengjie9510/Google-Map-Downloader/blob/master/downloader_1.1.py):  
    A small tool, you only need to input the spatial extent and map zoom level to download Google Maps, and output to TIFF format, including the spatial coordinate system.  
[downloader_1.2](https://github.com/zhengjie9510/Google-Map-Downloader/blob/master/downloader_1.2.py):  
    It is an improvement on version 1.1. Due to the existence of GIL locks in python's multi-threading, python's multi-threading cannot use multi-cores. Considering that computers are now multi-core, In order to make full use of the computer's multi-core resources and increase the download speed, try to use multi-process + multi-threaded way to achieve map tile download. The final speed has been greatly improved, but this part has not implemented the progress bar function.
## 指南/Guide
### 安装/Install
```python
conda install --yes --file requirements.txt
```
### 使用/Use
```python
if __name__ == '__main__':
    start_time=time.time()
    
    # main(100.361,38.866,100.386,38.839,13,r'C:\Users\test.tif')
    main(left,top,right,bottom,zoom,filePath,style='s',server="Google")

    end_time=time.time()
    print('lasted a total of {:.2f} seconds'.format(end_time-start_time))
```
```python
'''
Parameters
----------
left, top : left-top coordinate, for example (100.361,38.866)
    
right, bottom : right-bottom coordinate
    
z : zoom

filePath : File path for storing results, TIFF format
    
style : 
    m for map; 
    s for satellite; 
    y for satellite with label; 
    t for terrain; 
    p for terrain with label; 
    h for label;

source : Google China (default) or Google
'''
```
## 问题/Issues
If you encounter the problem of Bad network link, you can change the HEADERS in the download function, and try again.
```python
def download(self,url):
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36'}
        header = ur.Request(url,headers=HEADERS)
        err=0
        while(err<3):
            try:
                data = ur.urlopen(header).read()
            except:
                err+=1
            else:
                return data
        raise Exception("Bad network link.")
```
