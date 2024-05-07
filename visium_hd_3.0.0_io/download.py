#!/usr/bin/env python3
##
import os
import subprocess
from pathlib import Path

import sys

sys.path.insert(1, os.path.join(sys.path[0], Path(__file__).parent.parent.resolve()))

from utils import download, unzip

##

# from https://www.10xgenomics.com/datasets/visium-hd-cytassist-gene-expression-libraries-of-mouse-intestine
# Visium HD Spatial Gene Expression Library, Mouse Small Intestine (FFPE)

urls = [
    "https://cf.10xgenomics.com/samples/spatial-exp/3.0.0/Visium_HD_Mouse_Small_Intestine/Visium_HD_Mouse_Small_Intestine_tissue_image.btf",
    "https://cf.10xgenomics.com/samples/spatial-exp/3.0.0/Visium_HD_Mouse_Small_Intestine/Visium_HD_Mouse_Small_Intestine_cloupe_008um.cloupe",
    "https://cf.10xgenomics.com/samples/spatial-exp/3.0.0/Visium_HD_Mouse_Small_Intestine/Visium_HD_Mouse_Small_Intestine_feature_slice.h5",
    "https://cf.10xgenomics.com/samples/spatial-exp/3.0.0/Visium_HD_Mouse_Small_Intestine/Visium_HD_Mouse_Small_Intestine_spatial.tar.gz",
    "https://cf.10xgenomics.com/samples/spatial-exp/3.0.0/Visium_HD_Mouse_Small_Intestine/Visium_HD_Mouse_Small_Intestine_square_002um_binned_outputs.tar.gz",
    "https://cf.10xgenomics.com/samples/spatial-exp/3.0.0/Visium_HD_Mouse_Small_Intestine/Visium_HD_Mouse_Small_Intestine_square_008um_binned_outputs.tar.gz",
    "https://cf.10xgenomics.com/samples/spatial-exp/3.0.0/Visium_HD_Mouse_Small_Intestine/Visium_HD_Mouse_Small_Intestine_square_016um_binned_outputs.tar.gz",
]

##
os.makedirs("data", exist_ok=True)
for url in urls:
    print(url)
    name = Path(url).name
    download(url, os.path.join("data", name), name)

files = [
    "Visium_HD_Mouse_Small_Intestine_spatial.tar.gz",
    "Visium_HD_Mouse_Small_Intestine_square_002um_binned_outputs.tar.gz",
    "Visium_HD_Mouse_Small_Intestine_square_008um_binned_outputs.tar.gz",
    "Visium_HD_Mouse_Small_Intestine_square_016um_binned_outputs.tar.gz",
]
for file in files:
    subprocess.run(f"tar -xzf data/{file} -C data", shell=True, check=True)
    subprocess.run(f"rm data/{file}", shell=True, check=True)
