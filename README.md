# Hindi to ISL Animation 🎬

A college project that converts Hindi text to Indian Sign Language (ISL) animations.

##  Overview

This project is a third-year college initiative designed to bridge the communication gap by translating Hindi text into Indian Sign Language (ISL) animations. The system leverages machine translation and animation technologies to create accessible content for the deaf and hard-of-hearing community.

## Features

- **Hindi to ISL Translation** - Converts Hindi text input to Indian Sign Language
- **Animation Generation** - Creates visual animations representing ISL signs
- **Web-based Interface** - User-friendly website for easy access and translation
- **Multi-language Support** - Built-in machine translation capabilities

## 🛠️ Tech Stack

- **Language**: Python
- **Machine Translation**: M2M100 (Meta's Many-to-Many Multilingual Model)
- **Model Size**: M2M100 1.2B CT2 INT8 
- **Frontend**: Web-based interface

## Installation & Setup

###  Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

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

##  Usage

1. Enter Hindi text in the input field
2. Click "Translate to ISL"
3. View the generated ISL animation
4. Save or share the animation as needed

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

## License

This project is a college assignment. See the repository for more details.


## Issues

If you encounter any issues:
- Check that the model is correctly placed in `hemant/m2m100_ct2_12b/`
- Verify all dependencies are installed
- Ensure Python 3.8+ is installed

##  Future Enhancements

- [ ] Support for more Indian languages
- [ ] Improved animation quality and realism
- [ ] Mobile app version
- [ ] Real-time translation
- [ ] User feedback and testing with ISL community

## Acknowledgments

- Meta AI for the M2M100 translation model
- The ISL and deaf community for guidance and feedback

---

**Last Updated**: April 8, 2026  
**Repository**: https://github.com/avanitank15/Hindi-to-ISL-animation-