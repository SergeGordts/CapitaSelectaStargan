Research Topic

• Applying StarGAN to FFHQ Data: A Comparative Study with Original StarGAN Results
on Facial Attribute Transformations

Research Aim

• The aim of this research is to investigate the effectiveness of the StarGAN model in
generating attribute-based transformations on new, high-quality datasets.
Specifically, the study applies StarGAN trained on CelebA (128x128 resolution) to images from the
Flickr-Faces-HQ (FFHQ) dataset and evaluates the model’s ability to generate two specific
transformations.
This research will compare the results of these transformations to those reported in the original StarGAN study to assess model
generalizability and performance on diverse data sources.

Data: 

• Full CelebA dataset  
• FFHQ dataset (128*128)  

Methodological Approach

• Model Selection: The pre-trained StarGAN model
(on dataset CelebA) as provided by the original authorsis is limited to transformations on 5 default attributes.
To overcome this we train the model on the full CelebA dataset for all 40 attributes.

• Data Preparation: sample images from the FFHQ dataset to
match the input size and format expected by the model (128x128 resolution, normalized).

• Apply transformations targeting 2 attributes to the FFHQ data. 

• Generation Process:
For each image, use StarGAN to generate two variants: a single task transformation for each attribute, and a multi-task transformation for both attributes.

• Qualitative Evaluation is performed.

• Quantitative Evaluation Classifier: Use a pre-trained classifier (VG-
GFace2, OpenFace, ...) to measure the presence and accuracy of the at-
tribute in transformed images. 
Metrics: Calculate metrics such as classification accu-
racy to quantify how well the generated images reflect the intended attributes.

• Comparison and Analysis:
Compare the FFHQ transformation results to those from the
original StarGAN study on CelebA to assess differences in attribute representation,
realism, and model generalizability.

Since the FFHQ dataset exceeds the file size of Github (100MB) it is stored locally from
https://drive.google.com/open?id=1tg-Ur7d4vk1T8Bn0pPpUSQPxlPGBlGfv.
The trained model also exceeds the file size of Github (100MB) so it is stored locally.

Resources

. Data: Full CelebA dataset & FFHQ dataset
. Trained Model of StarGAN on CelebA dataset.
. NNabla (Neural Network Libraries) - deep learning framework developed by Sony.
