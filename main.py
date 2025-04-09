import OpenImageIO as oiio
import glob
import os

if __name__ == '__main__':

    for path in glob.glob('C:/EXR/ACES2065_1/*.exr'):

        output_folder = os.path.join(os.path.dirname(path) , 'ACEScg')
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, os.path.basename(path))

        print(output_path)

        #Read File
        buf = oiio.ImageBuf(path)

        #Convert ColorSpace
        dst = oiio.ImageBufAlgo.colorconvert( buf, "ACES2065-1", "ACEScg",
                                      colorconfig='studio-config-v2.2.0_aces-v1.3_ocio-v2.4.ocio')

        #Write File
        dst.write(output_path)
