# Hindi to ISL Animation

A college project that converts Hindi text to Indian Sign Language (ISL) animations.

##  Overview

This project is a third-year college initiative designed to bridge the communication gap by translating Hindi text into Indian Sign Language (ISL) animations.

## Features

- **Hindi to ISL Translation** - Converts Hindi text input to Indian Sign Language
- **Animation Generation** - Creates visual animations representing ISL signs
- **Web-based Interface** - User-friendly website for easy access and translation
- **Multi-language Support** - Built-in machine translation capabilities

## Installation & Setup

###  Steps

. **Clone the repository**
   ```bash
   git clone https://github.com/avanitank15/Hindi-to-ISL-animation-.git
   cd Hindi-to-ISL-animation-
   ```

. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

. **Download the translation model**
   
   Download the M2M100 model from Hugging Face:
   - **Model URL**: https://huggingface.co/jncraton/m2m100_1.2B-ct2-int8
   - **Installation Path**: Place the model inside the `hemant/m2m100_ct2_12b/` directory

. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Project Structure

```
Hindi-to-ISL-animation-/
├── README.md
├── requirements.txt
├── app.py
├── hemant/
│   └── m2m100_ct2_12b/          # Translation model directory
├── templates/                     # Web templates
├── static/                        # CSS, JS, animations
└── pages ├── home.py                     
          ├── about.py         
          ├── form.py   
          ├── form.db                            
          └── main.py                     
```

## Configuration

Ensure the model path is correctly configured in your application settings:

```
Model Location: hemant/m2m100_ct2_12b/
```
## Tech Stack

- **Language**: Python
- **Machine Translation**: M2M100 (Meta's Many-to-Many Multilingual Model)
- **Model Size**: M2M100 1.2B CT2 INT8 
- **Frontend**: Web-based interface


## Issues

If you encounter any issues:
- Check that the model is correctly placed in `hemant/m2m100_ct2_12b/`
- Verify all dependencies are installed
- Ensure Python 3.8+ is installed

---

**Last Updated**: April 8, 2026  
**Repository**: https://github.com/avanitank15/Hindi-to-ISL-animation-