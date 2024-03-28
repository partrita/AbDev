# AbDev

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>AbDev: Predictive Modeling for Monoclonal Antibody (mAb) Biophysical Properties</h1>
    <p>AbDev is a comprehensive predictive model package designed for the analysis of 12 critical biophysical properties of monoclonal antibodies (mAbs). This tool combines a deep learning-based tool, DeepSP, and machine learning techniques to provide insights based on the variable regions sequences of mAbs.</p>

<h2>Getting Started</h2>
<p>To utilize AbDev effectively, follow the guidelines outlined below:</p>

<h3>Feature Preparation</h3>
<ol>
    <li><strong>Prepare a CSV File:</strong> Begin by preparing a CSV file named "Sequence_Info.csv" using the format provided in this guide as a reference. This file should contain the variable regions sequences of the mAbs you wish to analyze.</li>
</ol>

<h3>Generating Spatial Properties with DeepSP</h3>
<ol start="2">
    <li><strong>Run the DeepSP Notebook:</strong> Use the "DeepSP.ipynb" notebook file to execute DeepSP, a deep learning-based tool developed by our group. DeepSP is designed to generate 30 spatial properties of mAbs based on their sequences.
        <ul>
            <li>Upon completion, you will obtain a "SAPSCM.csv" file, which contains the spatial properties needed for further analysis.</li>
        </ul>
    </li>
</ol>

<h3>Predicting Biophysical Properties with AbDev</h3>
<ol start="3">
    <li><strong>Run the AbDev Notebook:</strong> Next, execute the "AbDev.ipynb" notebook file. This step will process the features generated in the previous step and produce the "Prediction_Result.csv" file. This file includes predictions for 12 biophysical properties of the analyzed mAbs.</li>
</ol>

<h2>Citation</h2>
<ul>
    <li><strong>For DeepSP usage:</strong> The manuscript is currently under review, but it is available on bioRxiv for reference. Please cite accordingly when using DeepSP in your research.
        <br><a href="https://www.biorxiv.org/content/10.1101/2024.02.28.582582v1">Read the DeepSP preprint on bioRxiv</a>
    </li>
    <li><strong>For AbDev usage:</strong> The publication related to AbDev is currently under preparation. More details will be provided upon publication.</li>
</ul>
</body>
</html>
