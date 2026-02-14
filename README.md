# 🚲 US Bikeshare Data Analysis

An interactive Command-Line Interface (CLI) data analysis project built using **Python and Pandas** to explore bikeshare data from three major U.S. cities.

---

## 📌 Project Overview

This project analyzes bike-share trip data for:

- Chicago
- New York City
- Washington

The application allows users to filter data dynamically by:

- City
- Month (January – June or All)
- Day of Week (Monday – Sunday or All)

Based on the selected filters, the program computes and displays meaningful descriptive statistics about travel patterns and user demographics.

---

## 🎯 Key Features

✔ Interactive CLI-based application  
✔ Dynamic filtering (city, month, day)  
✔ Handles invalid user inputs  
✔ Gracefully handles empty datasets  
✔ Displays raw data in 5-row increments  
✔ Modular function-based architecture  
✔ Execution time tracking for each statistics section

---

## 📊 Dataset Information

The datasets include bike trip records from the **first six months of 2017**.

### Core Columns (All Cities)

- Start Time
- End Time
- Trip Duration (seconds)
- Start Station
- End Station
- User Type (Subscriber / Customer)

### Additional Columns (Chicago & NYC Only)

- Gender
- Birth Year

> Note: Washington dataset does not contain Gender or Birth Year data.

---

## 📈 Statistics Computed

### 🔹 1. Popular Times of Travel

- Most Common Month
- Most Common Day of Week
- Most Common Start Hour

(Extracted using `pd.to_datetime()` and `.dt` attributes)

---

### 🔹 2. Popular Stations & Trips

- Most Common Start Station
- Most Common End Station
- Most Frequent Trip Combination (Start → End)

---

### 🔹 3. Trip Duration Analysis

- Total Travel Time (converted to hours)
- Average Travel Time (converted to minutes)

---

### 🔹 4. User Statistics

- Counts of User Types
- Gender Distribution (if available)
- Earliest Birth Year
- Most Recent Birth Year
- Most Common Birth Year

The program checks for column availability before computing demographic statistics.

---

## 🛠 Technologies Used

- Python 3
- Pandas
- Datetime handling
- CLI (Command-Line Interface)

### Key Pandas Methods Used

- `read_csv()`
- `to_datetime()`
- `mode()`
- `mean()`
- `sum()`
- `value_counts()`
- `dt.month`
- `dt.day_name()`
- `dt.hour`

---

## 💡 Learning Outcomes

Through this project, I gained hands-on experience in:

- Data analysis using **Pandas**
- Extracting and transforming **datetime features**
- Building interactive **CLI applications**
- Writing modular and reusable **Python functions**
- Handling missing data and edge cases
- Implementing robust user input validation
- Performing descriptive statistical analysis

---

## 🧠 Technical Highlights

- Implemented a reusable helper function (`handle_empty_df`) to manage empty DataFrames gracefully
- Added raw data preview functionality in chunks of 5 rows for better user interaction
- Converted trip duration into readable hours and minutes
- Dynamically created trip combinations using column concatenation
- Added execution time tracking for performance visibility and optimization awareness

---

## 📜 Acknowledgment

Data and project guidelines were provided by **Udacity** as part of the _AWS Cloud Data Engineer Nanodegree_ program.
