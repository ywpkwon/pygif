import argparse
import imageio
import os
import glob

def makegif(inf, fps):

    # sorted image file names
    valid_ext = ["jpg","gif","png","tga"]
    filenames = []
    for ext in valid_ext:
        filenames += glob.glob(os.path.join(inf, '*.'+ext))
    filenames.sort()

    # Load each file into a list
    frames = [] 
    for filename in filenames:
        print(filename)
        frames.append(imageio.imread(filename))

    # Save them as frames into a gif
    exportname = "output.gif"
    kargs = { 'duration': 1.0/fps }
    imageio.mimsave(exportname, frames, 'GIF', **kargs)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='lets make gif!')
    parser.add_argument("--inf", required=True, action="store", help="input folder path")
    parser.add_argument("--fps", default=2.0, type=float, help="frames per second")
    args = vars(parser.parse_args())
    makegif(args['inf'], args['fps'])