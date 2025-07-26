<div id="top">

<!-- HEADER STYLE: MODERN -->
<div align="left" style="position: relative; width: 100%; height: 100%; ">
<!-- Make sure SalaryWise-Logo.png is in your repository root folder -->
<img src="SalaryWise-Logo.png" width="" align="right" alt="Project Logo"/>

# <em>Predict Salary in seconds with 98% accuracy.</em>


<!-- BADGES -->
<!-- local repository, no metadata badges. -->

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikitlearn">
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white" alt="NumPy">
<br>
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Plotly-3F4F75.svg?style=for-the-badge&logo=Plotly&logoColor=white" alt="Plotly">
<img src="https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/Matplotlib-11557c.svg?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
<img src="https://img.shields.io/badge/Seaborn-094363.svg?style=for-the-badge&logo=seaborn&logoColor=white" alt="Seaborn">

</div>
</div>
<br clear="right">

---

## 🌌 Table of Contents

- [🌌 Table of Contents](#-table-of-contents)
- [🔮 Overview](#-overview)
- [💫 Features](#-features)
- [🌀 Project Structure](#-project-structure)
    - [✨ Project Index](#-project-index)
- [⭐ Getting Started](#-getting-started)
    - [🌟 Prerequisites](#-prerequisites)
    - [💫 Installation](#-installation)
    - [⚡ Usage](#-usage)
- [✧ Contact me](#-contact-me)

---

## 🔮 Overview

Source Code Summaries provides a complete, ready-to-deploy framework for building salary prediction applications, including a user-friendly Streamlit interface, a comprehensive data analysis notebook, and a well-defined dependency management system.

**Why Source Code Summaries?**

This project accelerates salary data analysis and application development by providing a pre-built structure with integrated data science tools and a user-friendly interface. The core features include:

- **🟢 Reproducible Environments:**  Leverages `requirements.txt` for consistent dependency management across different environments, ensuring seamless deployment and collaboration.
- **🔵 Streamlit-Powered UI:**  The `salarywise_app.py` file utilizes Streamlit to create an intuitive and interactive user interface, minimizing front-end development effort.
- **🟡 Data-Driven Insights:**  The Jupyter Notebook (`Salary_Wise.ipynb`) facilitates comprehensive exploratory data analysis (EDA) using pandas and other data science libraries.
- **🟠 Pre-trained Model Integration:**  Seamlessly integrates pre-trained models (indicated by `joblib` import) for faster development and potentially improved prediction accuracy.
- **🟣  Modular Design:**  Cleanly separated components (app, analysis, dependencies) promote maintainability, scalability, and efficient teamwork.
- **⚫️  Visualizations:**  Utilizes powerful visualization libraries like Plotly and Matplotlib for clear and effective data representation.

---

## 💫 Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>A monolithic application built using the **Streamlit** framework for the user interface.</li></ul> |
| 📄 | **Documentation** | <ul><li>`Salary_Wise.ipynb` Jupyter Notebook serves as detailed documentation for the data analysis, preprocessing, and model training process.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>`Streamlit:` For building the interactive web application.</li><li>`Pandas & NumPy:` For data manipulation and numerical operations.</li><li>`Scikit-learn:` For machine learning model training and preprocessing.</li><li>`Plotly:` For creating interactive data visualizations</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Extensive use of data science and machine learning libraries (e.g., `scikit-learn`, `pandas`, `numpy`).</li><li>Web framework dependencies (`streamlit`).</li><li>Visualization libraries (`matplotlib`, `seaborn`, `plotly`).</li><li>All required Python packages are listed in the `requirements.txt` file, managed via `pip`.</li></ul> |


---

## 🌀 Project Structure

```sh
└── /
    ├── requirements.txt
    ├── Data
    │   └── Salary_Data.csv
    ├── Notebook
    │   └── Salary_Wise.ipynb
    ├── cleaned_dataset.csv
    ├── model.pkl
    ├── preprocessor.pkl
    ├── SalaryWise-Logo.png
    ├── salarywise_app.py
    └── scaler.pkl
```

### ✨ Project Index

<details open>
	<summary><b><code>/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>- The <code>requirements.txt</code> file specifies the projects dependencies<br>- It lists all external libraries and their versions necessary for the application to function correctly, including data science tools like scikit-learn, pandas, and visualization libraries such as Altair, Plotly, and Matplotlib<br>- This ensures consistent and reproducible builds across different environments<br>- The Django frameworks presence suggests a web application context.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/salarywise_app.py'>salarywise_app.py</a></b></td>
					<td style='padding: 8px;'>- The <code>salarywise_app.py</code> file is the main entry point for the SalaryWise application<br>- It uses the Streamlit library to create a user interface, likely leveraging a pre-trained model (indicated by <code>joblib</code> import) and data processing capabilities (<code>pandas</code>, <code>numpy</code>) to provide salary-related insights and visualizations (using <code>plotly</code>)<br>- The application incorporates styling and potentially animations (<code>streamlit_lottie</code>) to enhance the user experience<br>- In short, its the front-end application responsible for presenting salary predictions or analysis to the user.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- Notebook Submodule -->
	<details>
		<summary><b>Notebook</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ Notebook</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Notebook/Salary_Wise.ipynb'>Salary_Wise.ipynb</a></b></td>
					<td style='padding: 8px;'>- The Jupyter Notebook <code>Salary_Wise.ipynb</code> analyzes salary data within the larger project<br>- Its purpose is to perform exploratory data analysis (EDA) on salary information, likely to understand salary distributions, identify trends, or inform compensation decisions<br>- The specific analyses performed are not detailed in the provided metadata, but the notebooks role is to provide insights derived from the salary data within the broader projects context.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## ⭐ Getting Started

### 🌟 Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip

### 💫 Installation

Build  from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯  git clone https://github.com/JAI-K-910/SalaryWise.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯  cd SalaryWise
    ```

3. **Install the dependencies:**

	```sh
	❯  pip install -r requirements.txt
	```

### ⚡ Usage

To run the application, execute the following command in your terminal from the project's root directory:

	❯ streamlit run salarywise_app.py
	
---
## ✧ Contact me

<!-- BADGES -->
<a href="https://github.com/JAI-K-910">
<img src="https://img.shields.io/badge/GitHub-JAI--K--910-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
</a>
<br>
<a href="https://www.linkedin.com/in/jai-kishore-mahore-a278652b0/">
<img src="https://img.shields.io/badge/LinkedIn-Jai_Kishore_Mahore-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<br>

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
