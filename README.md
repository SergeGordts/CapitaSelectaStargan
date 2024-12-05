Research Topic

Applying StarGAN to FFHQ Data: A Comparative Study with Original StarGAN Results
on Facial Attribute Transformations

Research Aim

The aim of this research is to investigate the effectiveness of the StarGAN model in
generating attribute-based transformations on new, high-quality datasets.
Specifically, the study applies StarGAN trained on CelebA (128x128 resolution) to images from the
Flickr-Faces-HQ (FFHQ) dataset and evaluates the model’s ability to generate two specific
transformations: Smiling and Blond Hair.
This research will compare the results of these transformations to those reported in the original StarGAN study to assess model
generalizability and performance on diverse data sources.

Methodological Approach

• Model Selection and Data Preparation Model: Using the pre-trained StarGAN model
(CelebA, 128x128 resolution) as provided by the original authors, trained on CelebA
for facial attribute transformations. Data: Sample images from the FFHQ dataset to
match the input size and format expected by the model (128x128 resolution, normalized).

Since the FFHQ dataset exceeds the file size of Github (100MB) it is stored locally from
https://drive.google.com/open?id=1tg-Ur7d4vk1T8Bn0pPpUSQPxlPGBlGfv.

• Attribute Transformation Application Attributes: Apply transformations targeting
2 attributes to the FFHQ data. Generation Process:
For each image, use StarGAN to generate two variants: one for each attriibute transformation.
Since we use the pretrained Stargan model (downloaded via the notebook) the following attributes are
available: Black_Hair, Blond_Hair, Brown_Hair, Male, Young.

The pretrained model exceeds the file size of Github (100MB) so it is stored locally.

• Quantitative Evaluation Classifier: Use a pre-trained facial expression classifier (VG-
GFace2, OpenFace, ...) to measure the presence and accuracy of the "Smiling" at-
tribute in transformed images. Metrics: Calculate metrics such as classification accu-
racy to quantify how well the generated images reflect the intended attributes.

• Comparison and Analysis Compare the FFHQ transformation results to those from the
original StarGAN study on CelebA to assess differences in attribute representation,
realism, and model generalizability.

Resources

• Datasets: FFHQ: High-resolution images from the Flickr-Faces-HQ (FFHQ) dataset,
sampled at 128x128 resolution.
• Pre-trained Models: StarGAN: Pre-trained model trained on CelebA (128x128), from
the original StarGAN implementation. Facial Expression Classifier: A pre-trained
model for facial expression classification, such as those available from open repositories
or transfer learning on the CelebA-HQ or AffectNet datasets.
