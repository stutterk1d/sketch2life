# Pix2Pix Image Transformation Project

## Overview
This project utilizes the Pix2Pix Generative Adversarial Network (GAN) for transforming sketches into realistic images. The core of the project is a Jupyter notebook that demonstrates the training and usage of the Pix2Pix model, accompanied by a Flask web application for interacting with the model through a web interface.

## Features
- **Model Training**: Detailed explanation and execution of training the Pix2Pix model on a custom dataset.
- **Image Transformation**: Processes for transforming input images using the trained model.
- **Web Application**: A Flask app that allows users to upload sketches and receive transformed images.

## Getting Started

### Prerequisites
- Python 3.x
- TensorFlow 2.x
- Flask
- PIL (Pillow)
- NumPy
- Matplotlib

### Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/yourgithubusername/pix2pix-project.git
cd pix2pix-project
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Running the Notebook
To explore the Pix2Pix model training and image transformation process, open the Jupyter notebook:
```bash
jupyter notebook pix2pix_notebook.ipynb
```

### Running the Web Application
To start the Flask web application locally:
```bash
python app.py
```
Navigate to `http://localhost:5000` in your web browser to interact with the application.

## Usage
- **For Model Training and Testing**: Refer to the `pix2pix_notebook.ipynb` for step-by-step instructions on training the model and transforming images.
- **For the Web Application**: Upload a sketch image through the web interface, and the application will display the transformed image.

## Deployment on Google Cloud (Historical)
This project was previously hosted on Google Cloud, demonstrating a scalable deployment method. Although it's currently not hosted due to cost considerations, you can find the deployment configurations and instructions in the `deployment/` directory for historical reference and future deployments.

## Contributing
Contributions to improve the project are welcome. Please follow the standard fork-and-pull request workflow.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The TensorFlow team for providing the Pix2Pix model implementation.
- The Quick, Draw! Dataset for sketch data.
