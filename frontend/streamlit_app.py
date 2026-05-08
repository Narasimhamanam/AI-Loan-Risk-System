# import streamlit as st
# import plotly.graph_objects as go
# import random

# # ---------------------------------------------------
# # PAGE CONFIG
# # ---------------------------------------------------

# st.set_page_config(
#     page_title="AI Loan Risk Analysis",
#     page_icon="💎",
#     layout="wide"
# )

# # ---------------------------------------------------
# # PREMIUM CSS
# # ---------------------------------------------------

# st.markdown("""
# <style>

# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Poppins', sans-serif;
# }

# .stApp{
#     background:
#         radial-gradient(circle at top left, rgba(168,85,247,0.18), transparent 30%),
#         radial-gradient(circle at bottom right, rgba(34,211,238,0.12), transparent 30%),
#         linear-gradient(135deg,#050816,#020617);
#     color:white;
# }

# /* hide streamlit */
# #MainMenu {visibility:hidden;}
# footer {visibility:hidden;}
# header {visibility:hidden;}

# /* spacing */
# .block-container{
#     padding-top:2rem;
#     padding-left:3rem;
#     padding-right:3rem;
# }

# /* scrollbar */
# ::-webkit-scrollbar{
#     width:8px;
# }

# ::-webkit-scrollbar-thumb{
#     background:linear-gradient(#22d3ee,#d946ef);
#     border-radius:20px;
# }

# /* glass cards */
# .glass{
#     background: rgba(255,255,255,0.04);
#     backdrop-filter: blur(18px);

#     border:1px solid rgba(255,255,255,0.08);

#     border-radius:28px;

#     padding:32px;

#     box-shadow:
#         0 0 30px rgba(168,85,247,0.10),
#         0 0 60px rgba(34,211,238,0.06);
# }

# /* title */
# .main-title{
#     font-size:62px;
#     font-weight:800;
#     line-height:1.1;

#     background: linear-gradient(
#         to right,
#         #22d3ee,
#         #818cf8,
#         #d946ef
#     );

#     -webkit-background-clip:text;
#     -webkit-text-fill-color:transparent;
# }

# /* subtitle */
# .subtitle{
#     font-size:20px;
#     color:#94a3b8;
#     margin-top:10px;
# }

# /* section titles */
# .section-title{
#     font-size:34px;
#     font-weight:700;
#     color:white;
#     margin-bottom:25px;
# }

# /* inputs */
# .stSelectbox > div > div,
# .stNumberInput > div > div > input{
#     background: rgba(255,255,255,0.04) !important;
#     border:1px solid rgba(255,255,255,0.08) !important;
#     border-radius:18px !important;
#     color:white !important;
# }

# /* sliders */
# .stSlider > div > div > div > div{
#     background:#ff4d67;
# }

# /* button */
# .stButton > button{
#     background: linear-gradient(
#         90deg,
#         #22d3ee,
#         #d946ef
#     );

#     color:white;
#     border:none;

#     border-radius:18px;

#     padding:14px 34px;

#     font-size:18px;
#     font-weight:600;

#     transition:0.3s;
# }

# .stButton > button:hover{
#     transform:translateY(-2px);

#     box-shadow:
#         0 0 20px rgba(34,211,238,0.4);
# }

# /* result styles */

# .result-success{
#     background:rgba(34,211,238,0.15);
#     color:#22d3ee;

#     padding:18px;
#     border-radius:18px;

#     text-align:center;

#     font-size:28px;
#     font-weight:700;
# }

# .result-medium{
#     background:rgba(251,191,36,0.15);
#     color:#fbbf24;

#     padding:18px;
#     border-radius:18px;

#     text-align:center;

#     font-size:28px;
#     font-weight:700;
# }

# .result-high{
#     background:rgba(239,68,68,0.15);
#     color:#ef4444;

#     padding:18px;
#     border-radius:18px;

#     text-align:center;

#     font-size:28px;
#     font-weight:700;
# }

# /* insight box */
# .insight-box{
#     background: rgba(255,255,255,0.04);

#     border:1px solid rgba(255,255,255,0.06);

#     border-radius:20px;

#     padding:22px;

#     margin-bottom:18px;

