# Intelligent_hair_analysis_system
This project is based on paper "Lee, S.-H & Yang, C.-S. (2018). An intelligent hair and scalp analysis system using camera sensors and Norwood-Hamilton model. International Journal of Innovative Computing, Information and Control. 14. 503-518."

1. ABSTRACT  
...This paper proposes the concep of using webcam and microsope camera sensors to extract characteristic images to evaluate the hair and scalp tatus of the user. Through the Norwood-Hamilton scale model and detection of scalp surface status, actual information is provided to the users to understand their own physical status.

2. Proposed Methods  
In the pre-processing stage of baldness detection, the clothes or background environment included in the input images will generate noise. To reduce the disturbances, the boundary of the image is cropped through the user interface of the system. Then the Otsu threshold value [24] is used to obtain the binary image, and K-means clustering
[25] is performed twice for this binary image. In the detection stage, the baldness status is contrasted according to the Norwood-Hamilton scale model, and the three most possible situations are output. A voting mechanism is adopted against the three situations to obtain the results.

![methods](https://user-images.githubusercontent.com/54901021/77377575-d4ce8080-6db6-11ea-801a-3ce0f778b0f1.PNG)

3.1. Preprocessing.   
The clothes of the users and background environment in the images
extracted by the webcam will affect the accuracy of the judgment. Therefore, in Step 1,
the boundary of the target image is cropped by a user-friendly interface operation provided
by the system, and then the Otsu threshold value is used to obtain the binary image. Kmeans clustering is conducted twice for this binary image with K values of four and two,
as shown in Figure 2. We use the K value of four to separate the background environment
and hair. Owing to the influence of light condition, the K value of four has the good
performance to classify this situation. Again, we do the K-means clustering by setting
the K value of two. We would like to get the non-hair and hair result. We expected
the outcome of the second step could remove noise more clearly to increase the diagnosis
efficiency. In some situations, it is unnecessary to perform the K-means clustering twice;
it is only required to divide the binary images into two groups.  
3.2. Detection of baldness status.   
According to the Norwood-Hamilton scale model
shown in Figure 3, the baldness status is divided into seven and four phases, including
M type, U type, O type, and syndrome type. According to the Norwood-Hamilton scale
model, the 7-phase baldness model images become the contrastive sample images after
binarization, as shown in Figure 4. After the hair images of the subject are extracted
by the webcam camera sensors and pre-processed, they are compared with the sample
images. This study adopted the simple calculation method of mean square error (MSE),
as expressed in Equation (1) for the contrast calculation between the detected hair images
and sample images. In Equation (1), W and H are denoted as the width and height of
image respectively, Imageij is the pixel (i, j) of input image, and P
k
ij is the pixel (i, j) of
the kth sample image. Therefore, a 4 × 7 matrix can be acquired, as shown in Figure 5.
