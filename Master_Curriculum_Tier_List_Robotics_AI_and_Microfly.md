# 👑 IIT Madras BS Cross-Curriculum Master Tier List: Robotics, AI Systems, Time-Critical Firmware & Microfly Builder

---

## 🧭 Target Engineering Profile & Mission

This document synthesizes and filters courses across all **4 IIT Madras BS Programs**:
1. **BS in Data Science and Applications (DS & AI)**
2. **BS in Electronic Systems (ES)**
3. **BS in Management and Data Science (MDS)**
4. **BS in Aeronautics and Space Technology (AST / Aero)**

### 🎯 Target Specialization:
- **Autonomous Robotics & Smart Gadgets Maker**
- **AI Systems & Deep Learning Vision Expert**
- **Time-Critical, Low-Latency Embedded Firmware Engineer**
- **Microfly / Autonomous Micro-Drone (MAV) Builder with Camera & Sensor Telemetry**

---

# 📊 Master Tier Overview

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ S-TIER (The God-Tier Core) ──► Firmwares, Control Math, Sensors, Flight Dynamics & Edge AI Vision│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ A-TIER (Core Accelerators) ──► DSP/Kalman Filters, RTOS, Aerodynamics, CAD/3D Print, PCB Design │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ B-TIER (High-Value Electives)► Embedded Linux/FPGA, RF Telemetry, MLOps/Quantization, Speech/NLP│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SKIP / LEAVE ENTIRELY      ──► Corporate Finance, Marketing, Web Apps, DBMS, Rocket Turbines     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

# 🏆 S-TIER: The Non-Negotiable Core Arsenal (Must-Take)
*Without these courses, your microfly/robot cannot balance, cannot read sensors, cannot drive motors, and will flip and crash in 50 milliseconds.*

| Program | Course Code | Course Name | Why It Is Crucial for Your Goal |
| :--- | :--- | :--- | :--- |
| **ES** | **CS2101 / CS1101** | **Embedded C Programming** *(+ Intro to C)* | **The Firmware Engine**: Writing low-level 1 ms control loops, reading I2C/SPI sensor registers, and generating PWM signals to motor ESCs. |
| **ES** | **EE3102** | **Control Engineering** | **The Brain of Stability**: Feedback control (PID, State-Space, Pole Placement). Without this, a flying drone flips and crashes in 50 ms. |
| **ES** | **EE3103 / EE3104** | **Sensors and Applications (+ Lab)** | **The Eyes & IMU**: Interfacing 6-axis Gyros, Accelerometers, Barometers, LIDAR, and Optical Flow sensors; noise filtering and calibration. |
| **Aero** | **BSAS4012** | **Design Project: Design of MAVs and UAVs** | **Direct Practical Target**: Dedicated hands-on design and build project for Micro Aerial Vehicles (MAVs) and Drones! |
| **Aero** | **BSAS3003 & BSAS4007**| **Flight Dynamics I & Aerospace Control/Estimation**| **3D Flight Physics**: 6-DOF equations of motion (Roll, Pitch, Yaw), aerodynamic stability derivatives, and state estimation (Kalman filters). |
| **DS** | **BSDA5006** | **Deep Learning for Computer Vision** | **Visual Navigation**: Processing camera feeds on edge devices for real-time obstacle avoidance, target tracking, and visual odometry. |
| **DS/ES**| **BSCS2004 / BSCS3004**| **ML Foundations & Deep Learning** | **AI Architectures**: Mastering neural network design, loss functions, backprop, and training custom edge models. |
| **ES** | **EE1103 & EE2102** | **Circuits & Analog Electronic Systems** | **Motor Drivers & Hardware**: MOSFET H-bridges, motor switching circuits, and analog signal conditioning. |
| **ES** | **EE5103** | **Power Management for Electronic Systems** | **Battery & Weight Optimization**: High-efficiency buck/boost switching converters and power budgeting for ultra-lightweight LiPo batteries. |
| **All** | **MA1101 & MA2101/2**| **Math for Electronics & Aero I & II** | Multivariable calculus, differential equations, and linear algebra governing 3D spatial rotations (quaternions). |

---

# 🥇 A-TIER: Core Accelerators (High Value)
*Take these to build custom lightweight PCBs, filter out violent motor vibrations, and implement autonomous path planning.*

