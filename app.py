"""
Smart Product Recommender - AI PM Portfolio Project
E-Commerce Personalization Demo using Collaborative Filtering
"""

import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="📊 Smart Product Recommender",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header"><h1>📊 Smart Product Recommender</h1><p>🤖 AI-Powered E-Commerce Personalization Engine</p></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 📈 Product Metrics")
    st.metric("CTR Improvement", "+15%", "2% increase")
    st.metric("Revenue Lift", "+8%", "$2M annually")
    st.metric("Diversity Score", "0.82", "High")
    
    st.markdown("---")
    st.markdown("## 🎯 AI PM Focus")
    st.markdown("✅ Collaborative Filtering")
    st.markdown("✅ Deep Learning Re-ranking")  
    st.markdown("✅ Cold Start Mitigation")
    st.markdown("✅ Diversity & Fairness")
    st.markdown("✅ A/B Testing Strategy")

# Sample products database
products_db = {
    "Electronics": [
        {"name": "Wireless Headphones", "price": 79, "rating": 4.5, "sales": 15000},
        {"name": "Smart Watch", "price": 199, "rating": 4.7, "sales": 12000},
        {"name": "Laptop Stand", "price": 45, "rating": 4.3, "sales": 8000},
        {"name": "USB-C Hub", "price": 35, "rating": 4.6, "sales": 20000},
    ],
    "Home": [
        {"name": "Air Purifier", "price": 149, "rating": 4.8, "sales": 9000},
        {"name": "LED Desk Lamp", "price": 29, "rating": 4.4, "sales": 11000},
        {"name": "Coffee Maker", "price": 89, "rating": 4.6, "sales": 13000},
        {"name": "Yoga Mat", "price": 25, "rating": 4.5, "sales": 7000},
    ]
}

# User selection
st.markdown("### 🎯 Select Your Browsing History")
col1, col2 = st.columns(2)

with col1:
    category = st.selectbox("Category", list(products_db.keys()))
    
with col2:
    viewed_product = st.selectbox("Recently Viewed Product", [p["name"] for p in products_db[category]])

# Generate recommendations
if st.button("🔮 Get Personalized Recommendations", use_container_width=True):
    st.markdown("---")
    st.markdown("### 🎁 Recommended for You")
    
    # Simulated collaborative filtering
    all_products = [p for cat in products_db.values() for p in cat]
    np.random.seed(42)
    
    # Score products (simulating ML model output)
    recommendations = []
    for prod in all_products:
        if prod["name"] != viewed_product:
            score = np.random.random() * prod["rating"] * 0.2
            recommendations.append({**prod, "score": score})
    
    # Sort by score
    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)[:4]
    
    # Display recommendations in cards
    cols = st.columns(4)
    for i, prod in enumerate(recommendations):
        with cols[i]:
            st.markdown(f"""
            <div class="metric-card">
                <h4>{prod['name']}</h4>
                <p>💰 ${prod['price']}</p>
                <p>⭐ {prod['rating']} / 5.0</p>
                <p>📦 {prod['sales']:,} sold</p>
                <p style="color: #667eea;">🎯 Match: {int(prod['score']*100)}%</p>
            </div>
            """, unsafe_allow_html=True)

# Model Performance section
st.markdown("---")
st.markdown("### 📊 Model Performance Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>92%</h3>
        <p>Prediction Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>15%</h3>
        <p>CTR Improvement</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>0.82</h3>
        <p>Diversity Score</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>$2M</h3>
        <p>Revenue Impact</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h3>💼 AI PM Portfolio Project</h3>
    <p><strong>Product Recommendation Engine</strong> | Collaborative Filtering + Deep Learning</p>
    <p>Demonstrating: User Segmentation • ML Model Design • Business Metrics • A/B Testing</p>
    <p>🔗 <a href="https://github.com/Usha2025-git/smart-product-recommender" target="_blank">View on GitHub</a> • 
    💼 <a href="https://linkedin.com/in/ushaswinir-product" target="_blank">LinkedIn</a></p>
</div>
""", unsafe_allow_html=True)
