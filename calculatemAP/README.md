# mAP (mean Average Precision)

This folder is a copy of [https://github.com/Cartucho/mAP](https://github.com/Cartucho/mAP), you can use it by yourself

Here I offer some tools to help generate the input data, then you could use the data and the mAP tool to generate your results.

## Quick-start

1.	Move `yolo.py` and `yolo_video.py` to parent directory (back-up in advance). 
2.	Modify some of the content in `yolo.py` and `yolo_video.py` like the directories if you have modified before.
3.	Run `python yolo_video.py --image` and input your testlist, which has the same format with `train.txt` mentioned in `train.py`, then you would get an output file, which contains all of the boxes your network predicted.
4.	Move your testlist and outputlist to current directory
5.	Remove all of the files in `./input/detection-results` and `./input/ground-truth`	
6.	Run `python traintxt2groundtruth.py` and `python outputtxt2detectionresults.py` to generate data in certain format (the results are located in ./input/...).
7.	If you want to see the animation, you can add the pictures into `./input/images-optional`, or you would have to delete that folder.
8.	Run `python main.py`.

## Addition
1.	Only supports `.jpg` picture, if you want to change, just look at `traintxt2groundtruth.py` and `outputtxt2detectionresults.py`
2.	If you not set, your class name would be 0,1,2,3,..., their definition is also in `traintxt2groundtruth.py` and `outputtxt2detectionresults.py`