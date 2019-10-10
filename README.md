# HorizonNet
My attempt to make a self driving car with deep learning in Forza Horizon 4.
 - developped with Python 3.7
 - works for Windows (FH4 is not on Linux)
 - you need an xbox controller for now

## How to launch
1. To execute just type `python main.py`.
2. It will then capture, every 2 seconds approximately, a new image of the game and the inputs from the controller.
3. The neural network is in development ... :)

## Example of a capture
 - Image file `x_image.png`

![alt text](https://raw.githubusercontent.com/aurelien_m/HorizonNet/master/data/9_image.png)

 - Inputs file `x_inputs.txt` 

Steering: (x: 5188, y: 2591)

Pedals: (gas: 75, brake: 0)
