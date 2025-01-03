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
>Sample images from the FFHQ dataset are prepared (label files are generated by the MobilenetV2 classifier) for single and multi transformation by the pretrained Stargan model.
Single and multi transformation by the pretrained Stargan model are applied.  
The code is in the directory data preparation (mobilenetv2 needs tensorflow, see environment.yaml)
>
• MobileNetV2 Classifier Training: 
>A trained and finetuned MobileNetV2 classifier on the CelebA dataset to predict five specific attributes from the CelebA dataset is created.
>The objective is to use this classifier to assess the effectiveness of attribute-based transformations applied by StarGAN.  
The code is in the directory Classifier
>
• Single and Multi-Transformation on CelebA
>Single and multi transformation by the pretrained Stargan model on a CelebA dataset are applied.  
The code is in the directory StarGan_single_multi_transformations  

• Evaluation Metrics
  >• Accuracy metric is calculated to quantify how well the generated images (for images from CelebA and FFHQ) reflect the intended attributes.  
  >• Qualitative Analysis: a random selected set of transformed images are visually inspected to assess realism, identity preservation, and unintended changes. 
     Images and transformed images are shown side by side with a slider (0-10) to choose score of inspection.
  The code is in the directory metrics.

**Resources**  
>• Data: FFHQ dataset & CelebA dataset   
>• Pretrained model of StarGAN on CelebA dataset   
>• MobilenetV2: https://github.com/d-li14/mobilenetv2.pytorch   
