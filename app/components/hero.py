import streamlit as st
from textwrap import dedent


def hero_section():

    st.markdown(
        dedent("""
<div class="hero">

<!-- LEFT SIDE -->

<div class="hero-left">

<div class="hero-badge">
✨ AI Powered Roommate Intelligence
</div>

<h1 class="hero-brand">
RoomSync AI
</h1>

<h2 class="hero-title">

Find Your <span>Perfect</span><br>

Roommate Using<br>

<span>Explainable AI</span>

</h2>

<p class="hero-description">

RoomSync AI analyzes over <strong>207 behavioural signals</strong>
including sleep schedule, cleanliness, study habits,
privacy preferences and lifestyle compatibility to
recommend roommates you'll actually enjoy living with.

</p>

<div class="hero-highlights">

<div>✓ 207 behavioural signals</div>

<div>✓ Explainable AI recommendations</div>

<div>✓ No personality quizzes</div>

</div>

<div class="hero-buttons">

<a href="#" class="primary-btn">
🚀 Start Matching
</a>


<button class="secondary-btn">
▶ Watch Demo
</button>

</div>

<div class="trust-row">

<div class="trust-item">
🧠 Explainable AI
</div>

<div class="trust-item">
⚡ XGBoost
</div>

<div class="trust-item">
✨ SHAP
</div>

<div class="trust-item">
📊 207 Signals
</div>

</div>

</div>

<!-- RIGHT SIDE -->

<div class="hero-right">

<div class="compatibility-card">

<div class="live-status">

● LIVE AI ENGINE

</div>

<h3>

🧠 AI Matching Engine

</h3>

<p class="score-label">

Compatibility Score

</p>

<div class="compatibility-score">

❤️ 96.8%

</div>

<div class="progress-bar">

<div class="progress-fill"></div>

</div>

<p class="prediction-text">

Predicted using behavioural similarity,
explainable AI and machine learning.

</p>

<div class="match-list">

<div>✓ Sleep Compatibility</div>

<div>✓ Cleanliness Match</div>

<div>✓ Privacy Balance</div>

<div>✓ Study Schedule Match</div>

</div>

<div class="card-divider"></div>

<div class="mini-stats">

<div>
<span>Wake Time</span>
<strong>7:00 AM</strong>
</div>

<div>
<span>Noise Level</span>
<strong>Low</strong>
</div>

<div>
<span>Lifestyle Match</span>
<strong>94%</strong>
</div>

</div>

</div>

</div>

</div>
"""),
unsafe_allow_html=True,
)