# MIS - Management Information System Dashboard POC

### This repository contains the Proof of Concept (POC) Dashboard for a Management Information System (MIS). The dashboard provides visualizations and analytics to support decision-making and monitor key performance indicators (KPIs) within an organization.

## Functionality

Currently, the functionality of the dashboard is limited to the Financials page, which displays processed 2018 MIS data. However, in the future, we plan to incorporate additional pages to display key KPIs in other areas like Supply and Team. This expansion will provide a more comprehensive view of the organization's performance across different areas.

## How to run MIS POC Dashboard

To run the application, you need to have Python 3.8 or above installed. Follow these steps:

1. Clone the repository 

2. Create a virtual environment  
```bash
conda create venv
```

3. Install the required packages using the command 
```bash
pip install -r requirements.txt
```

4. Activate the virtual environment using the command
```bash
conda activate venv/
```

5. Run the command 
```bash
streamlit run dashboard/app.py 
```

## Challenges


During the exploratory data analysis of the MIS reports for 2018, several challenges were encountered in cleaning and formatting the data for further analysis. The data had to undergo various cleaning steps to ensure it was in the correct format.

The preprocessing steps involved in preparing the data for analysis included the following:

* Dropping unwanted columns and null values: Columns that were not relevant to the analysis or contained missing values were removed from the dataset.
* Transposing the data frame: The data frame was transposed to transform key KPIs into column headers and months into rows, facilitating easier analysis.
* Creating a month variable: A new variable was created to represent the month for each data entry, allowing for temporal analysis.

* One specific challenge encountered was the presence of repeating months due to target month data. To address this, the target month data was dropped from the analysis as it represented the target for that specific month rather than true values of the variables. However, in future analyses, instead of dropping this data, it can be utilized for comparative analysis to measure the target achieved for a given month. This would provide valuable insights into performance and progress over time.

## Future Scope

In the future scope of the project, we can enhance the data preprocessing and dashboard functionalities as follows:

* Data Preprocessing Automation: Currently, the data preprocessing is performed in Jupyter notebooks for the convenience of data exploration. However, a future enhancement would involve creating data pipelines that automate the preprocessing of MIS excel sheets. This would streamline the data cleaning and formatting process, making it more efficient and scalable.

* Real-time Alerts: As part of the dashboard's advanced features, we can implement a mechanism to trigger alerts when key KPIs, such as the burn rate, experience significant changes beyond a specified threshold. These alerts would provide timely notifications to stakeholders, enabling them to proactively address any emerging issues or opportunities based on the detected deviations.

By incorporating data pipeline automation and real-time alerts, the project will become more robust and capable of handling larger datasets while providing valuable insights and proactive monitoring for decision-making.








