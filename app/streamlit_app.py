#1 libraries
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def validate_inputs(data):

    errors = []

    # Age
    if data["Age at enrollment"] < 17 or data["Age at enrollment"] > 70:
        errors.append("❌ Age must be between 17 and 70.")

    # Admission Grade
    if data["Admission grade"] < 0 or data["Admission grade"] > 200:
        errors.append("❌ Admission Grade must be between 0 and 200.")

    # Average Grade
    if data["Average_grade"] < 0 or data["Average_grade"] > 20:
        errors.append("❌ Average Grade must be between 0 and 20.")

    # Approval Rate
    if data["Approval_rate"] < 0 or data["Approval_rate"] > 100:
        errors.append("❌ Approval Rate must be between 0 and 100.")

    # Total Approved
    if data["Total_approved"] > data["Total_enrolled"]:
        errors.append("❌ Total Approved cannot exceed Total Enrolled.")

    # Previous Qualification Grade
    if data["Previous qualification (grade)"] < 0:
        errors.append("❌ Previous Qualification Grade cannot be negative.")

    return errors
#Page configuration
st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide"
)
#Sidebar
with st.sidebar:

    st.image(
        "https://img.icons8.com/color/240/graduation-cap.png",
        width=120
    )

    st.title("Student Analytics")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "📊 Single Prediction",
            "📂 Batch Prediction",
            "📈 Analytics"
        ]
    )

    st.markdown("---")

    st.info(
        """
        **Student Dropout Prediction**

        Built using

        • LightGBM

        • FastAPI

        • Docker

        • Streamlit
        """
    )
## ---------------- HOME PAGE ---------------- #

if page == "🏠 Home":

    st.title("🎓 Student Dropout Prediction Dashboard")

    st.markdown("""
    Welcome to the **Student Dropout Prediction System**.

    This application uses **Machine Learning (LightGBM)** to predict whether a student is likely to:

    - 🎓 Graduate
    - 📘 Continue Enrollment
    - ⚠️ Drop Out

    It is built using **FastAPI**, **Streamlit**, **Docker**, and **MLflow**.
    """)

    st.divider()

    # Dashboard Metrics
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🤖 Model", "LightGBM")
    col2.metric("🎯 Accuracy", "92%")
    col3.metric("⚡ API", "Running")
    col4.metric("📊 Features", "41")

    st.divider()

    # About the project
    st.subheader("📖 About the Project")

    st.write("""
    This dashboard predicts student academic outcomes based on demographic,
    academic, and socioeconomic information.

    **Main Features:**
    - 📊 Single Student Prediction
    - 📂 Batch CSV Prediction
    - 📈 Interactive Analytics
    - ⭐ Feature Importance Visualization
    - 🐳 Docker Deployment
    - 🔬 MLflow Experiment Tracking
    """)

    st.divider()

    # Technology Stack
    st.subheader("🛠️ Technology Stack")

    tech1, tech2, tech3 = st.columns(3)

    with tech1:
        st.success("""
        **Machine Learning**
        - LightGBM
        - Scikit-learn
        - SHAP
        """)

    with tech2:
        st.info("""
        **Backend**
        - FastAPI
        - Docker
        - MLflow
        """)

    with tech3:
        st.warning("""
        **Frontend**
        - Streamlit
        - Plotly
        - Pandas
        """)

    st.divider()

    st.caption("© 2026 Student Dropout Prediction System")
#Prediction Page
# ---------------- SINGLE PREDICTION ---------------- #


