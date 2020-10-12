
DataPath = 'MC2-Image-Data/'

import os
import process_data

if __name__ == '__main__':
    
    with os.scandir(DataPath) as entries:
        for entry in entries:
            if entry.name == 'TrainingImages':
                continue
            print(entry.name)