import streamlit as st

# Page configuration
st.set_page_config(page_title="Project Portfolio Management", layout="wide")

# Header
st.title("Project Portfolio Management (PPM)")
st.subheader("A Strategic Approach to Managing Multiple Projects")

# Introduction
st.write(
    """
    **Project Portfolio Management (PPM)** is a strategic approach to managing multiple projects and programs within an organization. 
    It ensures alignment with business objectives, prioritizes initiatives, and optimizes resource allocation to maximize overall value.
    """
)

# Key Components of PPM
st.header("Key Components of PPM")

# Strategic Alignment
with st.expander("Strategic Alignment"):
    st.write(
        """
        PPM ensures that all projects in the portfolio align with the organization's strategic goals and objectives. 
        This alignment is crucial for maximizing the return on investment and achieving long-term success.
        """
    )

# Project Selection and Prioritization
with st.expander("Project Selection and Prioritization"):
    st.write(
        """
        A critical aspect of PPM is establishing criteria for selecting and prioritizing projects. This involves:
        - Developing a project intake process
        - Creating valuation criteria
        - Using tools such as project portfolio matrices and scoring models
        - Conducting cost-benefit analyses
        """
    )

# Resource Management
with st.expander("Resource Management"):
    st.write(
        """
        Efficient allocation and management of an organization's resources, including personnel, equipment, and financial assets, 
        ensure that resources are used effectively across all projects in the portfolio.
        """
    )

# Risk Management
with st.expander("Risk Management"):
    st.write(
        """
        Identifying and mitigating risks across the project portfolio is a key responsibility in PPM. 
        This involves developing comprehensive risk management plans to address potential issues impacting multiple projects.
        """
    )

# The Role of a Project Portfolio Manager
st.header("The Role of a Project Portfolio Manager")
st.write(
    """
    Project portfolio managers oversee the entire portfolio. Their responsibilities include:
    - Approving or rejecting project proposals
    - Ensuring strategic alignment of projects
    - Managing resource allocation
    - Monitoring portfolio performance
    - Communicating with stakeholders
    """
)

# PPM Process
st.header("PPM Process")
st.write(
    """
    The PPM process typically involves the following steps:
    1. Ensuring strategic alignment
    2. Establishing a project intake process
    3. Defining selection and prioritization criteria
    4. Validating portfolio feasibility
    5. Defining portfolio governance guidelines
    """
)

# Benefits of PPM
st.header("Benefits of PPM")

# Interactive Benefits List
benefits = [
    "Improved decision-making",
    "Better resource utilization",
    "Enhanced risk management",
    "Increased alignment with business strategy",
    "Improved project success rates",
]
selected_benefits = st.multiselect("Select the benefits of PPM to explore:", benefits)

if selected_benefits:
    st.write("### Selected Benefits")
    for benefit in selected_benefits:
        st.write(f"- {benefit}")
else:
    st.write("Select a benefit from the list above to learn more.")

# Conclusion
st.header("Conclusion")
st.write(
    """
    By taking a holistic view of all projects and programs, PPM enables organizations to make informed decisions about which initiatives 
    to pursue and how to allocate resources effectively. Implementing effective PPM drives strategic alignment, enhances resource optimization, 
    and improves overall project success rates.
    """
)
