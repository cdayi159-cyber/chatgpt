# USGS Earthquake Viewer

A Gradio application that visualizes recent earthquakes from the USGS Earthquake Catalog.

## Features

- Interactive world map using Folium
- Latest earthquake data from USGS GeoJSON feeds
- Ready for deployment to Hugging Face Spaces
- Automatic deployment via GitHub Actions

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

## Deployment

Push to the `main` branch. GitHub Actions will automatically deploy to the Hugging Face Space `cdayi159/space1`.

Configure the `HF_TOKEN` GitHub Actions secret with write access to the Space.
