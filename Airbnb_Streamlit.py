import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px
from st_aggrid import AgGrid
import pandas as pd
import numpy as np
import json

img = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\00-featured-airbnb-pink-logomark.jpg')
st.set_page_config(page_title = 'Airbnb Analysis', page_icon = img, layout = 'wide')

selected = option_menu('Airbnb Analysis', ["Home","About","Analysis"], 
    icons=['house',"display", "bar-chart-fill"], 
    menu_icon='buildings-fill', default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#000000"}, # #008080
        "icon": {"color": "violet", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "center", "margin":"0px", "--hover-color": "#808080"},
        "nav-link-selected": {"background-color": "#808080"},
    }
)

if selected == 'Home':
    st.markdown("# :red[Project Title:]")
    st.markdown("## :black[&nbsp; &nbsp; &nbsp; &nbsp; Airbnb Analysis]")
    st.markdown("# :red[Skills take away From This Project:]")
    st.markdown("## :black[&nbsp; &nbsp; &nbsp; &nbsp; Python scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb]")
    st.markdown("# :red[Domain:]")
    st.markdown("## :black[&nbsp; &nbsp; &nbsp; &nbsp; Travel Industry, Property Management and Tourism.]")
    st.markdown("# :red[Problem Statement:]")
    st.markdown("## :black[&nbsp; &nbsp; &nbsp; &nbsp; This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.]")

elif selected == 'About':
    column1,column2,column3 = st.columns([2,4,2], gap = 'large')
    with column2:
        img = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\airbnb_logo_detail.jpg')
        st.image(img)
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    column1,column2 = st.columns([2,2], gap = 'large')
    with column1:
        img = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\airbnb%20luxe.webp')
        st.image(img)
    with column2:
        url = "https://www.airbnb.co.in/help/article/221/"
        st.markdown("## :red[Airbnb began in 2008 when two designers who had space to share hosted three travelers looking for a place to stay. Now, millions of Hosts and guests have created [free Airbnb accounts](%s) to enjoy each other's unique view of the world. You can host anything, anywhere, so guests can enjoy everything, everywhere. ]"% url)
    st.markdown("# :black[How Airbnb Working:]")        
    st.markdown("## :red[&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Airbnb is an online marketplace that connects people who want to rent out their property with people who are looking for accommodations, typically for short stays. Airbnb offers hosts a relatively easy way to earn some income from their property.]")

