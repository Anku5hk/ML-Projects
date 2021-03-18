# Welcome to ML-Projects
Goal: Build cool Deep Learning, Computer Vision, NLP applications/tutorials while maintaining code readability. 

## Image Processing
* [Image filtering](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Image_filtering.ipynb): To  blur, add/remove nosie, sharpen image.
* [Edge detection](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Edge_detection.ipynb): Gradient Operators, Laplacian of Gaussian, Canny Edge Detection.
* [Corner Detection](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Corner_Detection.ipynb): Harris, Shi-Tomasi, FAST Corner Detection.
* [Keypoints detection and matching](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Keypoints_detection_and_matching.ipynb): Using ORB to detect keypoints and descriptors, then match with other images.
* [Image Pyramid And Reconstructing Image](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Image_Pyramid_And_Reconstructing_Image.ipynb): Gaussian, Laplacian Pyramid and Image reconstruction.
* [Optical flow demo notebook[Extra]](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Optical_flow_demo.ipynb): Little demo.
* [Optical flow](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/optical_flow.py): Find flow of particular object. 
* [Dense flow](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Dense_flow.py): Find global motion, process is to track all pixels to estimate motion.
* [Bag of visual words](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Bag_of_visual_words.ipynb): Make BOVW features to train an image classifier on.

## Face Applications
* [Face & Facial landmarks Detection](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Face%20Recognition/Face_Detection_methods.ipynb): Using Haarcascades, Face Detection library, dlib.
* [Face recognition using dimension reduction](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Face%20Recognition/Face_recognition_pca.ipynb): Make features using PCA/LDA which are dimension reduction algorithms and then use a classifier on top to classify the face.
* [Face_recognition using deep learning](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Face%20Recognition/Face_recognition_deep_learning.ipynb): A more modern and prefered way using deep learning library for faces called Face Detection library.
* [Extract faces[Extra]](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/extract_faces.py): Extract faces from a folder just by running this .py file into the folder containing images using Haarcascades.

## Computer Vision
* [Environment Sound Classification](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Some_deep_learning/Environmental_Sound_Classification_PT.ipynb): Using spectorgrams as features to train image classifier.
* Image Classification:
  1. [Image Classfication using BOVW](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Image%20processing/Image_Classfication_using_BOWV.ipynb): Use Bag Of Visual Words(BOVW) features to classify images using SVM.
  2. [Image Classification using HOG](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Some_deep_learning/Image_Classification_Using_HOG%2BSVM.ipynb): Use Histogram Of Gradients Features to classify images using SVM.
  3. [Using Deep learning + Clean pipeline](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Pytroch_GPU_Pipeline.ipynb): Using resnet18 to classify flowers, also a clean pytorch training pipeline.
* Object Detection:
  1. [Object Detection Using HOG(part 1)](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Vehicle_Detector_Using_HOG.ipynb): Train car/non-car using HOG featues and SVM classifier.
  2. [Object Detection Using HOG(part 2)](https://github.com/Anku5hk/ML-Projects/blob/master/Vehicle_Detection/Vehicle_Detector_Using_HOG_2.ipynb): Create object detector with sliding window approach.
  3. [Object Detection Using Faster R-CNN(part 1 optional)](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Some_deep_learning/Train_Feature_extractor.ipynb): Train a resnet18 car/non-car classifier.
  4. [Object Detection Using Faster R-CNN(part 2)](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Train_Object_Detector.ipynb): Train Faster-RCNN object detector with resnet car classifier as backbone.
* Image Segmentation:
  1. [Semantic Segmentation Using U-Net](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Some_deep_learning/Semantic_Segmentaion_Using_U_Net.ipynb): Semantic Segmentation using U-Nets on Oxford-Pets dataset.
* Auto-Encoders:
  1. [Image denoising using AutoEncoders](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Some_deep_learning/Auto_encoders_with_Pytroch.ipynb): Image reconstruction and image denoising using autoencoders.
  2. [Image coloring using AutoEncoders(RGB image)](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Image_coloring_with_auto_encoders_RGB.ipynb): Image colorization using cnn autoencoders.
  3. [Image coloring using AutoEncoders(LAB image)](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Image_coloring_with_auto_encoders_LAB.ipynb): Image colorization using cnn autoencoders.
* Image Translation:
  1. [Unpaired Image-Image Translation](https://github.com/Anku5hk/The_ML_Workflow/blob/master/Some_deep_learning/Image_Image_Translation_using_CycleGans.ipynb): Unpaired Image-Image translation using CycleGans.

## Pytorch Bag Of Tricks
* [Knowledge Distillation pytorch](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Knowledge_Distillation_pytorch.ipynb): Train Teacher model, then train Student model with same or smaller model size. Also Improves generalization.
* [Stochastic Weight Averaging pytorch](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/SWA_pytorch.ipynb): Improve generalization by Weight Averaging after training, by training for ~25% more with SWA. 
* [Gradient accumulation pytorch](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Gradient_Accumulation_pytorch.ipynb): Update weights with bigger batch size, by updating weights after some number of iteration.
* [Automatic Precision Training pytorch](https://github.com/Anku5hk/ML-Projects/blob/master/Some_deep_learning/Automatic_Precision_Training_pytorch.ipynb): Fit a bigger batch, improve training speed using Automatic Precision(Mixed Precision Training), basically doing multiplications with fp16 and addition with fp32.

## Kaggle Solutions
* [Petals to the Metal: FLower Classification on TPU](https://github.com/Anku5hk/The_ML_Workflow/tree/master/Kaggle%20competitions%20solutions/Petals%20to%20the%20Metal_%20Flower%20Classification%20on%20TPU): Image classification using effnets on TPU with Tensorflow.
* [Wheat Detection](https://github.com/Anku5hk/The_ML_Workflow/tree/master/Kaggle%20competitions%20solutions/Wheat%20Detection): Object detection using efficient-det and faster-rcnn with Pytorch.

##
