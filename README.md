# ORB_SLAM2-Python-Jetbot

## Part I: ORB-SLAM for Python 3.6 Setup
Clone the repositories into same folder.

### Pangulin
https://github.com/stevenlovegrove/Pangolin
- Dependency
```
sudo apt install libgl1-mesa-dev
sudo apt install libglew-dev
sudo apt install cmake
sudo apt-get install libxkbcommon-x11-dev
```
- Build
```
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build
cd build
cmake ..
cmake --build .
```

### ORB-SLAM2
sudo apt-get install libeigen3-dev
sudo apt install libwayland-dev
https://github.com/raulmur/ORB_SLAM2
1. add ```#include <unistd.h>``` into ```Include/System.h```.
2. Patch the repository (see Python Binding).
5. Build project 
```
chmod +x build.sh
./build.sh
```
6. Python binding requires ```sudo make install```.

### Python Binding
https://github.com/jskinn/ORB_SLAM2-PythonBindings
1. Patch the orb-slam repository.
```
git apply ../ORB_SLAM2-PythonBindings/orbslam-changes.diff
```
2. Build ORB-SLAM2 (see ORB-SLAM2).
3. Modify the python version from 3.5 to 3.6 in "CMakeLists.txt"
```
31 find_package(PythonLibs 3.5 REQUIRED) -> 3.6
33 find_package(Boost 1.45.0 REQUIRED COMPONENTS python-py35) -> 36
72 install(TARGETS ${TARGET_MODULE_NAME} DESTINATION lib/python3.5/dist-packages) -> 3.6
```
4. Some Dependency.
```
sudo apt-get install libboost-all-dev
```
5. Build project.
```
mkdir build
cd build
cmake ..
make
make install
```

6. Test the python import
```
python3
>>> import orbslam2 
```

### Test on TUM Dataset
#### TUM Datasets 
https://vision.in.tum.de/data/datasets/rgbd-dataset/download

Recommand Sequence 'freiburg3_long_office_household'
https://vision.in.tum.de/rgbd/dataset/freiburg3/rgbd_dataset_freiburg3_long_office_household.tgz

#### Run Code
1. Copy ```ORB_SLAM2-PythonBindings/txamples/orbslam_mono_tum.py``` to ```ORB-SLAM2/```
2. Make folder ```Datasets/``` and extract the dataset into it.
3. Run orb-slam
```
python3 orbslam_mono_tum.py Vocabulary/ORBvoc.txt Examples/Monocular/TUM3.yaml Datasets/rgbd_dataset_freiburg3_long_office_household
```

## Part II: Camera Calibration & Jetbot SLAM Live Demo
### Collect Data
### Search Chessboard
### Calibration
### Extract Camera Config
### Record Dataset

### Some Problem
- restart camera
```
sudo systemctl restart nvargus-daemon
```
- Failed to load module “canberra-gtk-module”
```
sudo apt-get install libcanberra-gtk-module
```

### Opencv Calibration Tutorial
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html

### Matplotlib
- FreeType
http://www.linuxfromscratch.org/blfs/view/svn/general/freetype2.html
./configure
sudo make  install
- LibPng
sudo apt-get install -y libpng-dev

### Plotly
1. Install python plotly library
```
pip3 install plotly
```
2. Install jupyter extension and rebuild jupyter.
```
sudo jupyter labextension install @jupyterlab/plotly-extension
jupyter lab build
```
3. Restart your jetbot.