elif selected == "Analysis":
    st.sidebar.markdown("# :rainbow[Select an option to Filter:]")
    df = pd.read_csv("AB1_NYC_2019.csv")
    st.dataframe(df.head(10))
    # with side_bar:
    #     st.title("this is analysis part")
    # df = pd.read_csv("AB1_NYC_2019.csv")
    # st.dataframe(df.head(10))
    neigh_group = st.sidebar.multiselect(
        ":red[**Select the Neighbourhood Group:**]",
        options = df['neighbourhood_group'].unique(),
        default = df['neighbourhood_group'].unique()
    )

    df1 = df[['neighbourhood_group','calculated_host_listings_count']]
    group_by = df1.groupby('neighbourhood_group').sum()
    # st.dataframe(df1)
    # st.dataframe(group_by)
    count = df.groupby('neighbourhood_group').count()
    # st.dataframe(count)
    specific_row = count.loc[neigh_group]
    # st.dataframe(specific_row)
    st.markdown("# Neighbourhood Group vs Number of properties listed")
    bar = px.bar(specific_row, x = neigh_group,y = 'number_of_reviews',labels={'x': 'Neighbourhood Group', 'number_of_reviews':'Number of Properties'},height = 600)
    st.plotly_chart(bar)

    group_by = df.groupby('host_name').count()
    grouped_df = group_by.reset_index()
    top_10_rows = grouped_df.nlargest(10, 'availability_365')
    # st.dataframe(top_10_rows)
    st.markdown("# Host vs Number of Property List")
    bar1 = px.bar(top_10_rows, x = 'host_name',y = 'availability_365',height = 600,labels={'host_name':'Host Name', 'availability_365':'Number of Properties'})
    st.plotly_chart(bar1)

    
    st.markdown("# Host contain maximum count of Properties in specific Neighbourhood Group")
    option = st.selectbox(':red[**Select any Neighbourhood Group to Explore:**]',options = ['Brooklyn','Manhattan','Queens','Staten Island','Bronx'])
    specific_groups = df[df['neighbourhood_group'] == option]
    grouped_df = specific_groups.groupby('host_name').count()
    result = grouped_df.reset_index()
    top_5_rows = result.nlargest(5, 'availability_365')
    data_frame = pd.DataFrame(top_5_rows, columns=['host_name', 'availability_365'])
    data_frame.columns = ['Host Name', 'Number of Properties']
    result1 = data_frame.reset_index()
    result1 = result1.drop('index', axis=1)
    st.write(result1.style.background_gradient(cmap='Oranges'))
    # st.dataframe(specific_groups)
    # st.dataframe(grouped_df)
    # st.dataframe(result)
    # st.dataframe(top_5_rows)
    bar2 = px.bar(top_5_rows, x = 'host_name',y = 'availability_365',height = 600,labels={'host_name':'Host Name', 'availability_365':'Number of Properties'},title = f'Neighbourhood Group : {option}')
    st.plotly_chart(bar2)

    st.markdown("# Room Type vs Total Price")
    df1 = df[['room_type','price']]
    # df1['price'] = df1['price'].map('${:.2f}'.format)
    # st.dataframe(df1)
    Max = df1.groupby('room_type')['price'].sum()
    max_indexes = df1.groupby('room_type')['price'].sum().map('${:.2f}'.format)
    result = max_indexes.reset_index()
    result1 = Max.reset_index()
    # max_indexes['price'] = max_indexes['price'].map('${:.2f}'.format)
    # st.dataframe(result)
    st.dataframe(result1.style.background_gradient(cmap='Oranges'))
    # max_rows = df1.loc[max_indexes]
    # st.dataframe(max_rows)
    bar3 = px.bar(result, x = 'room_type',y = 'price',labels={'room_type':'Room Type', 'price':'Tota Price'},text_auto=True)
    bar3.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(bar3)

    st.markdown("# Neighbourhood Group / Room Type vs Price")
    # st.dataframe(df)
    hist = px.histogram(df, x="neighbourhood_group", y="price",color='room_type', barmode='group',height=550,width=1200,color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(hist)

    st.markdown("# Preferred Room Type in all Neighbourhood Group based on Reviews")
    hist = px.histogram(df, x="neighbourhood_group", y="number_of_reviews",color='room_type', barmode='group',height=550,width=1200,color_discrete_sequence=px.colors.qualitative.G10)
    st.plotly_chart(hist)
    
    df1 = df[['neighbourhood_group','availability_365','room_type']]
    grouped_df = df1.groupby(['neighbourhood_group', 'room_type']).mean().reset_index()
    # st.dataframe(grouped_df)
    st.markdown("# Room Type vs Availability of 365 Days")
    hist = px.histogram(grouped_df, x="neighbourhood_group", y="availability_365",color='room_type', barmode='group',height=550,width=1200)
    st.plotly_chart(hist)

    st.markdown("# List of Busiest Host")
    df1 = df[['host_name', 'availability_365', 'neighbourhood_group', 'neighbourhood']]
    grouped_df = df1.groupby(['host_name', 'neighbourhood_group', 'neighbourhood']).sum()
    result = grouped_df.reset_index()
    bottom_50_rows = result.nsmallest(1000, 'availability_365')
    bottom_50_rows = bottom_50_rows.reset_index(drop=True)
    st.dataframe(bottom_50_rows,use_container_width=True)

    st.markdown("# Which Property has maximum Number of Reviews")
    df1 = df[['host_name', 'number_of_reviews', 'neighbourhood_group', 'neighbourhood','name']]
    grouped_df = df1.groupby(['host_name', 'neighbourhood_group', 'neighbourhood','name']).sum()
    result = grouped_df.reset_index()
    bottom_50_rows = result.nlargest(10, 'number_of_reviews')
    bottom_50_rows = bottom_50_rows.reset_index(drop=True)
    st.dataframe(bottom_50_rows,use_container_width=True)
    hist = px.histogram(bottom_50_rows, x="name", y="number_of_reviews",color='neighbourhood_group', barmode='group',height=550,width=1200,color_discrete_sequence=px.colors.qualitative.Plotly_r)
    st.plotly_chart(hist)
    
    
    



    # 'Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 
    # 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens', 
    # 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 
    # 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 
    # 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 
    # 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 
    # 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 
    # 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 
    # 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 
    # 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 
    # 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 
    # 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 
    # 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 
    # 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'hot', 'hot_r', 'hsv', 
    # 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r',
    # 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 
    # 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 
    # 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 
    # 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 
    # 'winter_r'