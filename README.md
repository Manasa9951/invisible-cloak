# Invisible-Cloak
> It’s the cloak which Harry Potter uses to become invisible. Of course, we all know that an invisibility cloak is not real — it’s all **__graphics trickery__**.

> Well, it turns out that you can create this magical experience using an image processing technique called **__color detection and segmentation__**. And the good news is, you don’t need to be part of Hogwarts for that! All you need is a red colored cloth.

<img src="https://imgur.com/rPWfhz1.jpg">

[Click here for Video Demo](https://youtu.be/IhpFZ5t9tD0)

## Requirements
- python 3
- opencv library
- numpy library
- Red cloth (which will serve as a cloak)

## Installation of libraries (can be skipped if done)
- Installation of Open CV and numpy

``pip install opencv-python``

## Code
The basic idea is given below:
1. Capture and store the background frame.
2. Detect the red colored cloth using color detection algorithm.
3. Segment out the red colored cloth by generating a mask.
4. Generate the final augmented output to create the magical effect.

- [background.py](./background.py)
    It is used for extracting the static background frame. We will replace the current frame pixels corresponding to the cloth with the background pixels to generate the effect of an invisibility cloak. For this we need to store the frame of a static background.

- [invisible_cloak.py](./invisible_cloak.py)
    Invisible_cloak file records the main window and works with the image saved by ``background.py`` for making the invisible cloak.

## Reference Links
- https://youtu.be/EGMHG0bv-CE
- https://learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv/

