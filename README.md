## Titanic Dataset

This project uses the [Titanic training dataset from Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset?select=Titanic-Dataset.csv) after extrapolation to 1M dataset size.

Download the dataset and place it in the `data/` directory before running the agent.

---

## Running the Agent

You can run the agent in two different modes:

### 1. **GPU-Accelerated Mode** (NVIDIA cuML + cuDF)
Leverages NVIDIA's RAPIDS libraries for faster data processing and model training.

python -m cudf.pandas -m cuml.accel run.py


---

### 2. **CPU Mode** (scikit-learn + pandas)
Uses standard pandas and scikit-learn for data processing and modeling.

python run.py


---

**Note:**  
- Ensure you have the appropriate dependencies installed for each mode.  
- GPU mode requires a supported NVIDIA GPU and the RAPIDS ecosystem installed.
