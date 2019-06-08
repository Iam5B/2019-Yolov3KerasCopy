# Annotate your picture

This is how I annotate pictures when using yolov3.

You can use it to build your training set and testing set.

## Marker

1.	Modify the classes in `./Marker/data/obj.data`.
2.	Modify `./Marker/data/obj.names`.
3.	Clear `./Marker/data/img` and import your images.
4.	Double click `./Marker/yolo_mark.cmd`.
5.	Press 'h' if you meet some problems.

## Transformer

1.	Copy `./Marker/data/train.txt` and `./Marker/data/img`(folder) to `./Transformer`, dont modify train.txt
2.	Run `python transfer.py`
3.	Save your `train.txt`

## Addition
1.	I don't know if you could run `yolo_mark.cmd`, I run it on WIN10 64, if you couldn't run it, then you could try to build this project ☞ [Yolo_mark](https://github.com/AlexeyAB/Yolo_mark)