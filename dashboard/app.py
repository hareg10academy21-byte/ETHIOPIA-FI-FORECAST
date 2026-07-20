import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#---------------------------------------------------
# Page Configuration
#---------------------------------------------------

st.set_page_config(

    page_title="Financial Inclusion Forecasting",

    layout="wide"

)


#---------------------------------------------------
# Sidebar
#---------------------------------------------------

st.sidebar.title("Dashboard Menu")


page = st.sidebar.selectbox(

            "Select Page",

            [

                "Overview",

                "Trends Analysis",

                "Forecast Analysis",

                "Inclusion Projections"

            ]

)


#---------------------------------------------------
# Sample Data
#---------------------------------------------------

years_access = [2011,2014,2017,2021,2024,2025,2026,2027]

access = [14,22,35,46,49,53,55,57]


years_payment = [2014,2017,2021,2024,2025,2026,2027]

payment = [2,8,20,35,40,45,50]


years_mobile = [2021,2024,2025,2026,2027]

mobile_money = [4.7,9.45,12,15,18]


#---------------------------------------------------
# Overview Page
#---------------------------------------------------

if page=="Overview":


    st.title(

    "Forecasting Financial Inclusion in Ethiopia"

    )


    st.header("Current Financial Inclusion Statistics")


    col1,col2,col3,col4=st.columns(4)


    col1.metric(

        "Account Ownership",

        "49%"

    )


    col2.metric(

        "Digital Payment",

        "35%"

    )


    col3.metric(

        "Mobile Money",

        "9.45%"

    )


    col4.metric(

        "NFIS Target",

        "60%"

    )



    st.divider()


    col1,col2,col3,col4=st.columns(4)


    col1.metric(

        "Telebirr Users",

        "54M+"

    )


    col2.metric(

        "M-PESA Users",

        "10M+"

    )


    col3.metric(

        "Growth",

        "+3%"

    )


    col4.metric(

        "Forecast 2027",

        "57%"

    )


    st.divider()


    fig,ax=plt.subplots()


    ax.plot(

            years_access,

            access,

            marker="o"

            )


    ax.set_title(

            "Account Ownership Trend"

            )


    ax.set_xlabel(

            "Year"

            )


    ax.set_ylabel(

            "Percentage"

            )


    st.pyplot(fig)



#---------------------------------------------------
# Trends Analysis
#---------------------------------------------------

elif page=="Trends Analysis":


    st.title(

    "Trends Analysis"

    )


    start_year,end_year=st.slider(

        "Select Year Range",

        2011,

        2027,

        (2011,2027)

    )


    st.subheader(

    "Account Ownership Trend"

    )


    fig1,ax1=plt.subplots()


    ax1.plot(

            years_access,

            access,

            marker="o"

            )


    ax1.set_xlabel("Year")

    ax1.set_ylabel("Percentage")


    st.pyplot(fig1)



    st.subheader(

    "Digital Payment Trend"

    )


    fig2,ax2=plt.subplots()


    ax2.plot(

            years_payment,

            payment,

            marker="o"

            )


    ax2.set_xlabel("Year")

    ax2.set_ylabel("Percentage")


    st.pyplot(fig2)



    st.subheader(

    "Mobile Money Trend"

    )


    fig3,ax3=plt.subplots()


    ax3.plot(

            years_mobile,

            mobile_money,

            marker="o"

            )


    ax3.set_xlabel("Year")

    ax3.set_ylabel("Percentage")


    st.pyplot(fig3)



#---------------------------------------------------
# Forecast Analysis
#---------------------------------------------------

elif page=="Forecast Analysis":


    st.title(

    "Forecast Analysis"

    )


    scenario=st.selectbox(

            "Select Scenario",

            [

                "Baseline",

                "Optimistic",

                "Pessimistic"

            ]

    )



    if scenario=="Baseline":

        values=[53,55,57]


    elif scenario=="Optimistic":

        values=[55,58,60]


    else:

        values=[51,53,55]



    years=[2025,2026,2027]


    fig,ax=plt.subplots()


    ax.plot(

            years,

            values,

            marker="o"

            )


    ax.set_title(

            scenario+" Forecast"

            )


    ax.set_xlabel(

            "Year"

            )


    ax.set_ylabel(

            "Percentage"

            )


    st.pyplot(fig)



    forecast=pd.DataFrame(


            {

            "Year":[2025,2026,2027],

            "Access":[53,55,57],

            "Digital Payment":[40,45,50]

            }

    )


    st.subheader(

    "Forecast Table"

    )


    st.dataframe(

        forecast

    )



#---------------------------------------------------
# Inclusion Projection
#---------------------------------------------------

elif page=="Inclusion Projections":



    st.title(

    "Inclusion Projections"

    )



    st.write(

    "Financial Inclusion Target : 60%"

    )


    fig,ax=plt.subplots()


    ax.plot(

            [2024,2025,2026,2027],

            [49,53,55,57],

            marker="o"

            )


    ax.axhline(

                y=60,

                linestyle="--"

                )


    ax.set_xlabel(

                "Year"

                )


    ax.set_ylabel(

                "Percentage"

                )


    ax.set_title(

                "Progress Toward 60% Target"

                )


    st.pyplot(fig)



    st.subheader(

    "Scenario Selection"

    )


    scenario=st.selectbox(

        "Choose Scenario",

        [

        "Base",

        "Optimistic",

        "Pessimistic"

        ]

    )


    st.write(

    "Selected Scenario :",

    scenario

    )



    #---------------------------------------

    # Download Forecast

    #---------------------------------------


    df=pd.DataFrame(

        {

        "Year":[2025,2026,2027],

        "Access":[53,55,57],

        "Digital Payment":[40,45,50]

        }

    )


    csv=df.to_csv(

            index=False

            ).encode()


    st.download_button(

            "Download Forecast Data",

            csv,

            "forecast.csv",

            "text/csv"

    )


#---------------------------------------------------
# Footer
#---------------------------------------------------

st.divider()


st.write(

"Developed for Forecasting Financial Inclusion in Ethiopia."

)