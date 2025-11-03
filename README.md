# Python-Code-of-Pulse-Echo-project
Project: Using Phthon find acoustic attenuation in Vibration-Damping Alloys(Automatic code to detect acoustic attenuation and speed in composite alloys).

Project Overview

•	Utilized Python programming for the analysis and visualization of Pulse-Echo data.
•	Developed Python code to automatically identify individual echoes within a pulse of Pulse-Echo Data.
•	Employed advanced algorithms for accurate and efficient echo detection.
•	Implemented code to perform correlation analysis between the 1st echo and consecutive echoes.
•	Utilized correlation results to calculate the time delay between echoes.
•	Leveraged the calculated time delay to determine the velocity of the acoustic wave in the material.
•	Computed the attenuation coefficient based on the obtained data.
•	Ensured automation in the process, enhancing the efficiency of echo identification and analysis.
•	Improved accuracy through systematic correlation analysis.
•	Obtained valuable insights into the acoustic properties of the material under examination.
•	Results contribute to a better understanding of the velocity and attenuation coefficient of the acoustic wave. Using attenuation and velocity, we ncan relate engineering damping and 
quality factor of composite alloy.


# ⚙️ Acoustic Attenuation and Pulse–Echo Analysis in Vibration-Damping Alloys

This project presents a comprehensive **ultrasonic Pulse–Echo analysis** of **vibration-damping metallic alloys** using **Python-based signal processing**.  
The study automated Python based data analysis to evaluates the **sound velocity** and **attenuation coefficient** of Fe–Mn–V–C alloys to understand their acoustic damping properties, which play a critical role in applications such as **naval stealth materials** and **noise reduction systems**.

---

## 🧩 Figure 1: Experimental Motivation and Objective

This figure outlines the **motivation** behind developing vibration-damping alloys for stealth applications.  
Submarine hulls generate mechanical vibrations that can radiate sound into water, making them detectable by passive or active SONAR systems.  
By using alloys with high acoustic attenuation, such vibrations can be absorbed efficiently, leading to **quieter and more secure naval operations**.

The project focuses on three alloys (Samples A, B, and C) containing different ratios of Fe, Mn, V, and C.  
Each material was tested using a **Pulse–Echo ultrasonic setup** to derive quantitative damping characteristics.

### 📌 Figure 1:
![Figure 1](images/figure1_motivation.png)

---

## 🧪 Figure 2: Pulse–Echo Ultrasonic Setup

The **experimental setup** includes:
- **Pulser–Receiver (PR)** unit for generating and detecting ultrasonic pulses  
- **Oscilloscope** for visualizing the returning echoes  
- **Transducer** for transmitting and receiving signals through the alloy sample  

This system captures **multiple echo reflections** corresponding to successive internal reflections within the sample.

### 📌 Figure 2:
![Figure 2](images/figure2_setup.png)

---

## 📊 Figure 3: Typical Pulse–Echo Waveform

This figure displays a **representative Pulse–Echo signal** recorded from one alloy.  
The first large pulse corresponds to the initial reflection, followed by successive echoes (2nd, 3rd, etc.), each with progressively reduced amplitude due to internal attenuation.

The **decay of echo amplitude** reveals material damping characteristics, while the **time difference between echoes** determines the **sound velocity**.

### 📌 Figure 3:
![Figure 3](images/figure3_echo_waveform.png)

---

## 🔍 Figure 4: Correlation Analysis for Time Delay Estimation

The **Python analysis script** applies cross-correlation between the **first echo (reference)** and each subsequent echo to find precise **time delays**.  
This ensures accurate computation of sound velocity, minimizing human error in manual measurement.

### 📌 Figure 4:
![Figure 4](images/figure4_correlation_analysis.png)

---

## 🧮 Figures 5–6: Velocity Calculation for Alloy B

A **linear regression** between depth and time delay was used to calculate the sound velocity in Alloy B.  
Ten time traces were recorded for statistical reliability.  
The slope of the fitted line represents the **velocity (m/s)**, with a near-perfect **R² ≈ 0.9998**, indicating highly consistent data.

### 📌 Figure 5:
![Figure 5](images/figure5_velocity_fit_B.png)

