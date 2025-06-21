![image](https://github.com/user-attachments/assets/ce03bf1d-f5cb-43ff-8299-723095ceff79)
🏀 Bouncing Ball Simulation with Restitution and Gravity
This project visualizes the motion of a bouncing ball under the influence of gravity and a given coefficient of restitution (e). It demonstrates how energy is progressively lost after each bounce due to inelastic collisions.

🔍 Overview
Using basic physics equations, this simulation tracks the height vs time profile of a ball dropped from a certain height. It models:

Gravitational acceleration acting on the ball (g = 9.81 m/s²)

Restitution, or how much energy is retained after each bounce

The way bounce height decreases exponentially after each impact

Time evolution of the system across several bounces

📈 Features
Accurate simulation of multiple bounces

Configurable parameters:

Initial height

Coefficient of restitution (0–1)

Number of bounces

Generates a plot of Height vs Time for easy visualization

⚙️ How It Works
The simulation applies the kinematic equations of motion for free fall and bounce:

Fall time: 
𝑡
=
2
ℎ
/
𝑔
t= 
2h/g
​
 

Rebound height: 
ℎ
next
=
ℎ
⋅
𝑒
2
h 
next
​
 =h⋅e 
2
 

Each bounce is modeled until a specified number is reached or the height becomes negligible.

📊 Output
The output is a stepwise plot showing the ball’s bounce pattern over time:

Each drop and rise is marked

Bounce height diminishes based on restitution

Demonstrates physical damping through energy loss

📦 Requirements
Python 3.x

matplotlib

numpy

Install dependencies with:

bash
Copy
Edit
pip install matplotlib numpy
🚀 Usage
Run the script using:

bash
Copy
Edit
python bouncing_ball.py
Modify the parameters at the top of the script to explore different scenarios (e.g. steel ball vs rubber ball).

🧠 Educational Value
This project is ideal for students and educators looking to explore:

Newtonian mechanics

Energy conservation and loss

The impact of material properties (via restitution) on motion

📜 License
MIT License
