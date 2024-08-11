import pandas as pd 
import plotly.express as px
import streamlit as st   

# Set page configuration
st.set_page_config(
    page_title='Consoleflare Analytics Portal',
    page_icon='📊',
    layout='wide'
)

# Set custom CSS for dark theme and heading colors
st.markdown("""
    <style>
        /* Change the overall background color */
        .main {
            background-color: #0e1117;
        }

        /* Global text color */
        body, .css-18e3th9, .css-1aumxhk, .stDataFrame {
            color: #e0e0e0;
        }

        /* Specific header colors */
        h1, h2, h3 {
            color: #1f77b4; /* Blue color */
        }

        /* Specific paragraph colors */
        p {
            color: #ffffff; /* White color */
        }

        /* Streamlit widget labels (e.g., sliders, select boxes) */
        .css-1sbuyqj, .stSlider, .stSelectbox {
            color: #c5c5c5; /* Light grey */
        }

        /* Streamlit button text */
        .stButton button {
            color: #ffffff; /* White color */
        }
    </style>
""", unsafe_allow_html=True)

# Title and subheader
st.title('📊 Data Analytics Portal')
st.subheader('Explore Data with Ease.')
st.subheader('Authored by: DEBOJIT BASAK')

# File uploader
file = st.file_uploader('Drop CSV or Excel file', type=['csv', 'xlsx'])
if file:
    if file.name.endswith('csv'):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)   
    
    st.dataframe(data)
    st.info('File is successfully uploaded', icon='🚨')

    # Dataset basic information
    st.subheader('🔍 Basic Information of the Dataset')
    tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Top and Bottom Rows', 'Data Types', 'Columns'])

    with tab1:
        st.write(f'There are {data.shape[0]} rows and {data.shape[1]} columns in the dataset')
        st.subheader('📊 Statistical Summary')
        st.dataframe(data.describe())
    
    with tab2:
        st.subheader('📈 Top Rows')
        toprows = st.slider('Number of rows you want', 1, data.shape[0], key='topslider')
        st.dataframe(data.head(toprows))
        
        st.subheader('📉 Bottom Rows')
        bottomrows = st.slider('Number of rows you want', 1, data.shape[0], key='bottomslider')
        st.dataframe(data.tail(bottomrows))
    
    with tab3:
        st.subheader('📝 Data Types of Columns')
        st.dataframe(data.dtypes)
    
    with tab4:
        st.subheader('🔖 Column Names in Dataset')
        st.write(list(data.columns))
    
    # Column values count
    st.subheader('🔢 Column Values to Count')
    with st.expander('Value Count'):
        col1, col2 = st.columns(2)
        with col1:
            column = st.selectbox('Choose column name', options=list(data.columns))
        with col2:
            toprows = st.number_input('Top rows', min_value=1, step=1)
        
        if st.button('Count'):
            result = data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)
            
            st.subheader('📊 Visualization')
            fig = px.bar(data_frame=result, x=column, y='count', text='count', template='plotly_dark')
            st.plotly_chart(fig)
            
            fig = px.line(data_frame=result, x=column, y='count', text='count', template='plotly_dark')
            st.plotly_chart(fig)
            
            fig = px.pie(data_frame=result, names=column, values='count', template='plotly_dark')
            st.plotly_chart(fig)

    # Groupby feature
    st.subheader('📚 Groupby: Simplify Your Data Analysis')
    st.write('The groupby lets you summarize data by specific categories and groups')
    with st.expander('Group By your columns'):
        col1, col2, col3 = st.columns(3)
        with col1:
            groupby_cols = st.multiselect('Choose your columns to groupby', options=list(data.columns))
        with col2:
            operation_col = st.selectbox('Choose column for operation', options=list(data.columns))
        with col3:
            operation = st.selectbox('Choose operation', options=['sum', 'max', 'min', 'mean', 'median', 'count'])
        
        if groupby_cols:
            result = data.groupby(groupby_cols).agg(
                newcol=(operation_col, operation)
            ).reset_index()
            st.dataframe(result)

            st.subheader('📊 Data Visualization')
            graphs = st.selectbox('Choose your graph', options=['line', 'bar', 'scatter', 'pie', 'sunburst'])
            if graphs == 'line':
                x_axis = st.selectbox('Choose X axis', options=list(result.columns))
                y_axis = st.selectbox('Choose Y axis', options=list(result.columns))
                color = st.selectbox('Color Information', options=[None] + list(result.columns))
                fig = px.line(data_frame=result, x=x_axis, y=y_axis, color=color, markers=True, template='plotly_dark')
                st.plotly_chart(fig)
            elif graphs == 'bar':
                x_axis = st.selectbox('Choose X axis', options=list(result.columns))
                y_axis = st.selectbox('Choose Y axis', options=list(result.columns))
                color = st.selectbox('Color Information', options=[None] + list(result.columns))
                facet_col = st.selectbox('Column Information', options=[None] + list(result.columns))
                fig = px.bar(data_frame=result, x=x_axis, y=y_axis, color=color, facet_col=facet_col, barmode='group', template='plotly_dark')
                st.plotly_chart(fig)
            elif graphs == 'scatter':
                x_axis = st.selectbox('Choose X axis', options=list(result.columns))
                y_axis = st.selectbox('Choose Y axis', options=list(result.columns))
                color = st.selectbox('Color Information', options=[None] + list(result.columns))
                size = st.selectbox('Size Column', options=[None] + list(result.columns))
                fig = px.scatter(data_frame=result, x=x_axis, y=y_axis, color=color, size=size, template='plotly_dark')
                st.plotly_chart(fig)
            elif graphs == 'pie':
                values = st.selectbox('Choose Numerical Values', options=list(result.columns))
                names = st.selectbox('Choose Labels', options=list(result.columns))
                fig = px.pie(data_frame=result, values=values, names=names, template='plotly_dark')
                st.plotly_chart(fig)
            elif graphs == 'sunburst':
                path = st.multiselect('Choose your Path', options=list(result.columns))
                fig = px.sunburst(data_frame=result, path=path, values='newcol', template='plotly_dark')
                st.plotly_chart(fig)
