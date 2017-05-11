from PIL import Image
import os, sys, time


def path_to_images(path, img_format):
        try:
            jpegs = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(img_format)]
            return jpegs
        except Exception:
            print time.strftime("%c"),"The path is wrong,- "


def BlackWhite_foto (img, img_path):
            if img.mode <> 'L':
                converted = img.convert('L')
                converted.save(img_path)
                print time.strftime("%c"), img_path,'-- photo is black/white now'
                return converted
            else:
                return img


def landscape_orient(image,image_path):
        width, height = image.size
        if height > width:
            image.rotate(90.0).save(image_path)
            # img.resize((height, width), Image.ANTIALIAS).save(jpeg)
            print time.strftime("%c"), image_path, '-- photo is rotated'

def main():
    path_to_folder = raw_input('Path to the folder:')
    temp = sys.stdout
    sys.stdout = open('log.txt', 'w')
    # path = 'C:\Users\Natalia_Chorna\python_for_qa\python_secondary_skill\hw03\photo - Copy'
    paths_of_images = path_to_images(path_to_folder, 'jpg')
    try:
        for image_path in paths_of_images:
            img = Image.open(image_path)
            black_image = BlackWhite_foto(img, image_path)  # convert to black/white
            landscape_orient(black_image, image_path)  # rotate
    except TypeError:
        print time.strftime("%c"), "End"
    except IOError:
        print time.strftime("%c"),"- Cannot identify image file"
    else:
        print "Exception"
    sys.stdout.close()
    sys.stdout = temp


if __name__ == "__main__":
    main()