cmake_minimum_required(VERSION 3.0.2) # KOREKSI: Update ke CMake versi lebih modern
project(onboard_detector)

# KOREKSI: Tambahkan kebijakan CMake modern untuk konsistensi
cmake_policy(SET CMP0048 NEW)
cmake_policy(SET CMP0067 NEW)
cmake_policy(SET CMP0054 NEW)

## Compile as C++14, supported in ROS Noetic
set(CMAKE_CXX_STANDARD 14) # KOREKSI: Set standar C++ ke C++14
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF) # Memaksa kepatuhan ketat terhadap standar C++ yang ditentukan
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall") # KOREKSI: Pindahkan ke sini

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  cv_bridge
  message_filters
  image_transport
  vision_msgs
  # KOREKSI: Tambahkan dependensi lain yang mungkin diperlukan secara tidak langsung
  sensor_msgs
  geometry_msgs
  nav_msgs
  tf
  eigen_conversions
  pcl_ros
  pcl_conversions
)

find_package(PCL 1.7 REQUIRED) # KOREKSI: PCL 1.7 digunakan di sini, tetapi C++14 mungkin masih diperlukan
find_package(Eigen3 REQUIRED) # KOREKSI: Tambahkan pencarian Eigen3 jika digunakan


###################################
## catkin specific configuration ##
###################################
catkin_package(
   INCLUDE_DIRS include
   LIBRARIES onboard_detector
   CATKIN_DEPENDS
     roscpp
     rospy
     std_msgs
     cv_bridge
     message_filters
     image_transport
     vision_msgs
     # KOREKSI: Tambahkan dependensi yang relevan dari find_package
     sensor_msgs
     geometry_msgs
     nav_msgs
     tf
     eigen_conversions
     pcl_ros
     pcl_conversions
   # KOREKSI PENTING: Hapus baris 'DEPENDS system_lib' karena tidak didefinisikan
)

###########
## Build ##
###########

include_directories(
  include
  SYSTEM
  ${catkin_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}
  ${Eigen3_INCLUDE_DIR} # KOREKSI: Tambahkan Eigen3 include dir
)

add_library(${PROJECT_NAME}
   include/${PROJECT_NAME}/dynamicDetector.cpp
   include/${PROJECT_NAME}/uvDetector.cpp
   include/${PROJECT_NAME}/dbscan.cpp
   include/${PROJECT_NAME}/kalmanFilter.cpp
   include/${PROJECT_NAME}/fakeDetector.cpp
)
target_compile_features(${PROJECT_NAME} PUBLIC cxx_std_14) # KOREKSI: Terapkan C++14

add_executable(detector_node src/detector_node.cpp)
target_compile_features(detector_node PUBLIC cxx_std_14) # KOREKSI: Terapkan C++14

add_executable(fake_detector_node src/fake_detector_node.cpp)
target_compile_features(fake_detector_node PUBLIC cxx_std_14) # KOREKSI: Terapkan C++14


target_link_libraries(${PROJECT_NAME}
  ${catkin_LIBRARIES}
  ${PCL_LIBRARIES}
  ${Eigen3_LIBRARIES} # KOREKSI: Tautkan Eigen3
)
target_link_libraries(detector_node ${PROJECT_NAME})
target_link_libraries(fake_detector_node ${PROJECT_NAME})