if page == "📊 Single Prediction":

    st.title("📊 Student Information")

    API_URL ="http://api:8000/predict"

    # ---------------- Personal ---------------- #

    st.header("👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider(
            "Age at Enrollment",
            17,
            70,
            20
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        marital_status = st.selectbox(
            "Marital Status",
            [1,2,3,4,5,6]
        )

    with col2:

            nationality = st.number_input(
                "Nationality",
                value=1
            )

            international = st.selectbox(
                "International Student",
                ["No","Yes"]
            )

            displaced = st.selectbox(
                "Displaced Student",
                ["No","Yes"]
            )

    gender = 1 if gender=="Male" else 0
    international = 1 if international=="Yes" else 0
    displaced = 1 if displaced=="Yes" else 0

    # ---------------- Academic ---------------- #

    st.header("🎓 Academic Information")

    col1,col2 = st.columns(2)

    with col1:

        admission_grade = st.slider(
            "Admission Grade",
            0.0,
            200.0,
            120.0
        )

        previous_grade = st.slider(
            "Previous Qualification Grade",
            0.0,
            200.0,
            120.0
        )

        average_grade = st.slider(
            "Average Grade",
            0.0,
            20.0,
            12.0
        )

    with col2:

        course = st.number_input(
            "Course Code",
            value=1
        )

        application_mode = st.number_input(
            "Application Mode",
            value=1
        )

        application_order = st.slider(
            "Application Order",
            1,
            10,
            1
        )
        #Financial Information
    st.header("💰 Financial Information")

    col1,col2 = st.columns(2)

    with col1:

        debtor = st.selectbox(
            "Debtor",
            ["No","Yes"]
        )

        tuition = st.selectbox(
            "Tuition Fees Up to Date",
            ["Yes","No"]
        )

    with col2:

        scholarship = st.selectbox(
            "Scholarship Holder",
            ["No","Yes"]
        )

        unemployment = st.slider(
            "Unemployment Rate",
            0.0,
            30.0,
            10.0
        )

    inflation = st.slider(
        "Inflation Rate",
        -5.0,
        20.0,
        2.0
    )

    gdp = st.slider(
        "GDP",
        -10.0,
        10.0,
        1.0
    )

   #Performance Metrics
    st.header("📈 Performance")

    col1,col2 = st.columns(2)

    with col1:

        approval_rate = st.slider(
            "Approval Rate",
            0.0,
            100.0,
            75.0
        )

        total_approved = st.slider(
            "Total Approved",
            0,
            30,
            12
        )

    with col2:

        total_enrolled = st.slider(
            "Total Enrolled",
            0,
            30,
            12
        )

        grade_improvement = st.slider(
            "Grade Improvement",
            -10.0,
            10.0,
            0.0
        )
    #Predict Button
    st.divider()

    predict = st.button(
        "🚀 Predict Student Status",
        use_container_width=True
    )


    # ---------------------------------------------------------
    # IMPORTANT
    # Fill the remaining features with your own input widgets.
    # Below is only a sample.
    # ---------------------------------------------------------

    data = {

        "Marital status":0,
        "Application mode":1,
        "Application order":1,
        "Course":1,
        "Daytime/evening attendance":1,
        "Previous qualification":1,
        "Previous qualification (grade)":120,
        "Nacionality":1,
        "Mother's qualification":1,
        "Father's qualification":1,
        "Mother's occupation":1,
        "Father's occupation":1,
        "Admission grade":admission_grade,
        "Displaced":1,
        "Educational special needs":0,
        "Debtor":0,
        "Tuition fees up to date":1,
        "Gender":gender,
        "Scholarship holder":1,
        "Age at enrollment":age,
        "International":0,

        "Curricular units 1st sem (credited)":6,
        "Curricular units 1st sem (enrolled)":6,
        "Curricular units 1st sem (evaluations)":6,
        "Curricular units 1st sem (approved)":6,
        "Curricular units 1st sem (grade)":average_grade,
        "Curricular units 1st sem (without evaluations)":0,

        "Curricular units 2nd sem (credited)":6,
        "Curricular units 2nd sem (enrolled)":6,
        "Curricular units 2nd sem (evaluations)":6,
        "Curricular units 2nd sem (approved)":6,
        "Curricular units 2nd sem (grade)":average_grade,
        "Curricular units 2nd sem (without evaluations)":0,

        "Unemployment rate":unemployment,
        "Inflation rate":inflation,
        "GDP":1,

        "Average_grade":average_grade,
        "Total_approved":12,
        "Grade_improvement":0,
        "Total_enrolled":12,
        "Approval_rate":100

    }

    if predict:

        errors = validate_inputs(data)

        if errors:

            st.error("Please correct the following errors:")

            for error in errors:
             st.write(error)

            st.stop()

        with st.spinner("Predicting Student Status..."):

            response = requests.post(API_URL,  json={"data": data})

        if response.status_code == 200:
            st.success("✅ Validation passed. Prediction generated successfully.")

            result = response.json()

            prediction = result["prediction"]

            probs = result["probabilities"]

            confidence = max(probs) * 100

            #st.divider()

            st.divider()

            st.markdown("## 🎯 Prediction Result")

            if prediction == 0:

                status = "🎓 Graduate"
                color = "green"
                risk = "🟢 Low Risk"

            elif prediction == 1:

                status = "⚠️ Dropout"
                color = "red"
                risk = "🔴 High Risk"

            else:

                status = "📘 Enrolled"
                color = "orange"
                risk = "🟠 Medium Risk"

            st.markdown(f"""
            <div style="padding:20px;
            background-color:#F5F5F5;
            border-radius:12px; 
            border-left:8px solid {color};">

            <h2>{status}</h2>

            <h4>Prediction Confidence : {confidence:.2f}%</h4>

            <h4>{risk}</h4>

            </div>
            """, unsafe_allow_html=True)

            st.divider()

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric(
                "Prediction",
                status
            )

            with c2:
                st.metric(
                "Confidence",
                f"{confidence:.2f}%"
            )

            with c3:
                st.metric(
                "Risk Level",
                risk
            )

            prob_df = pd.DataFrame({

                "Class":[
                    "Graduate",
                    "Dropout",
                    "Enrolled"
                ],

                "Probability":probs

            })

            st.subheader("Prediction Probabilities")

            fig = px.bar(
                prob_df,
                x="Class",
                y="Probability",
                color="Class",
                text="Probability"
            )

            fig2 = px.pie(
                prob_df,
                names="Class",
                values="Probability",
                hole=0.45
            )

            gauge = go.Figure(

                go.Indicator(

                    mode="gauge+number",

                    value=confidence,

                    title={"text":"Prediction Confidence"},

                    gauge={

                        "axis":{"range":[0,100]},

                        "bar":{"color":"green"}

                    }

                )

            )
            left, right = st.columns(2)

            with left:
                st.plotly_chart(
                fig,
                use_container_width=True
            )

            with right:
                st.plotly_chart(
                fig2,
                use_container_width=True
            )

            st.plotly_chart(
                gauge,
            use_container_width=True
            )

            st.subheader("📊 Class Probabilities")

            classes = [
            "Graduate",
            "Dropout",
            "Enrolled"
            ]

            for cls, prob in zip(classes, probs):

                st.write(f"### {cls}")

                st.progress(float(prob))

                st.write(f"{prob*100:.2f}%")

            st.subheader("📋 Student Summary")

            summary = pd.DataFrame({

                "Feature":[

                    "Age",

                    "Gender",

                    "Admission Grade",

                    "Average Grade",

                    "Unemployment"

                ],

                "Value":[

                    age,

                    gender,

                    admission_grade,

                    average_grade,

                    unemployment

                ]

            })

            st.subheader("📋 Student Summary")

            c1, c2 = st.columns(2)

            with c1:

                st.metric("Age", age)

                st.metric(
                "Admission Grade",
                admission_grade
            )

                st.metric(
                "Average Grade",
                average_grade
            )

            with c2:

                st.metric(
                "Gender",
                "Male" if gender else "Female"
            )

                st.metric(
                "Unemployment",
                unemployment
                )

                st.metric(
                "Inflation",
                inflation
            )

        else:
            st.error("❌ Prediction Failed")

            st.write("Status Code:", response.status_code)

            try:
                st.json(response.json())
            except:
                st.write(response.text)
# ---------------- BATCH PREDICTION ---------------- #
# ---------------- BATCH PREDICTION ---------------- #

if page == "📂 Batch Prediction":

    st.title("📂 Batch Student Prediction")

    st.write(
        """
        Upload a CSV file containing student information.
        The system will predict the status of every student.
        """
    )

    API_URL = "http://127.0.0.1:8000/predict"

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df = pd.read_csv(uploaded_file)

            st.success("✅ File Uploaded Successfully")

            st.subheader("Preview")

            st.dataframe(df.head())

            st.write(f"Total Students : {len(df)}")

            if st.button(
                "🚀 Predict All Students",
                use_container_width=True
            ):

                predictions = []

                confidence = []

                progress = st.progress(0)

                status = st.empty()

                for i, row in df.iterrows():

                    payload = {
                        "data": row.to_dict()
                    }

                    response = requests.post(
                        API_URL,
                        json=payload
                    )

                    if response.status_code == 200:

                        result = response.json()

                        pred = result["prediction"]

                        probs = result["probabilities"]

                        predictions.append(pred)

                        confidence.append(max(probs) * 100)

                    else:

                        predictions.append("Error")

                        confidence.append(0)

                    progress.progress((i + 1) / len(df))

                    status.write(
                        f"Processing {i+1}/{len(df)}"
                    )

                progress.empty()

                status.empty()

                label_map = {
                    0: "Graduate",
                    1: "Dropout",
                    2: "Enrolled"
                }

                df["Prediction"] = [
                    label_map.get(x, x)
                    for x in predictions
                ]

                df["Confidence (%)"] = [
                    round(x, 2)
                    for x in confidence
                ]

                st.success("🎉 Batch Prediction Completed")

                st.subheader("Prediction Results")

                st.dataframe(df)

                # ---------------- KPI ---------------- #

                c1, c2, c3 = st.columns(3)

                c1.metric(
                    "Total Students",
                    len(df)
                )

                c2.metric(
                    "Graduates",
                    (df["Prediction"] == "Graduate").sum()
                )

                c3.metric(
                    "Dropouts",
                    (df["Prediction"] == "Dropout").sum()
                )

                # ---------------- Pie Chart ---------------- #

                st.subheader("Prediction Distribution")

                pie = px.pie(

                    df,

                    names="Prediction",

                    title="Prediction Distribution",

                    hole=0.45

                )

                st.plotly_chart(
                    pie,
                    use_container_width=True
                )

                # ---------------- Bar Chart ---------------- #

                bar = px.histogram(

                    df,

                    x="Prediction",

                    color="Prediction",

                    title="Prediction Count"

                )

                st.plotly_chart(
                    bar,
                    use_container_width=True
                )

                # ---------------- Download ---------------- #

                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(

                    "📥 Download Prediction Results",

                    csv,

                    "student_predictions.csv",

                    "text/csv",

                    use_container_width=True

                )

        except Exception as e:

            st.error(str(e))
# ---------------- ANALYTICS DASHBOARD ---------------- #

if page == "📈 Analytics":

    import joblib
    import plotly.figure_factory as ff

    st.title("📈 Student Analytics Dashboard")
   
    # ---------------- Load Dataset ---------------- #

    df = pd.read_csv("data/featured_student.csv")

    st.markdown("---")

    # ============================
    # KPI CARDS
    # ============================

    st.subheader("📊 Dataset Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Students",
        len(df)
    )

    c2.metric(
        "Total Features",
        len(df.columns)
    )

    c3.metric(
        "Average Age",
        round(df["Age at enrollment"].mean(),2)
    )

    c4.metric(
        "Average Grade",
        round(df["Average_grade"].mean(),2)
    )

    st.markdown("---")

    # ============================
    # TARGET DISTRIBUTION
    # ============================

    if "Target" in df.columns:

        st.subheader("🎯 Student Status Distribution")

        fig = px.pie(

            df,

            names="Target",

            hole=0.45,

            color="Target",

            title="Student Status"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    # ============================
    # AGE DISTRIBUTION
    # ============================

    st.subheader("👨 Age Distribution")

    fig = px.histogram(

        df,

        x="Age at enrollment",

        nbins=30,

        title="Age Distribution"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ============================
    # AVERAGE GRADE
    # ============================

    st.subheader("📚 Average Grade Distribution")

    fig = px.histogram(

        df,

        x="Average_grade",

        nbins=30,

        title="Average Grade"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ============================
    # APPROVAL RATE
    # ============================

    st.subheader("✅ Approval Rate")

    fig = px.histogram(

        df,

        x="Approval_rate",

        nbins=25,

        title="Approval Rate"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    # ============================
    # CORRELATION HEATMAP
    # ============================

 # ============================
# CORRELATION HEATMAP
# ============================

    st.subheader("🔥 Correlation Heatmap")

    corr = df.corr(numeric_only=True)

# Select top 15 features
    top_features = (
        corr.abs()
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .index
    )

    corr = corr.loc[top_features, top_features]

# Convert values to strings with 3 decimal places
    annotation_text = [
    [f"{value:.3f}" for value in row]
    for row in corr.values
    ]

    fig = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        annotation_text=annotation_text,
        colorscale="Viridis",
        showscale=True
    )

    fig.update_layout(
        width=800,
        height=800
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
         key="correlation_heatmap"
    )
   # st.plotly_chart(fig, use_container_width=True)

    # ============================
    # FEATURE IMPORTANCE
    # ============================

    st.subheader("⭐ Top 10 Important Features")

    model = joblib.load("models/final_model.pkl")

   # st.write("Total Columns:", len(df.columns))
    #st.write("Feature Importances:", len(model.feature_importances_))
   # st.write("Columns:", df.columns.tolist())
   # st.write("Feature Names from Model:", model.feature_name_)
    #feature_names = list(df.columns)
    feature_names = model.feature_name_

    if "Target" in feature_names:
        feature_names.remove("Target")

    importance = pd.DataFrame({

        "Feature": feature_names,

        "Importance": model.feature_importances_

    })

    importance = importance.sort_values(

        by="Importance",

        ascending=False

    ).head(10)

    fig = px.bar(

        importance,

        x="Importance",

        y="Feature",

        orientation="h",

        text="Importance",

        title="Top 10 Feature Importance"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # ============================
    # NUMERIC SUMMARY
    # ============================

    st.subheader("📋 Dataset Summary")

    st.dataframe(

        df.describe(),

        use_container_width=True

    )

    st.markdown("---")

    # ============================
    # SAMPLE DATA
    # ============================

    st.subheader("📂 Dataset Preview")

    st.dataframe(

        df.head(),

        use_container_width=True

    )

    st.markdown("---")

    # ============================
    # DOWNLOAD DATASET
    # ============================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        "📥 Download Dataset",

        csv,

        "featured_student.csv",

        "text/csv",

        use_container_width=True

    )