import cv2
import os
import moviepy.editor as mp
import PIL
import time
import pyperclip as pc
from pynput.keyboard import Key, Controller
from keyboard import press
import mouse
from pyautogui import *
keyboardd = Controller()


# HI change these to you mouse positon to where you paste in the data
x = 1143
y = 142
#################





def convert():
    # set vid to the video you want to convert  add .mp4 after(has to be in downloads)
    vid = ".mp4"



    clip = mp.VideoFileClip("C:\\Users\\tatea\\Downloads\\"+ vid)
    clip_resized = clip.resize( (22,22) )
    clip_resized.write_videofile("nw.mp4")
    vid = cv2.VideoCapture("nw.mp4")

    try:

        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0

    while (True):

        # reading from frame
        success, frame = vid.read()

        if success:
            # continue creating images until video remains
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    vid.release()
    cv2.destroyAllWindows()


#####

def main(new_width=22):
            current = 0
            dir = "C:\\Users\\tatea\PycharmProjects\\asciirecroom\\data"
            ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
            print("pee")
            time.sleep(3)

            poop = 0
            two = 1
        #while True:
            current = 0
            cur = str(current)

            def resize_image(image, new_width=22):
                width, height = image.size
                ratio = height / width
                new_height = int(new_width * ratio)
                resized_image = image.resize((new_width, new_height))
                return (resized_image)

                # convert each pixel to grayscale

            def grayify(image):
                grayscale_image = image.convert("L")
                return (grayscale_image)

                # convert pixels to a string of ascii characters

            def pixels_to_ascii(image):
                pixels = image.getdata()
                characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
                return (characters)



            app = len(os.listdir(dir))
            for images in os.listdir(dir):




                    c = str(current)

                    # attempt to open image from user-input
                    image = PIL.Image.open(str("C:\\Users\\tatea\PycharmProjects\\asciirecroom\\data\\frame"+ c +".jpg"))

                    # convert image to ascii
                    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

                    # format
                    pixel_count = len(new_image_data)
                    join = "".join(
                        [new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])
                    ascii_image = join


                    res = ' '.join(ascii_image[i:i + 22] for i in range(0, len(ascii_image), 22))
                    #print(res)
                    if current ==64:
                        exit()
                    if two == 1:
                        pc.copy(res)
                        mouse.click('left')
                        time.sleep(0.4)
                        mouse.move(x, y, absolute=True, duration=0)

                        mouse.click('left')

                        time.sleep(0.3)
                        keyboardd.press(Key.ctrl.value)
                        keyboardd.press('v')
                        keyboardd.release('v')
                        keyboardd.release(Key.ctrl.value)

                        time.sleep(0.1)
                        press('enter')
                        keyDown('esc')
                        keyUp('esc')
                        time.sleep(0.2)
                        mouse.click('right')


                    if poop == 1:
                        pc.copy(res)
                        mouse.move(x, y, absolute=True, duration=0)
                        mouse.click("left")
                        time.sleep(0.1)
                        keyboardd.press(Key.ctrl.value)
                        keyboardd.press('v')
                        keyboardd.release('v')
                        keyboardd.release(Key.ctrl.value)
                        press('enter')

                        print(current)
                        current += 1

                        with open("ascii_image.txt", "w") as f:
                            f.write(res)

                    print(current , "out of" , app)
                    current += 1

                    time.sleep(0.5)







input = input("1 convet / 2 print:")
if input == "2":
    main()
if input == "1":
    convert()