### 📌 Figure 6:
![Figure 6](images/figure6_velocity_stats_B.png)

---

## 📈 Figures 7–8: Velocity Calculation for Alloy C

Alloy C shows a similar relationship between **depth** and **time delay**, but with slightly different velocity due to composition variations.  
Statistical analysis revealed a small decrease in mean velocity, suggesting microstructural effects.

### 📌 Figure 7:
![Figure 7](images/figure7_velocity_fit_C.png)

### 📌 Figure 8:
![Figure 8](images/figure8_velocity_stats_C.png)

---

## 📉 Figures 9–10: Attenuation Coefficient Analysis

The **attenuation coefficient (α)** was determined from the exponential decay of echo amplitudes.  
By fitting the **logarithm of amplitude ratio (log(A₀/Aᵢ))** against the corresponding depth, a linear trend was obtained, where the slope gives α.  
Higher α indicates greater damping capacity.

### 📌 Figure 9:
![Figure 9](images/figure9_attenuation_fit_B.png)

### 📌 Figure 10:
![Figure 10](images/figure10_attenuation_fit_C.png)

---

## 📋 Figure 11: Comparative Summary of Velocity and Attenuation

This comparison shows that both alloys exhibit similar velocities (~5800 m/s) but different attenuation coefficients.  
Alloy C has higher attenuation (α ≈ 0.84 Np/m) than Alloy B (α ≈ 0.62 Np/m), suggesting improved internal damping due to compositional or structural differences.

| Property | Alloy B | Alloy C |
|-----------|----------|----------|
| Mean Velocity (m/s) | 5850 | 5820 |
| Velocity Std. Dev. | ±50 | ±60 |
| Attenuation Coefficient (Np/m) | 0.62 | 0.84 |
| R² (Velocity Fit) | 0.9998 | 0.9996 |

### 📌 Figure 11:
![Figure 11](images/figure11_comparison_chart.png)

---

## 🧠 Figure 12: Microstructural Interpretation

Differences in attenuation are attributed to **scattering, absorption, and porosity** within the alloy microstructure.  
Increased attenuation (as in Alloy C) may arise from greater **dislocation density** or **grain boundary scattering**, enhancing its **vibrational damping efficiency**.

### 📌 Figure 12:
![Figure 12](images/figure12_microstructure_effects.png)

---

## 🔭 Figure 13: Future Work and Research Goals

Future work includes:
- **Scanning Electron Microscopy (SEM)** to correlate attenuation with alloy microstructure  
- Investigating **tensile strength** and **elastic modulus** to link acoustic and mechanical damping  
- Exploring other **Fe–Mn–V–C** alloy compositions to optimize acoustic performance  

### 📌 Figure 13:
![Figure 13](images/figure13_future_goals.png)

---

## 💻 Tools Used

- **Python:** NumPy, SciPy, pandas, Matplotlib for data analysis and visualization  
- **Signal Processing:** Cross-correlation for echo alignment and delay estimation  
- **Linear Regression:** For calculating velocity and attenuation  
- **PowerPoint:** Visualization and slide generation  
- **GitHub Actions:** Continuous integration testing of analysis scripts  

---

## 📚 Key Insights

- Developed a fully automated **Python workflow** for Pulse–Echo analysis  
- Achieved **high accuracy (R² ≈ 0.9998)** in velocity estimation  
- Quantified **attenuation coefficients** reflecting alloy damping capacity  
- Demonstrated correlation between **material composition** and **acoustic properties**  
- Provided a foundation for linking **ultrasonic damping** to **engineering quality factors (Q)**  

---

## 🏁 Conclusion

This project integrates **physics, materials science, and computational analysis** to characterize vibration-damping metallic alloys.  
By determining the **velocity** and **attenuation coefficient**, the work advances understanding of **acoustic damping mechanisms** and supports the development of alloys optimized for **quiet, durable, and energy-efficient systems**.

---

### 📘 References
Petculescu, G. et al., *Acoustic Attenuation in Vibration-Damping Alloys*, University of Louisiana at Lafayette, 2023.

---

## 🗂️ Repository Structure



