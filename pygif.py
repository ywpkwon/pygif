import argparse
import imageio
import os

def makegif(inf, fps):

    # Load each file into a list
    frames = []
    for root, dirs, filenames in os.walk(inf):
      for filename in filenames:
        if any([ext in filename.lower() for ext in [".png", ".jpg"]]):
            print(filename)
            frames.append(imageio.imread(os.path.join(inf,filename)))

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