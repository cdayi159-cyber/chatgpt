import requests
import pandas as pd
import folium
import gradio as gr

USGS={"Past Day":"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"}

def build_map():
    data=requests.get(USGS['Past Day'],timeout=30).json()
    m=folium.Map(location=[20,0],zoom_start=2,tiles='CartoDB positron')
    for f in data['features']:
        p=f['properties'];g=f['geometry']['coordinates']
        lon,lat,depth=g
        mag=p.get('mag') or 0
        folium.CircleMarker(location=[lat,lon],radius=max(3,mag*2),popup=f"{p.get('place')}<br>Mag {mag}",fill=True).add_to(m)
    return m._repr_html_()

demo=gr.Interface(fn=build_map,inputs=[],outputs=gr.HTML(),title='USGS Earthquake Viewer')

if __name__=='__main__':
    demo.launch()