**Research Topic**

• Applying StarGAN to FFHQ Data: A Comparative Study with Original StarGAN Results
on Facial Attribute Transformations

**Research Aim**

• The aim of this research is to investigate the effectiveness of the StarGAN model in
generating attribute-based transformations on new, high-quality datasets.
Specifically, the study applies StarGAN trained on CelebA (128x128 resolution) to images from the
Flickr-Faces-HQ (FFHQ) dataset and evaluates the model’s ability to generate two specific
transformations.
This research will compare the results of these transformations to those reported in the original StarGAN study to assess model
generalizability and performance on diverse data sources.

**Methodological Approach**

• Model Selection: The pre-trained StarGAN model
(on dataset CelebA) as provided by the original authorsis is limited to transformations on 5 default attributes.

• Data Preparation: sample images from the FFHQ dataset matched to the input size and format expected by the model (128x128 resolution, normalized).

• Apply transformations targeting 2 attributes to the FFHQ data.  
For each sampled image, use trained StarGAN to generate two variants: a single task transformation for each attribute, and a multi-task transformation for both attributes.

• Qualitative evaluation is performed (on sight)

• Quantitative evaluation Classifier: Using a small classifier like EfficientNet-Lite of MobileNet V2 to measure the presence and accuracy of the attribute in transformed images. 
This classifier is trained on a part of the CelebA dataset.
Metrics: Calculate metrics such as classification accuracy to quantify how well the generated images reflect the intended attributes.
Baseline is the classifier metrics on the stargan (single and multi-task) transformations.

• Comparison and Analysis:
Compare the FFHQ transformation results to those from the original StarGAN study on CelebA to assess differences in attribute representation, realism, and model generalizability.

Since the FFHQ dataset exceeds the file size of Github (100MB) it is stored locally from
https://drive.google.com/open?id=1tg-Ur7d4vk1T8Bn0pPpUSQPxlPGBlGfv.

**Resources**

. Data: FFHQ dataset
. Pretrained model of StarGAN on CelebA dataset.
. NNabla (Neural Network Libraries) - deep learning framework developed by Sony.
. https://github.com/RangiLyu/EfficientNet-Lite or https://github.com/d-li14/mobilenetv2.pytorch