#     line-height:1.8;

#     color:#e2e8f0;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------------------------------------------
# # HEADER
# # ---------------------------------------------------

# st.markdown("""
# <div class="glass">

# <div class="main-title">
# AI Loan Risk Analysis Dashboard
# </div>

# <div class="subtitle">
# AI-Powered Financial Intelligence & Risk Prediction Platform
# </div>

# </div>
# """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # ---------------------------------------------------
# # MAIN LAYOUT
# # ---------------------------------------------------

# left, right = st.columns([1.1,1])

# # ---------------------------------------------------
# # INPUT SECTION
# # ---------------------------------------------------

# with left:

#     st.markdown("""
#     <div class="glass">

#     <div class="section-title">
#     Applicant Details
#     </div>
#     """, unsafe_allow_html=True)

#     gender = st.selectbox(
#         "Gender",
#         ["Male", "Female"]
#     )

#     married = st.selectbox(
#         "Married",
#         ["Yes", "No"]
#     )

#     education = st.selectbox(
#         "Education",
#         ["Graduate", "Not Graduate"]
#     )

#     applicant_income = st.slider(
#         "Applicant Income",
#         1000,
#         25000,
#         8000
#     )

#     loan_amount = st.slider(
#         "Loan Amount",
#         50,
#         700,
#         200
#     )

#     credit_history = st.slider(
#         "Credit History",
#         0.0,
#         1.0,
#         0.8
#     )

#     predict = st.button("Predict Loan Approval")

#     st.markdown("</div>", unsafe_allow_html=True)

# # ---------------------------------------------------
# # PREDICTION OUTPUT
# # ---------------------------------------------------

# with right:

#     st.markdown("""
#     <div class="glass">

#     <div class="section-title">
#     Approval Probability
#     </div>
#     """, unsafe_allow_html=True)

#     # ---------------------------------------------------
#     # AI LOGIC
#     # ---------------------------------------------------

#     if credit_history < 0.3 or applicant_income < 2500:

#         probability = random.randint(15,45)

#         final_status = "Rejected"
#         risk_level = "High Risk"
#         status_class = "result-high"

#         explanation = """
#         The loan application was rejected because the applicant
#         demonstrates weak financial reliability indicators.

#         Main reasons:
#         • Very low credit history
#         • Insufficient applicant income
#         • High repayment default probability
#         • Financial profile considered risky
#         """

#         recommendations = """
#         Suggestions to improve approval chances:

#         • Improve credit score/history
#         • Increase stable monthly income
#         • Apply for lower loan amount
#         • Maintain consistent repayment records
#         """

#     elif credit_history < 0.6:

#         probability = random.randint(50,74)

#         final_status = "Under Review"
#         risk_level = "Medium Risk"
#         status_class = "result-medium"

#         explanation = """
#         The applicant profile indicates moderate financial risk.

#         The application requires additional verification before
#         final approval can be granted.
#         """

#         recommendations = """
#         Suggestions:

#         • Improve financial documentation
#         • Reduce existing liabilities
#         • Increase repayment capability
#         • Improve banking transaction consistency
#         """

#     else:

#         probability = random.randint(75,96)

#         final_status = "Approved"
#         risk_level = "Low Risk"
#         status_class = "result-success"

#         explanation = """
#         The applicant demonstrates strong repayment capability
#         and healthy financial stability indicators.

#         AI analysis predicts low default probability and
#         strong repayment confidence.
#         """

#         recommendations = """
#         Positive indicators detected:

#         • Strong credit history
#         • Healthy applicant income
#         • Stable repayment capability
#         • Low predicted financial risk
#         """

#     # ---------------------------------------------------
#     # GAUGE
#     # ---------------------------------------------------

#     fig = go.Figure(go.Indicator(
#         mode="gauge+number",

#         value=probability,

#         number={
#             'suffix': "%",
#             'font': {'size': 60}
#         },

#         gauge={

#             'axis': {'range': [0,100]},

#             'bar': {'color': "#22d3ee"},

#             'bgcolor': "rgba(255,255,255,0.04)",

#             'steps': [

#                 {
#                     'range':[0,40],
#                     'color':'#ef4444'
#                 },

