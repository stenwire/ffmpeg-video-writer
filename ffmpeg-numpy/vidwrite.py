import os
import ffmpeg
import numpy as np
from PIL import Image
import numpy as np
import cv2
import glob

img = os.path.join("./images/*.png")
# images = np.asarray(img)
out_put = os.path.join("./results")
# resolution = 0

def create_vid():
    """
    A function that writes images to a numpy array

    Parameters
    ----------
    none
    """
    numpy_list = []
    # img_list = ["1.png", "1.png", "1.png", "1.png"]
    files = glob.glob("*.png")
    for my_file in files:
        print(my_file)
        image = Image.open(my_file).convert('RGB')
        image = np.array(image)
        numpy_list.append(image)

    print('numpy_list shape:', np.array(numpy_list).shape)

    return(numpy_list)

def vidwrite(fn, images, framerate=60, vcodec='libx264'):
    """
    A function that writes a video from a numpy array

    Parameters
    ----------
    fn: path to save video output
        file name
    images: a numpy array
        A numpy array of images
    framerate: int
        output video frame rate
    vcodec: hex
        video codec format

    Usage
    -------
    vidwrite("./results/output.mp4", img)
    """
    if not isinstance(images, np.ndarray):
        images = np.asarray(images)
    n,height,width,channels = images.shape
    process = (
        ffmpeg
            .input('pipe:', format='rawvideo', pix_fmt='rgb24', s='{}x{}'.format(width, height))
            .output(fn, pix_fmt='yuv420p', vcodec=vcodec, r=framerate, format='mp4')
            .overwrite_output()
            .run_async(pipe_stdin=True)
    )
    for frame in images:
        process.stdin.write(
            frame
                .astype(np.uint8)
                .tobytes()
        )
    process.stdin.close()
    process.wait()


if __name__=="__main__":
    img = create_vid()
    vidwrite("./results/output.mp4", img)
