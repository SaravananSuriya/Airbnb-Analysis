import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd


img = Image.open('C:\\Users\\WELCOME\\OneDrive\\Desktop\\saravanan\\Visual_Studio_Code\\images\\00-featured-airbnb-pink-logomark.jpg')
st.set_page_config(page_title = 'Airbnb Analysis', page_icon = img, layout = 'wide')

selected = option_menu('Airbnb Analysis', ["Home","About","Analysis","Map"], 
    icons=['house',"display", "bar-chart-fill","map-fill"], 
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
    hide = """
        <style>
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide,unsafe_allow_html = True)
    st.stop()


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
    hide = """
        <style>
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide,unsafe_allow_html = True)
    st.stop()


elif selected == "Analysis":
    df = pd.read_csv("AB1_NYC_2019.csv")
    st.sidebar.markdown("# :rainbow[Select an option to Filter:]")
    neigh_group = st.sidebar.multiselect(
        ":white[**Select the Neighbourhood Group:**]",
        options = df['neighbourhood_group'].unique(),
        default = df['neighbourhood_group'].unique()
    )
    st.sidebar.markdown("")
    Neighbourhood = st.sidebar.multiselect(
        ":white[**Select the Neighbourhood:**]",
        options = df['neighbourhood'].unique(),
        default = ['Williamsburg','Bedford-Stuyvesant','Harlem','Bushwick','Upper West Side',"Hell's Kitchen",'East Village','Upper East Side','Crown Heights','Midtown','East Harlem','Greenpoint','Chelsea','Lower East Side','Astoria']
    )


    st.markdown("# Neighbourhood Group vs Number of properties listed")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    count = df.groupby('neighbourhood_group').count() 
    specific_row = count.loc[neigh_group]
    result = specific_row.reset_index()
    with column2:
        data_frame = pd.DataFrame(result, columns=['neighbourhood_group', 'id'])
        data_frame.columns = ['Neighbourhood Group', 'Number of Properties']
        with st.expander("",expanded=False):
            st.dataframe(data_frame.style.background_gradient(cmap='Oranges'),use_container_width=True)
    bar = px.bar(specific_row, x = neigh_group,y = 'number_of_reviews',labels={'x': 'Neighbourhood Group', 'number_of_reviews':'Number of Properties'},height = 600)
    st.plotly_chart(bar)

    st.markdown("# Neighbourhood vs Number of properties listed")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    count = df.groupby('neighbourhood').count()
    specific_row = count.loc[Neighbourhood]
    result = specific_row.reset_index()
    with column2:
        data_frame = pd.DataFrame(result, columns=['neighbourhood', 'id'])
        data_frame.columns = ['Neighbourhood', 'Number of Properties']
        with st.expander("",expanded=False):
            st.dataframe(data_frame.style.background_gradient(cmap='turbo'),use_container_width=True)
    bar = px.bar(specific_row, x = Neighbourhood,y = 'number_of_reviews',labels={'x': 'Neighbourhood', 'number_of_reviews':'Number of Properties'},height = 600,width=1000)
    st.plotly_chart(bar)

    
    st.markdown("# Host vs Number of Property List")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    group_by = df.groupby('host_name').count()
    grouped_df = group_by.reset_index()
    top_10_rows = grouped_df.nlargest(10, 'availability_365')
    top_10_rows = top_10_rows.reset_index(drop=True)
    with column2:
        with st.expander("",expanded=False):
            data_frame = pd.DataFrame(top_10_rows, columns=['host_name', 'id'])
            data_frame.columns = ['Host Name', 'Number of Properties']
            st.dataframe(data_frame.style.background_gradient(cmap='pink'),use_container_width=True)
    bar1 = px.bar(top_10_rows, x = 'host_name',y = 'availability_365',height = 600,labels={'host_name':'Host Name', 'availability_365':'Number of Properties'},width=1000)
    st.plotly_chart(bar1)

    
    st.markdown("# Host contain maximum count of Properties in specific Neighbourhood Group")
    option = st.selectbox(':red[**Select any Neighbourhood Group to Explore:**]',options = ['Brooklyn','Manhattan','Queens','Staten Island','Bronx'])
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    specific_groups = df[df['neighbourhood_group'] == option]
    grouped_df = specific_groups.groupby('host_name').count()
    result = grouped_df.reset_index()
    top_5_rows = result.nlargest(5, 'availability_365')
    data_frame = pd.DataFrame(top_5_rows, columns=['host_name', 'availability_365'])
    data_frame.columns = ['Host Name', 'Number of Properties']
    result1 = data_frame.reset_index()
    result1 = result1.drop('index', axis=1)
    with column2:
        with st.expander("",expanded=False):
            st.dataframe(result1.style.background_gradient(cmap='summer'),use_container_width=True)
    bar2 = px.bar(top_5_rows, x = 'host_name',y = 'availability_365',height = 600,labels={'host_name':'Host Name', 'availability_365':'Number of Properties'},title = f'Neighbourhood Group : {option}')
    st.plotly_chart(bar2)

    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    df1 = df[['room_type','price']]
    Max = df1.groupby('room_type')['price'].sum()
    result = Max.reset_index()
    column1,column2 = st.columns([2,2], gap = 'small')
    with column1:  
        st.markdown("# Room Type vs Total Price")
        with st.expander("",expanded=False):
            st.dataframe(result.style.background_gradient(cmap='cividis'),use_container_width=True) #use_container_width=True
        bar3 = px.bar(result, x = 'room_type',y = 'price',labels={'room_type':'Room Type', 'price':'Total Price'},text_auto=True,width=500)
        bar3.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(bar3)
    with column2:
        st.markdown("# Room Type vs Total Count")
        group_by = df1.groupby('room_type').count().reset_index()
        group_by.columns = ['Room Type', 'Count']
        with st.expander("",expanded=False):
            st.dataframe(group_by.style.background_gradient(cmap='cividis'),use_container_width=True)
        bar3 = px.bar(group_by, x = 'Room Type',y = 'Count',text_auto=True,width=500)
        bar3.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(bar3)


    st.markdown("# Room Type vs Average Price")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    df1 = df[['room_type','price']]
    count = df1.groupby('room_type').mean()
    result = count.reset_index()
    with column2:
        data_frame = pd.DataFrame(result, columns=['room_type', 'price'])
        data_frame.columns = ['Room Type', 'Price']
        with st.expander("",expanded=False):
            st.dataframe(data_frame.style.background_gradient(cmap='coolwarm'),use_container_width=True)
    bar = px.bar(result, x = 'room_type',y = 'price',labels={'x': 'Room Type', 'price':'Average Price'},height = 600)
    st.plotly_chart(bar)


    st.markdown("# Neighbourhood Group vs Average Price")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    df1 = df[['neighbourhood_group','price']]
    count = df1.groupby('neighbourhood_group').mean()
    specific_row = count.loc[neigh_group]
    result = specific_row.reset_index()
    with column2:
        data_frame = pd.DataFrame(result, columns=['neighbourhood_group', 'price'])
        data_frame.columns = ['Neighbourhood Group', 'Price']
        with st.expander("",expanded=False):
            st.dataframe(data_frame.style.background_gradient(cmap='binary'),use_container_width=True)
    bar = px.bar(specific_row, x = neigh_group,y = 'price',labels={'x': 'Neighbourhood Group', 'price':'Average Price'},height = 600)
    st.plotly_chart(bar)

    st.markdown("# Room Type vs Price")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    box = px.box(df,x = 'room_type', y = 'price', color = 'room_type')
    st.plotly_chart(box)

    st.markdown("# Neighbourhood Group vs Price")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    box = px.box(df,x = 'neighbourhood_group', y = 'price', color = 'neighbourhood_group')
    st.plotly_chart(box)


    st.markdown("# Neighbourhood vs Average Price")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    df1 = df[['neighbourhood','price']]
    count = df1.groupby('neighbourhood').mean()
    specific_row = count.loc[Neighbourhood]
    result = specific_row.reset_index()
    with column2:
        data_frame = pd.DataFrame(result, columns=['neighbourhood', 'price'])
        data_frame.columns = ['Neighbourhood', 'Average Price']
        with st.expander("",expanded=False):
            st.dataframe(data_frame.style.background_gradient(cmap='Wistia'),use_container_width=True)
    bar = px.bar(specific_row, x = Neighbourhood,y = 'price',labels={'x': 'Neighbourhood', 'price':'Average Price'},height = 600,width=1000)
    st.plotly_chart(bar)


    st.markdown("# Neighbourhood Group / Room Type vs Average Price")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    df1 = df[['neighbourhood_group','price','room_type']]
    grouped_df = df1.groupby(['neighbourhood_group', 'room_type']).mean().reset_index()
    with column2:
        with st.expander("",expanded=False):
            st.dataframe(grouped_df.style.background_gradient(cmap='Reds'),use_container_width=True)
    hist = px.histogram(grouped_df, x="neighbourhood_group", y="price",color='room_type', barmode='group',height=550,width=1100,color_discrete_sequence=px.colors.qualitative.Pastel,labels={'neighbourhood_group':'Neighbourhood Group', 'price':'Average Price'})
    st.plotly_chart(hist)

    column1,column2 = st.columns([2,2], gap = 'small')
    with column1:
        st.markdown("# Neighbourhood group vs Number of reviews")
        df1 = df[['neighbourhood_group','number_of_reviews']]
        grouped_df = df1.groupby(['neighbourhood_group']).count()
        specific_row = grouped_df.loc[neigh_group]
        result = specific_row.reset_index()
        data_frame = pd.DataFrame(result, columns=['neighbourhood_group', 'number_of_reviews'])
        data_frame.columns = ['Neighbourhood Group', 'Number of Reviews']
        with st.expander("",expanded=False):
            st.dataframe(data_frame.style.background_gradient(cmap='Purples'),use_container_width=True)
        bar = px.pie(specific_row, names = neigh_group,values = 'number_of_reviews',labels={'x': 'Neighbourhood Group', 'number_of_reviews':'Number of Properties'},width = 500,hole=0.3)
        st.plotly_chart(bar)
    with column2:
        st.markdown("# Room Type contain Number of reviews")
        df1 = df[['room_type','number_of_reviews']]
        grouped_df = df1.groupby(['room_type']).sum().reset_index()
        with st.expander("",expanded=False):
            st.dataframe(grouped_df.style.background_gradient(cmap='Purples'),use_container_width=True,width=350)
        pie1 = px.pie(df,names='room_type',values='number_of_reviews',hole=0.3,width=500)
        st.plotly_chart(pie1)

    st.markdown("# Preferred Room Type in all Neighbourhood Group based on Reviews")
    hist = px.histogram(df, x="neighbourhood_group", y="number_of_reviews",color='room_type', barmode='group',height=550,width=1100,color_discrete_sequence=px.colors.qualitative.G10,labels={'neighbourhood_group':'Neighbourhood Group'})
    st.plotly_chart(hist)
    
    st.markdown("# Room Type vs Availability of 365 Days")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    df1 = df[['neighbourhood_group','availability_365','room_type']]
    grouped_df = df1.groupby(['neighbourhood_group', 'room_type']).mean().reset_index()
    with column2:
        with st.expander("",expanded=False):
            st.dataframe(grouped_df.style.background_gradient(cmap='Greys'),use_container_width=True)
    hist = px.histogram(grouped_df, x="neighbourhood_group", y="availability_365",color='room_type', barmode='group',height=550,width=1100,labels={'neighbourhood_group':'Neighbourhood Group'})
    st.plotly_chart(hist)

    st.markdown("# List of Busiest Host")
    df1 = df[['host_name', 'availability_365', 'neighbourhood_group', 'neighbourhood']]
    grouped_df = df1.groupby(['host_name', 'neighbourhood_group', 'neighbourhood']).sum()
    result = grouped_df.reset_index()
    bottom_50_rows = result.nsmallest(100, 'availability_365')
    bottom_50_rows = bottom_50_rows.reset_index(drop=True)
    with st.expander("Table of Busiest host"):
        table = ff.create_table(bottom_50_rows,colorscale = 'hot')
        st.plotly_chart(table,use_container_width=True)

    st.markdown("# Which Property has maximum Number of Reviews")
    df1 = df[['host_name', 'number_of_reviews', 'neighbourhood_group', 'neighbourhood','name']]
    grouped_df = df1.groupby(['host_name', 'neighbourhood_group', 'neighbourhood','name']).sum()
    result = grouped_df.reset_index()
    bottom_50_rows = result.nlargest(10, 'number_of_reviews')
    bottom_50_rows = bottom_50_rows.reset_index(drop=True)
    with st.expander(""):
        st.dataframe(bottom_50_rows.style.background_gradient(cmap='Greens'))
    hist = px.histogram(bottom_50_rows, x="name", y="number_of_reviews",color='neighbourhood_group', barmode='group',height=550,width=1100,color_discrete_sequence=px.colors.qualitative.Plotly_r)
    st.plotly_chart(hist)

    st.markdown("# minimum nights guest stay at an airbnb")
    column1,column2,column3 = st.columns([0.5,2,2], gap = 'small')
    grouped_df = df.groupby('minimum_nights').count().reset_index()
    bottom_50_rows = grouped_df.nlargest(20, 'id').reset_index()
    data_frame = pd.DataFrame(bottom_50_rows, columns=['minimum_nights', 'id'])
    data_frame.columns = ['Minimum Nights', 'Count']
    with column2:
        with st.expander(""):
            st.dataframe(data_frame.style.background_gradient(cmap='Blues'),use_container_width=True,width=350)
    pie = px.pie(data_frame,names='Minimum Nights',values='Count',width=800)
    st.plotly_chart(pie)

    hide = """
        <style>
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide,unsafe_allow_html = True)
    st.stop()


elif selected == "Map":
    hide = """
        <style>
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide,unsafe_allow_html = True)
    
    df = pd.read_csv("AB1_NYC_2019.csv")
    st.sidebar.markdown("# :rainbow[Select an option to Filter:]")
    neigh_group = st.sidebar.selectbox(
        ":white[**Select the Neighbourhood Group:**]",
        options = df['neighbourhood_group'].unique(),
    )
    st.sidebar.markdown("")
    Neighbourhood = st.sidebar.multiselect(
        ":white[**Select the Neighbourhood:**]",
        options = df['neighbourhood'].unique(),
        default = ['Williamsburg','Bedford-Stuyvesant','Harlem','Bushwick','Upper West Side']
    )
    st.sidebar.markdown("")
    room = st.sidebar.selectbox(
        ":white[**Select the Room Type:**]",
        options = df['room_type'].unique(),
    )


    
    choice = st.selectbox('',options = ['All Locations of Airbnb in Map View','Price Analysis with specific Neighbourhood Group','Price Analysis with specific Neighbourhood','Price Analysis with specific Room Type','Number of Reviews with specific Neighbourhood Group','Checking Availability of days with specific Neighbourhood Group','Minimum Nigths staying in Airbnb Hotel with specific Neighbourhood Group','Host Listing count in specific neighbourhood group'])
    
    if choice == 'All Locations of Airbnb in Map View':
        st.markdown("# All Locations of Airbnb in Map View")
        fig = px.scatter_mapbox(df,lat = 'latitude',lon='longitude',zoom=9.3,width=1100,height=600,hover_data='neighbourhood',hover_name='neighbourhood_group',text='name')
        fig.update_layout(mapbox_style='carto-darkmatter')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        st.stop()

    elif choice == 'Price Analysis with specific Neighbourhood Group':
        st.markdown("# Price Analysis with specific Neighbourhood Group")
        df1 = df.query(f"neighbourhood_group == '{neigh_group}'")
        fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=10,color='price',width=1100,height=600,color_continuous_scale='jet',size = 'price',size_max=50,hover_data='neighbourhood',hover_name='name',title = f'Neighbourhood Group : {neigh_group}',text='room_type')
        fig.update_layout(mapbox_style='carto-positron')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        st.stop()

    elif choice == 'Price Analysis with specific Neighbourhood':
        st.markdown("# Price Analysis with specific Neighbourhood")
        df1 = df.query(f"neighbourhood == {Neighbourhood}")
        fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=10,color='neighbourhood',width=1100,height=600,color_continuous_scale='jet',size = 'price',size_max=50,hover_name='name',text='neighbourhood_group')
        fig.update_layout(mapbox_style='carto-darkmatter')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        st.stop()

    elif choice == 'Price Analysis with specific Room Type':
        st.markdown("# Price Analysis with specific Room Type")
        df1 = df.query(f"room_type == '{room}'")
        fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=9.3,color='price',width=1100,height=600,size = 'price',size_max=50,text='neighbourhood_group',hover_name='name',hover_data='neighbourhood',title = f'Room Type : {room}',color_continuous_scale='jet')
        fig.update_layout(mapbox_style='carto-darkmatter')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        st.stop()

    elif choice == 'Number of Reviews with specific Neighbourhood Group':
        st.markdown("# Number of Reviews with specific Neighbourhood Group")
        df1 = df.query(f"neighbourhood_group == '{neigh_group}'")
        fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=10,color='number_of_reviews',width=1150,height=600,color_continuous_scale='jet',size = 'number_of_reviews',size_max=50,hover_data='neighbourhood',hover_name='name',title = f'Neighbourhood Group : {neigh_group}',text='room_type')
        fig.update_layout(mapbox_style='carto-positron')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        st.stop()

    elif choice == 'Checking Availability of days with specific Neighbourhood Group':
        st.markdown("# Checking Availability of days with specific Neighbourhood Group")
        df1 = df.query(f"neighbourhood_group == '{neigh_group}'")
        fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=10,color='availability_365',width=1150,height=600,color_continuous_scale='jet',size = 'availability_365',hover_data='neighbourhood',hover_name='name',title = f'Neighbourhood Group : {neigh_group}',text='room_type',size_max=10)
        fig.update_layout(mapbox_style='carto-positron')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        st.stop()
    
    elif choice == 'Minimum Nigths staying in Airbnb Hotel with specific Neighbourhood Group':
        st.markdown("# Minimum Nigths staying in Airbnb Hotel with specific Neighbourhood Group")
        df1 = df.query(f"neighbourhood_group == '{neigh_group}'")
        fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=10,color='minimum_nights',width=1150,height=600,color_continuous_scale='jet',size = 'minimum_nights',hover_data='neighbourhood',hover_name='name',title = f'Neighbourhood Group : {neigh_group}',text='room_type',size_max=30)
        fig.update_layout(mapbox_style='carto-positron')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        st.stop()

    elif choice == 'Host Listing count in specific neighbourhood group':
        st.markdown("# Host Listing count in specific neighbourhood group")
        df1 = df.query(f"neighbourhood_group == '{neigh_group}'")
        fig = px.scatter_mapbox(df1,lat='latitude',lon='longitude',zoom=10,color='calculated_host_listings_count',width=1150,height=600,color_continuous_scale='jet',size = 'calculated_host_listings_count',hover_data='neighbourhood',hover_name='host_name',title = f'Neighbourhood Group : {neigh_group}',text='name',size_max=35)
        fig.update_layout(mapbox_style='carto-positron')
        fig.update_layout(margin={'r':0,'t':50,'l':0,'b':10})
        fig.update_geos(fitbounds="locations")
        st.plotly_chart(fig)
        fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
          ])
        st.stop()
