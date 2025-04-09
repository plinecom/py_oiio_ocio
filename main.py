import OpenImageIO as oiio
import glob
import os

if __name__ == '__main__':

    # 対象のディレクトリを指定

    for path in glob.glob('C:/EXR/ACES2065_1/*.exr'):
        new_folder = os.path.dirname(path) + '/ACEScg'
        os.makedirs(new_folder, exist_ok=True)
        new_path = new_folder +'/'+ os.path.basename(path)

        print(new_path)

        #Read File
        buf = oiio.ImageBuf(path)

        #Convert ColorSpace
        dst = oiio.ImageBufAlgo.colorconvert( buf, "ACES2065-1", "ACEScg",
                                      colorconfig='studio-config-v2.2.0_aces-v1.3_ocio-v2.4.ocio')

        #Write File
        dst.write(new_path)
