
import sys
sys.path.append('C:/Users/Ainee/Desktop/Work/MapIR/mapir-main/Modules')

from MapIR.mapir import MapIR
from Band_Correction.correction import band_correction
from Radiance_Calibration.radiance import radiance_calibration
from Radiance_Calibration.radiance import dark_current_subtraction
from Radiance_Calibration.radiance import flat_field_correction
from Reflectance_Calibration.reflectance_calibration import reflectance_calibration
from Analysis.vegetation_index import NDVI
from Data_Paths.data_filepaths import *



def process_single(file, save_directory=''):
    # Create MapIR Object
    image = MapIR(file)
    # image.dial_in()
    # image.display()

    # Dark Current Subtraction
    image = dark_current_subtraction(image)
    #image.display()

    # Band_Correction
    image = band_correction(image)
    #image.display()

    # Flat Field Correction
    image = flat_field_correction(image)
    #image.display()

    # Radiance_Calibration
    image = radiance_calibration(image)
    # image.display()
 
    # Reflectance Calibration
    # image = reflectance_calibration(image)
    # image.display()

    # Georectification
    image.extract_GPS('tiff')
    image.export_tiff(save_directory)
    # image.display()

    # Analysis
    # NDVI(image)


if __name__ == '__main__':

    #process_single(WF_68_81)
    process_single(active_dataset)