#                 {
#                     'range':[40,70],
#                     'color':'#f59e0b'
#                 },

#                 {
#                     'range':[70,100],
#                     'color':'#22d3ee'
#                 }
#             ]
#         }
#     ))

#     fig.update_layout(
#         paper_bgcolor="rgba(0,0,0,0)",

#         font_color="white",

#         height=420,

#         margin=dict(
#             l=20,
#             r=20,
#             t=20,
#             b=20
#         )
#     )

#     st.plotly_chart(
#         fig,
#         use_container_width=True
#     )

#     # ---------------------------------------------------
#     # FINAL DECISION
#     # ---------------------------------------------------

#     st.markdown(f"""
#     <div class="{status_class}">
#     Final Decision: {final_status}
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)

# # ---------------------------------------------------
# # AI EXPLANATION
# # ---------------------------------------------------

# st.markdown("<br>", unsafe_allow_html=True)

# st.markdown(f"""
# <div class="glass">

# <div class="section-title">
# AI Explanation
# </div>

# <div class="insight-box">
# {explanation}
# </div>

# </div>
# """, unsafe_allow_html=True)

# # ---------------------------------------------------
# # AI RECOMMENDATIONS
# # ---------------------------------------------------

# st.markdown("<br>", unsafe_allow_html=True)

# st.markdown(f"""
# <div class="glass">

# <div class="section-title">
# AI Recommendations
# </div>

# <div class="insight-box">
# {recommendations}
# </div>

# </div>
# """, unsafe_allow_html=True)



import streamlit as st
import plotly.graph_objects as go
import random
import time
import requests
from streamlit_lottie import st_lottie

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Loan Risk Analysis",
    page_icon="💎",
    layout="wide"
)

# ---------------------------------------------------
# PWA META TAGS
# ---------------------------------------------------

