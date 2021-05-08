ml_project
==============================



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw      <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── entities       <- configuration ORM entities
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── feature_builder.py
    │   │   └── nope_transformer.py
    │   │   └── outlier_transformer.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   └── model_trainer.py
    │   │
    │   ├── pipelines   <- Main application pipelines 
    │   │   └── predict_pipeline.py
    │   │   └── train_pipeline.py
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │   │   └── eda_report.py
    │   │   └── report.txt
    │   └── utils.py     <- top-level application utilities
    │
    └── tests     <- unit & intagration tests


--------

Model Training
------------


    python train_pipeline.py train=random_forest


