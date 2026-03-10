# 🏏 Beyond The Scorecard
### *An IPL Strategic Intelligence Suite*

---

## ✍️ Why I Built This
I still remember being a kid, glued to the TV, watching my very first season of the IPL. Back then, cricket was just magic and heroes. Now, as an engineer, I see it as a beautiful, complex system of variables. 

I didn't build this project just to practice Python; I built it to understand the "hidden" game. I wanted to know why my favorite players succeed in some places and struggle in others. This suite is the result of analyzing **278,000+ balls** to find the logic behind the magic.

---

## 🔍 The Moments (What the Data Taught Me)

### 🏡 The Ahmedabad Paradox
We all know **Shubman Gill** loves Ahmedabad, but the data showed me the *true scale* of it. His Strike Rate jumps by **31 points** at home compared to away. But here’s the kicker—while the batting thrives, **Rashid Khan’s economy climbs to 9.28** at the same venue. 

> **The Insight:** At the Narendra Modi Stadium, GT isn't a "bowling-first" team. They are a high-octane batting unit that uses scoreboard pressure to survive a high-scoring ground.

### 🛡️ The "Bumrah-Boult" Tax
In my model, I realized you can't just project runs based on simple averages. You have to account for "Fear Factors."
Facing the MI opening pair of **Jasprit Bumrah and Trent Boult** is a different game entirely. I built a "Tax" into my code that suppresses projected scoring by **~30%** against these two, reflecting the technical struggle even elite batters face against high-pace swing and pinpoint yorkers.

### 🌡️ The 40°C Decision
A captain’s toss decision isn't just a flip of a coin. My **Toss Optimizer** weighs:
* **Soil Friction:** Analyzing Red soil vs. Black soil behavior.
* **Environmental Stress:** Heat levels above **38°C** that favor batting first to avoid physical exhaustion in the sun.
* **The Dew Factor:** Predicting when the ball becomes a "bar of soap" for the bowlers, making a chase much easier.

---

## 🛠️ The Engine Room
* **Data Source:** Cricsheet (Ball-by-ball data, 2008-2025).
* **Philosophy:** **Interpretable Intelligence.** I avoided "Black Box" AI. If the win probability shifts, my code tells you *why* whether it's the "Wicket Penalty," the "Bumrah Tax," or the "Venue Gain."
* **Core Logic:**
$$Projected Total = Current + [(Rem. Overs \times Phase RPO) \times Player Mult \times Wicket Penalty]$$

---

### 📊 Technical Note on Data Integrity
*During the cleaning process, I identified a "Missing 3 Matches" gap in the 2024 season. While most algorithms would flag this as an error, a manual audit confirmed these were the three major washouts (including GT vs KKR). This project prioritizes "Cricket Reality" over "Raw Numbers."*

---
**Connect with me if you love the game as much as I do!**
