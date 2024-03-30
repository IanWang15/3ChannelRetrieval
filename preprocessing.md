There are nine channels available from SAGE III/ISS L2 data, but not all of them should be included in the model training process. Several channels may exhibit very high correlations, making it unnecessary to use both of them.

The initial step in constructing a machine learning (ML) model involves preprocessing the data to generate a training dataset, a process also known as feature selection. For this task, I utilized the scikit-learn library (https://scikit-learn.org/stable/modules/feature_selection.html).

Below are some key points extracted from my study notes on the user guide provided by the website:

1.13.1 Removing features with low variance:

This function helps identify any features that may be deemed meaningless. It evaluates whether certain features exhibit very low variations on their own.


