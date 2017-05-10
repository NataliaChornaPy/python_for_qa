from PIL import Image
import os, sys, time


def path_to_image(path, img_format):
        try:
                jpegs = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(img_format)]
                return jpegs
        except WindowsError, (ErrorNumber, ErrorMessage):
            print time.strftime("%c"),"The path is wrong,- ", ErrorMessage



def BlackWhite_foto (img,jpeg):
        if img.mode <> 'L':
            img.convert('L').save(jpeg)
            print time.strftime("%c"),jpeg, '-- photo is black/white now'
        print img,'hhhhhtttt'
        # return img


def landscape_orient(image):
        width, height = img.size
        if height > width:
            img.rotate(90.0).save(jpeg)
            # img.resize((height, width), Image.ANTIALIAS).save(jpeg)
            print time.strftime("%c"), jpeg, '-- photo is rotated'

if __name__ == "__main__":
    temp = sys.stdout
    sys.stdout = open('log.txt', 'w')
    path = 'C:\Users\Natalia_Chorna\python_for_qa\python_secondary_skill\hw03\photo - Copy'
    # obtain images with specified format
    images = path_to_image(path, 'jpg')
    try:
        for jpeg in images:
            img = Image.open(jpeg)
            print img,'fff'
            BlackWhite_foto(img,jpeg) # convert to black/white
            landscape_orient(img) # rotate
    except TypeError:
        print time.strftime("%c"),"End"
    except IOError:
                print time.strftime("%c"),jpeg,"- Cannot identify image file"
    sys.stdout.close()
    sys.stdout = temp
