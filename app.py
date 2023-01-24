import streamlit as st
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go


#---------------------------------#
# Page layout
# Page expands to full width
st.set_page_config(page_title='Sistem PTAS', layout='wide')


#---------------------------------#
# Build model
def build_model(df):
	m = Prophet(
        changepoint_prior_scale=0.5,
        seasonality_prior_scale=7.0,
        seasonality_mode='multiplicative'
	).fit(df)
	future = m.make_future_dataframe(periods=period, freq='h')
	forecast = m.predict(future)
    # Plot forecast
	st.write(f'Grafik prediksi tinggi sair sungai untuk {n_days} hari.')
	fig1 = plot_plotly(m, forecast, xlabel='Waktu', ylabel='Tinggi Air (m)')
	st.plotly_chart(fig1)

def plot_raw_data(df):
    df['ds'] = pd.to_datetime(df['ds'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], name="stock_open"))
    fig.layout.update(title_text='Grafik Tinggi Air Sungai', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


#---------------------------------#
# Sidebar - Collects user input features into dataframe
with st.sidebar.header('*Upload .csv file*'):
    uploaded_file = st.sidebar.file_uploader('*file .csv*', type=["csv"])
    st.sidebar.markdown("""
	[Contoh .csv *file*](https://github.com/AchmadRaihan/kalu-data/blob/main/kalu.csv)
	""")
# Sidebar - Days of prediction
n_days = st.sidebar.slider('Durasi Hari Prediksi:', 0, 7)
period = n_days * 24


#---------------------------------#
# Main panel
# Displays the dataset
st.write("""
# Sistem Prediksi Tinggi Air Sungai
*Dashboard* hasil prediksi tinggi air sungai.
""")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.markdown('**Hasil Prediksi Tinggi Air Sungai**')
    plot_raw_data(df)
    build_model(df)
else:
    st.info('Belum *upload* data untuk melihat hasil prediksi tinggi air sungai.')
    if st.button('Gunakan contoh *data set*'):
        df = pd.read_csv('kalu.csv')
        plot_raw_data(df)
        build_model(df)
