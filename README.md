**Research Topic**

• Applying StarGAN to FFHQ Data: A Comparative Study with Original StarGAN Results
on Facial Attribute Transformations

**Research Aim**

• The aim of this research is to investigate the effectiveness of the StarGAN model in
generating attribute-based transformations on new, high-quality datasets.
Specifically, the study applies StarGAN trained on CelebA (128x128 resolution) to images from the
Flickr-Faces-HQ (FFHQ) dataset and evaluates the model’s ability to generate two specific
transformations.
This research will compare the results of these transformations to assess model
generalizability and performance on diverse data sources.

**Methodological Approach**

• Data Preparation:  
>Sample images from the FFHQ dataset matched to the input size and format expected by the pretrained Stargan model (128x128 resolution, normalized).  
>Images from the CelebA dataset for training and finetuning of the MobilenetV2 classifier.  

• MobileNetV2 Classifier Training: 
>A trained and finetuned MobileNetV2 classifier on the CelebA dataset to predict five specific attributes from the CelebA dataset.   
The objective is to use this classifier to assess the effectiveness of attribute-based transformations applied by StarGAN.

• Single and Multi-Transformation on CelebA
>The focus is on the evaluation of single and multi-attribute transformations applied to the CelebA dataset, using a trained MobileNetV2 classifier to measure the effectiveness of these transformations.   
We assess the performance of the pretrained StarGAN model in generating transformations on the CelebA dataset, which can be used as a baseline for comparisons with StarGAN's ability to perform similar transformations on the Flickr-Faces-HQ (FFHQ) dataset.

• Generalizability Test on FFHQ
>Similar to CelebA, single and multi-transformations are applied to the FFHQ images using StarGAN.The MobileNetV2 classifier evaluates the transformed images' accuracy in achieving the target attributes.   
Results are compared against the CelebA transformations to determine how well StarGAN generalizes to new, higher-quality data.

• Evaluation Metrics
  >• Classifier-Based Accuracy: Calculate metrics such as classification accuracy to quantify how well the generated images reflect the intended attributes.  
  >• Precision and Recall  
  >• F1 score  
  >• Comparative Analysis: Accuracy results from CelebA and FFHQ are compared to highlight performance differences and generalizability.  
  >• Qualitative Analysis: a random selected set of transformed images are visually inspected to assess realism, identity preservation, and unintended changes.  
  
**Resources**  
>• Data: FFHQ dataset & CelebA dataset   
>• Pretrained model of StarGAN on CelebA dataset   
>• MobilenetV2: https://github.com/d-li14/mobilenetv2.pytorch   
