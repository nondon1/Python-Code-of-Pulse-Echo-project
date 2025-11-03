# Python-Code-of-Pulse-Echo-project
Project: Using Python to find acoustic attenuation in Vibration-Damping Alloys(Automatic code to detect acoustic attenuation and speed in composite alloys).

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


This project presents a comprehensive **ultrasonic Pulse–Echo analysis** of **vibration-damping metallic alloys** using **Python-based signal processing**.  
The study automated Python based data analysis to evaluates the **sound velocity** and **attenuation coefficient** of Fe–Mn–V–C alloys to understand their acoustic damping properties, which play a critical role in applications such as **naval stealth materials** and **noise reduction systems**.

---

## 🧪 Pulse–Echo Ultrasonic Setup

The **experimental setup** includes:
- **Pulser–Receiver (PR)** unit for generating and detecting ultrasonic pulses  
- **Oscilloscope** for visualizing the returning echoes  
- **Transducer** for transmitting and receiving signals through the alloy sample  

This system captures **multiple echo reflections** corresponding to successive internal reflections within the sample.

### 📌 Figure 1:
![Figure 2](https://github.com/nondon1/Python-Code-of-Pulse-Echo-project/blob/main/experiement.png)

---

## 📊 Typical Pulse–Echo Waveform

This figure displays a **representative Pulse–Echo signal** recorded from one alloy.  
The first large pulse corresponds to the initial reflection, followed by successive echoes (2nd, 3rd, etc.), each with progressively reduced amplitude due to internal attenuation.

The **decay of echo amplitude** reveals material damping characteristics, while the **time difference between echoes** determines the **sound velocity**.

### 📌 Figure 2:
![Figure 3](https://github.com/nondon1/Python-Code-of-Pulse-Echo-project/blob/main/Data%20Aqusition.png)


---

## 🧮 Velocity Calculation for Alloy B

A **linear regression** between depth and time delay was used to calculate the sound velocity in Alloy B.  
Ten time traces were recorded for statistical reliability.  
The slope of the fitted line represents the **velocity (m/s)**, with a near-perfect **R² ≈ 0.9998**, indicating highly consistent data.

### 📌 Figure 3:
![Figure 5](https://github.com/nondon1/Python-Code-of-Pulse-Echo-project/blob/main/sound%20speed.png)

### 📌 Figure 4:
![Figure 6](https://github.com/nondon1/Python-Code-of-Pulse-Echo-project/blob/main/Speed%20distribution.png)


---

## 📉 Attenuation Coefficient Analysis

The **attenuation coefficient (α)** was determined from the exponential decay of echo amplitudes.  
By fitting the **logarithm of amplitude ratio (log(A₀/Aᵢ))** against the corresponding depth, a linear trend was obtained, where the slope gives α.  
Higher α indicates greater damping capacity.

### 📌 Figure 5:
![Figure 9](https://github.com/nondon1/Python-Code-of-Pulse-Echo-project/blob/main/attenuation%20coeff.png)

### 📌 Figure 6:
![Figure 10](https://github.com/nondon1/Python-Code-of-Pulse-Echo-project/blob/main/attenuation%20coef%20distribution.png)

---

## 📋 Comparative Summary of Velocity and Attenuation

This comparison shows that both alloys exhibit similar velocities (~5800 m/s) but different attenuation coefficients.  
Alloy C has higher attenuation (α ≈ 0.84 Np/m) than Alloy B (α ≈ 0.62 Np/m), suggesting improved internal damping due to compositional or structural differences.

| Property | Alloy B | Alloy C |
|-----------|----------|----------|
| Mean Velocity (m/s) | 5850 | 5820 |
| Velocity Std. Dev. | ±50 | ±60 |
| Attenuation Coefficient (Np/m) | 0.62 | 0.84 |
| R² (Velocity Fit) | 0.9998 | 0.9996 |




---

## 🔭 Future Work and Research Goals

Future work includes:
- **Scanning Electron Microscopy (SEM)** to correlate attenuation with alloy microstructure  
- Investigating **tensile strength** and **elastic modulus** to link acoustic and mechanical damping  
- Exploring other **Fe–Mn–V–C** alloy compositions to optimize acoustic performance  


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