| Program | Course Code | Course Name | Value & Impact |
| :--- | :--- | :--- | :--- |
| **ES** | **EE3101** | **Digital Signal Processing (DSP)** | **Sensor Fusion**: Implementing complementary and Kalman filters to fuse noisy accelerometer data with drifting gyroscope data. |
| **DS** | **BSDA5007** | **Reinforcement Learning (Special Topics in ML)** | **Autonomous Control**: Sim-to-real reinforcement learning for training robotic locomotion and adaptive drone recovery maneuvers. |
| **DS** | **BSCS4022 / BSSE2001**| **Operating Systems & System Commands** | **Time-Critical Systems**: Real-time OS (FreeRTOS / RT-Linux), multithreading, priority inversion, and deterministic low-latency scheduling. |
| **Aero** | **BSAS3001 & BSAS2001**| **Aerodynamics & Fluid Mechanics** | **Lift & Thrust Physics**: Understanding rotor blade aerodynamics and thrust generation at micro-scale (low Reynolds numbers). |
| **Aero** | **BSAS2011 & BSAS2002**| **Solid Modeling of Aircraft & Strength of Materials** | **Gadget CAD & 3D Printing**: 3D CAD modeling (Fusion360/SolidWorks) and stress analysis to fabricate ultra-lightweight carbon-fiber/nylon frames. |
| **ES** | **EE4102 & EE4108** | **Electronic Product Design & Testing/Measurement**| **Custom Flight PCB**: Designing 4-layer micro-PCBs and debugging hardware noise with oscilloscopes and logic analyzers. |
| **DS** | **BSCS3003** | **AI: Search Methods for Problem Solving** | **Autonomous Path Planning**: $A^*$, Dijkstra, and RRT* trajectory planning through obstacle maps. |
| **DS** | **BSCS2002** | **DSA using Python** | High-level data structures and algorithms for ground-station telemetry and robotics simulation. |

---

# 🥈 B-TIER: High-Value Electives (Touch Later / As Needed)
*Secondary specializations depending on whether you want RF antennas, companion computers, or voice interfaces.*

| Program | Course Code | Course Name | When to Take |
| :--- | :--- | :--- | :--- |
| **ES** | **EE3102** | **Embedded Linux and FPGAs** | If your microfly carries an onboard companion computer (e.g. Raspberry Pi Zero / Kria FPGA for high-speed edge AI). |
| **ES** | **EE3105** | **Electromagnetic Fields & Transmission Lines** | For designing custom 2.4 GHz / 5.8 GHz RF telemetry and video transmission antennas. |
| **DS** | **BSDA5014 / BSDA6003**| **MLOps & Deployability Aspects of AI** | Quantizing models (INT8/FP16) and deploying onto micro-NPUs and microcontrollers (TensorRT, ONNX, TFLite-Micro). |
| **DS/ES**| **BSEE4001 / BSDA5005**| **Speech Technology & NLP** | For building voice-controlled interactive robots and smart gadgets (like the Rose voice AI project). |
| **DS** | **BSCS4024** | **Computer Networks** | Streaming live video and sensor telemetry via low-latency UDP/Wi-Fi to your ground station laptop. |
| **Aero** | **BSAS4004** | **Vibrations and Aero-Elasticity** | Understanding structural resonance to prevent motor vibrations from blinding the gyro sensors. |

---

# ❌ TIER 4: Leave / Skip Entirely (Zero Value for Hardware & Robots)

Do **not** waste time or course credits on these:

1. **All Business, Finance & Management (from MDS & DS)**:  
   *`Corporate Finance`, `Principles of Economics`, `Financial Accounting`, `Financial Forensics`, `HR Analytics`, `Marketing Analytics/Management`, `Macroeconomics`, `Market Research`, `Family Business`, `Brand Management`.*
2. **Enterprise Web & Database Software**:  
   *`Database Management Systems (DBMS)`, `Modern Application Development I & II`, `Programming Concepts using Java`.*
3. **Heavy Rocket & Turbine Engines (Aero)**:  
   *`Gas Turbine Propulsion`, `Rocket Propulsion for Space Applications` (Irrelevant for battery-powered micro-fliers and robots).*
4. **Silicon Fabrication & Bioinformatics**:  
   *`Semiconductor & VLSI Technology`, `Digital IC Design`, `Bioinformatics & Biological Networks`, `Biomedical Electronic Systems`.*

---

# 🚀 The Ultimate Integrated Semester-by-Semester Roadmap

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: Foundations & Electronics (Hardware Base)                                               │
│ Math I & II ──► Intro to C ──► Electrical Circuits ──► Analog Systems                            │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 2: Firmware, Control & Aerodynamics (Flight Base)                                          │
│ Embedded C (CS2101) ──► Control Engineering (EE3102) ──► Signals & Systems (EE2101) ──► Aerodynamics│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 3: Sensors, DSP & Drone Mechanics (The Flying Bot)                                         │
│ Sensors & Lab (EE3103/4) ──► DSP / Kalman (EE3101) ──► Flight Dynamics (BSAS3003) ──► Power (EE5103) │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 4: AI Vision, Autonomous Robotics & MAV Project (The Masterstroke)                         │
│ Deep Learning (CS3004) ──► Computer Vision (BSDA5006) ──► Reinforcement Learning ──► MAV Project│
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```
