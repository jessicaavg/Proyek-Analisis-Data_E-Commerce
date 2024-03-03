import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title("Dashboard BRAZILIAN E-COMMERCE")

st.markdown(
    """
    <style>
    .reportview-container .main {
        max-width: 100%;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 3rem;
    }

    .stButton>button {
        width: 200px;

    .stColumn {
        margin: 0px 10px; 

    .stSubheader {
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)

#load dataset
data_customer = pd.read_csv('data/customers_dataset.csv')
data_geolocation = pd.read_csv('data/geolocation_data_true.csv')
data_order = pd.read_csv('data/order_data_true.csv')
data_items = pd.read_csv('data/order_items_data_true.csv')
data_order_payments = pd.read_csv('data/order_payments_dataset.csv')
data_order_reviews = pd.read_csv('data/order_reviews_data_true.csv')
data_product_category_name_translation = pd.read_csv('data/product_category_name_translation.csv')
data_products = pd.read_csv('data/products_data_true.csv')
data_sellers = pd.read_csv('data/sellers_dataset.csv')

###############################
##          SIDEBAR          ##
###############################
data_customer = pd.read_csv('data/customers_dataset.csv')
st.sidebar.button("View Data")

if st.sidebar.button('Visualization Data'):
    #VISUASLISASI 1
    # Data
    st.markdown("<h3 style='text-align: center;'>Jumlah Metode Pembayaran yang Digunakan dalam E-Commerce</h3>", unsafe_allow_html=True)
    st.subheader("")
    payment_method = ('boleto', 'credit_card', 'debit_card', 'not_defined', 'voucher')
    votes = (19784, 76795, 1529, 3, 5775)

    # Plotting untuk plot bar
    fig1, ax1 = plt.subplots()
    ax1.bar(x=payment_method, height=votes, color='#9DBC98')
    ax1.set_xlabel('Metode Pembayaran')
    ax1.set_ylabel('Jumlah Pengguna per Metode Pembayaran')

    # Menampilkan bar chart
    st.pyplot(fig1)
    st.caption("<h6 style='text-align: justify;'> Dari hasil visualisasi diatas, dapat dilihat bahwa metode pembayaran pada e-commerce brazilian ada 4, yaitu boleto, credit card, debit card, voucher, dan ada beberapa yang tidak diketahui. Metode pembayaran yang paling sering digunakan ketika berbelanja adalah credit card dengan jumlah pengguna sebanyak 76.795 orang.</h6>", unsafe_allow_html=True)
    st.subheader("")

    #VISUALISASI 2
    st.markdown("<h3 style='text-align: center;'>Perbandingan banyaknya pembelian dalam setiap tahun</h3>", unsafe_allow_html=True)

    year = ('Tahun 2016', 'Tahun 2017', 'Tahun 2018')
    votes = (272, 43354, 52835)
    color = ('#43766C', '#F6D6D6', '#C4DFDF')
    explode = (0, 0, 0)

    # Plotting untuk plot pie
    fig2, ax2 = plt.subplots()
    ax2.pie(
        x=votes,
        labels=year,
        autopct='%1.1f%%',
        colors=color,
        explode=explode
    )   

    # Menampilkan plot pie di Streamlit
    st.pyplot(fig2)
    st.caption("<h6 style='text-align: justify;'> Dari pie chart diatas, dapat dilihat bahwa pembelian yang paling banyak terdapat pada tahun 2018 sebanyak 54,8% dan pembelian tahun 2017 sebanyak 44,9%. Pembelian paling sedikit terdapat pada tahun 2016, yaitu sebanyak 0,3% dari keseluruhan catatan pembelian.</h6>", unsafe_allow_html=True)
    st.subheader("")

    #VISUALISASI 3
    st.markdown("<h3 style='text-align: center;'>Rata-Rata Jumlah Pembelian per Bulan Pada Tahun 2018</h3>", unsafe_allow_html=True)
    st.subheader("")

    order_data = pd.read_csv("order_data_true.csv")
    order_data['order_purchase_timestamp'] = pd.to_datetime(order_data['order_purchase_timestamp'])

    start_date = pd.to_datetime('2018-01-01')
    end_date = pd.to_datetime('2019-01-01')
    orders_2018 = order_data[(order_data['order_purchase_timestamp'] >= start_date) & (order_data['order_purchase_timestamp'] < end_date)]

    orders_2018['order_month'] = orders_2018['order_purchase_timestamp'].dt.month

    bulan_orders_2018 = orders_2018.groupby('order_month').size()

    rata_orders_per_month_2018 = bulan_orders_2018.mean()

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    bulan_orders_2018.plot(kind='bar', color='skyblue')
    plt.xlabel('Bulan (dalam angka)')
    plt.ylabel('Jumlah Pesanan')
    plt.xticks(rotation=0)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.axhline(rata_orders_per_month_2018, color='red', linestyle='--', linewidth=1.5, label='Rata-rata')
    plt.legend()

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    st.caption("<h6 style='text-align: justify;'>Dari grafik diatas, dapat dilihat bahwa rata-rata jumlah pembelian per bulan pada tahun 2018 secara signifikan tidak berbeda jauh. Rata-rata jumlah pembelian yang paling banyak terdapat pada bulan 1 (januari) dan paling sedikit pada bulan 6 (juni). Pada dataset hanya memiliki daftar pembelian hingga bulan ke-8 (agustus). Jika seandainya data pembelian lengkap hingga akhir tahun, tidak menutup kemungkinan di bulan berikutnya terjadi peningkatan pembelian yang melampaui banyaknya pembelian di bulan 1.</h6>", unsafe_allow_html=True)

else:
    select = st.selectbox("Select the data you want to display", ['Customers Data', 'Geolocation Data', 'Order Data', 'Order Items Data', 'Order Payment Data', 'Order Reviews Data', 'Category Product Name Translation Data', 'Product Data', 'Sellers Data'])
    if select == "Customers Data":
        st.subheader("Customer Data)")
        st.write(data_customer)
        
        def convert_custdf(data_customer):
            return data_customer.to_csv().encode('utf-8')
        
        csv_data_cust = convert_custdf(data_customer)

        st.download_button(
            label="Download Customer Data as CSV",
            data=csv_data_cust,
            file_name='Customers_Data.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )
    elif select == "Geolocation Data":
        st.subheader("Geolocation Data")
        st.write(data_geolocation)
        def convert_geodf(data_geolocation):
            return data_geolocation.to_csv().encode('utf-8')
        
        csv_data_geo = convert_geodf(data_geolocation)

        st.download_button(
            label="Download Geolocation Data as CSV",
            data=csv_data_geo,
            file_name='data_geolocation.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )

    elif select == "Order Data":
        st.subheader("Order Data")
        st.write(data_order)
        def convert_orderdf(data_order):
            return data_order.to_csv().encode('utf-8')
        
        csv_data_order = convert_orderdf(data_order)

        st.download_button(
            label="Download Order Data as CSV",
            data=csv_data_order,
            file_name='csv_data_order.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )
    elif select == "Order Items Data":
        st.subheader("Order Items Data")
        st.write(data_items)
        def convert_itemdf(data_items):
            return data_items.to_csv().encode('utf-8')
        
        csv_data_item = convert_itemdf(data_items)

        st.download_button(
            label="Download Items Data as CSV",
            data=csv_data_item,
            file_name='Customers_Data.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )
    elif select == "Order Payment Data":
        st.subheader("Order Payment Data")
        st.write(data_order_payments)
        def convert_paydf(data_order_payments):
            return data_order_payments.to_csv().encode('utf-8')
        
        csv_data_pay = convert_paydf(data_order_payments)

        st.download_button(
            label="Download Order Payment Data as CSV",
            data=csv_data_pay,
            file_name='data_order_payments.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )
    elif select == "Order Reviews Data":
        st.subheader("Order Reviews Data")
        st.write(data_order_reviews)
        def convert_revdf(data_order_reviews):
            return data_order_reviews.to_csv().encode('utf-8')
        
        csv_data_rev = convert_revdf(data_order_reviews)

        st.download_button(
            label="Download Order Reviews Data as CSV",
            data=csv_data_rev,
            file_name='data_order_reviews.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )
    elif select == "Category Product Name Translation Data":
        st.subheader("Category Product Name Translation Data")
        st.write(data_product_category_name_translation)
        def convert_catdf(data_product_category_name_translation):
            return data_product_category_name_translation.to_csv().encode('utf-8')
        
        csv_data_cat = convert_catdf(data_product_category_name_translation)

        st.download_button(
            label="Download Category Product Name Translation Data as CSV",
            data=csv_data_cat,
            file_name='data_product_category_name_translation.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )
    elif select == "Product Data":
        st.subheader("Product Data")
        st.write(data_products)
        def convert_proddf(data_products):
            return data_products.to_csv().encode('utf-8')
        
        csv_data_prod = convert_proddf(data_products)

        st.download_button(
            label="Download Product Data as CSV",
            data=csv_data_prod,
            file_name='data_products.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )
    elif select == "Sellers Data":
        st.subheader("Sellers Data")
        st.write(data_sellers)
        def convert_selldf(data_sellers):
            return data_sellers.to_csv().encode('utf-8')
        
        csv_data_sell= convert_selldf(data_sellers)

        st.download_button(
            label="Download Sellers Data as CSV",
            data=csv_data_sell,
            file_name='data_sellers.csv',
            mime='text/csv',
            help="Click to download the DataFrame as a CSV file."
        )

with open("E-Commerce_Public_Dataset.zip", "rb") as file:
    btn = st.sidebar.download_button(
            label="Download Full Dataset",
            data=file,
            file_name="E-Commerce_Public_Dataset.zip",
            mime="file/zip"
          )