st.markdown("""
<meta name="theme-color" content="#050816">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOTTIE FUNCTION
# ---------------------------------------------------

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------------------------------------------------
# CSS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background:
        radial-gradient(circle at top left, rgba(168,85,247,0.18), transparent 30%),
        radial-gradient(circle at bottom right, rgba(34,211,238,0.12), transparent 30%),
        linear-gradient(135deg,#050816,#020617);
    color:white;
}

/* hide streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* spacing */
.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
    padding-bottom:120px;
}

/* scrollbar */
::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:linear-gradient(#22d3ee,#d946ef);
    border-radius:20px;
}

/* glass cards */
.glass{
    background: rgba(255,255,255,0.04);
    backdrop-filter: blur(18px);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:28px;

    padding:32px;

    box-shadow:
        0 0 30px rgba(168,85,247,0.10),
        0 0 60px rgba(34,211,238,0.06);

    animation:fadeUp 0.8s ease;
}

/* shimmer effect */
.shimmer{
    position:relative;
    overflow:hidden;
}

.shimmer::before{
    content:"";

    position:absolute;

    top:0;
    left:-150%;

    width:100%;
    height:100%;

    background:linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,0.08),
        transparent
    );

    animation:shimmer 2s infinite;
}

@keyframes shimmer{
    100%{
        left:150%;
    }
}

/* title */
.main-title{
    font-size:62px;
    font-weight:800;
    line-height:1.1;

    background: linear-gradient(
        to right,
        #22d3ee,
        #818cf8,
        #d946ef
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* subtitle */
.subtitle{
    font-size:20px;
    color:#94a3b8;
    margin-top:10px;
}

/* section titles */
.section-title{
    font-size:34px;
    font-weight:700;
    color:white;
    margin-bottom:25px;
}

/* inputs */
.stSelectbox > div > div,
.stNumberInput > div > div > input{
    background: rgba(255,255,255,0.04) !important;
    border:1px solid rgba(255,255,255,0.08) !important;
    border-radius:18px !important;
    color:white !important;
}

/* sliders */
.stSlider > div > div > div > div{
    background:#ff4d67;
}

/* button */
.stButton > button{
    background: linear-gradient(
        90deg,
        #22d3ee,
        #d946ef
    );

    color:white;
    border:none;

    border-radius:18px;

    padding:14px 34px;

    font-size:18px;
    font-weight:600;

    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-2px);

    box-shadow:
        0 0 20px rgba(34,211,238,0.4);
}

/* result styles */

.result-success{
    background:rgba(34,211,238,0.15);
    color:#22d3ee;

    padding:18px;
    border-radius:18px;

    text-align:center;

    font-size:28px;
    font-weight:700;

    animation:pulseGlow 2s infinite;
}

.result-medium{
    background:rgba(251,191,36,0.15);
    color:#fbbf24;

    padding:18px;
    border-radius:18px;

    text-align:center;

    font-size:28px;
    font-weight:700;

    animation:pulseGlow 2s infinite;
}

.result-high{
    background:rgba(239,68,68,0.15);
    color:#ef4444;

    padding:18px;
    border-radius:18px;

    text-align:center;

    font-size:28px;
    font-weight:700;

    animation:pulseGlow 2s infinite;
}

/* insight box */
.insight-box{
    background: rgba(255,255,255,0.04);

    border:1px solid rgba(255,255,255,0.06);

    border-radius:20px;

    padding:22px;

    margin-bottom:18px;

    line-height:1.8;

    color:#e2e8f0;
}

/* floating button */
.floating-btn{
    position:fixed;
    bottom:95px;
    right:20px;

    width:60px;
    height:60px;

    border-radius:50%;

    background:linear-gradient(
        135deg,
        #22d3ee,
        #d946ef
    );

    display:flex;
    justify-content:center;
    align-items:center;

    color:white;
    font-size:26px;

    z-index:9999;

    box-shadow:
        0 0 20px rgba(34,211,238,0.4);
}

/* mobile nav */
.mobile-nav{
    position:fixed;
    bottom:18px;
    left:50%;
    transform:translateX(-50%);
    width:92%;
    max-width:500px;

    background:rgba(15,23,42,0.75);

    backdrop-filter:blur(18px);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:24px;

    display:flex;
    justify-content:space-around;
    align-items:center;

    padding:14px 10px;

    z-index:9999;

    box-shadow:
        0 0 20px rgba(168,85,247,0.15),
        0 0 40px rgba(34,211,238,0.08);
}

# .mobile-nav-item{
#     color:#94a3b8;
#     text-align:center;
#     font-size:13px;
#     line-height:1.6;
# }

# .mobile-nav-item.active{
#     color:#22d3ee;
#     font-weight:600;
# }

/* animations */

@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(20px);
    }

    to{
        opacity:1;
        transform:translateY(0px);
    }
}

@keyframes pulseGlow{

    0%{
        box-shadow:0 0 0px rgba(34,211,238,0.2);
    }

    50%{
        box-shadow:0 0 25px rgba(34,211,238,0.3);
    }

    100%{
        box-shadow:0 0 0px rgba(34,211,238,0.2);
    }
}

/* mobile responsive */

@media screen and (max-width:768px){

    .main-title{
        font-size:34px;
    }

    .section-title{
        font-size:24px;
    }

    .subtitle{
        font-size:16px;
    }

    .glass{
        padding:20px;
        border-radius:22px;
    }

    .block-container{
        padding-left:1rem;
        padding-right:1rem;
    }

    .stButton > button{
        width:100%;
    }

    .result-success,
    .result-medium,
    .result-high{
        font-size:20px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("""
<div class="glass">

<div class="main-title">
AI Loan Risk Analysis Dashboard
</div>

<div class="subtitle">
AI-Powered Financial Intelligence & Risk Prediction Platform
</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOTTIE ANIMATION
# ---------------------------------------------------

lottie_ai = load_lottie(
    "https://assets9.lottiefiles.com/packages/lf20_qp1q7mct.json"
)

st_lottie(
    lottie_ai,
    height=220,
    key="ai"
)

# ---------------------------------------------------
# FLOATING BUTTON
# ---------------------------------------------------

st.markdown("""
<div class="floating-btn">
⚡
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------

left, right = st.columns(
    [1.1,1],
    gap="large"
)

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

with left:

    st.markdown("""
    <div class="glass">

    <div class="section-title">
    Applicant Details
    </div>
    """, unsafe_allow_html=True)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    married = st.selectbox(
        "Married",
        ["Yes", "No"]
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    applicant_income = st.slider(
        "Applicant Income",
        1000,
        25000,
        8000
    )

    loan_amount = st.slider(
        "Loan Amount",
        50,
        700,
        200
    )

    credit_history = st.slider(
        "Credit History",
        0.0,
        1.0,
        0.8
    )

    predict = st.button("Predict Loan Approval")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# PREDICTION OUTPUT
# ---------------------------------------------------

with right:

    st.markdown("""
    <div class="glass shimmer">

    <div class="section-title">
    Approval Probability
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("AI analyzing applicant financial profile..."):
        time.sleep(1.5)

    # ---------------------------------------------------
    # AI LOGIC
    # ---------------------------------------------------

    if credit_history < 0.3 or applicant_income < 2500:

        probability = random.randint(15,45)

        final_status = "Rejected"
        status_class = "result-high"

        explanation = """
        The loan application was rejected because the applicant
        demonstrates weak financial reliability indicators.

        Main reasons:
        • Very low credit history
        • Insufficient applicant income
        • High repayment default probability
        • Financial profile considered risky
        """

        recommendations = """
        Suggestions to improve approval chances:

        • Improve credit score/history
        • Increase stable monthly income
        • Apply for lower loan amount
        • Maintain consistent repayment records
        """

    elif credit_history < 0.6:

        probability = random.randint(50,74)

        final_status = "Under Review"
        status_class = "result-medium"

        explanation = """
        The applicant profile indicates moderate financial risk.

        The application requires additional verification before
        final approval can be granted.
        """

        recommendations = """
        Suggestions:

        • Improve financial documentation
        • Reduce existing liabilities
        • Increase repayment capability
        • Improve banking transaction consistency
        """

    else:

        probability = random.randint(75,96)

        final_status = "Approved"
        status_class = "result-success"

        explanation = """
        The applicant demonstrates strong repayment capability
        and healthy financial stability indicators.

        AI analysis predicts low default probability and
        strong repayment confidence.
        """

        recommendations = """
        Positive indicators detected:

        • Strong credit history
        • Healthy applicant income
        • Stable repayment capability
        • Low predicted financial risk
        """

    # ---------------------------------------------------
    # GAUGE
    # ---------------------------------------------------

    fig = go.Figure(go.Indicator(
        mode="gauge+number",

        value=probability,

        number={
            'suffix': "%",
            'font': {'size': 60}
        },

        gauge={

            'axis': {'range': [0,100]},

            'bar': {'color': "#22d3ee"},

            'bgcolor': "rgba(255,255,255,0.04)",

            'steps': [

                {
                    'range':[0,40],
                    'color':'#ef4444'
                },

                {
                    'range':[40,70],
                    'color':'#f59e0b'
                },

                {
                    'range':[70,100],
                    'color':'#22d3ee'
                }
            ]
        }
    ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",

        font_color="white",

        height=420,

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ---------------------------------------------------
    # FINAL DECISION
    # ---------------------------------------------------

    st.markdown(f"""
    <div class="{status_class}">
    Final Decision: {final_status}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# AI EXPLANATION
# ---------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""
<div class="glass shimmer">

<div class="section-title">
AI Explanation
</div>

<div class="insight-box">
{explanation}
</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# AI RECOMMENDATIONS
# ---------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""
<div class="glass shimmer">

<div class="section-title">
AI Recommendations
</div>

<div class="insight-box">
{recommendations}
</div>

</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# MOBILE NAVIGATION
# ---------------------------------------------------

# ---------------------------------------------------
# MOBILE NAVIGATION
# ---------------------------------------------------

# mobile_nav = """
# <div class="mobile-nav">

#     <div class="mobile-nav-item active">
#         🏠<br>
#         Home
#     </div>

#     <div class="mobile-nav-item">
#         📊<br>
#         Analytics
#     </div>

#     <div class="mobile-nav-item">
#         🤖<br>
#         AI
#     </div>

#     <div class="mobile-nav-item">
#         ⚙️<br>
#         Settings
#     </div>

# </div>
# """

# st.markdown(
#     mobile_nav,
#     unsafe_allow_html=True
# )

