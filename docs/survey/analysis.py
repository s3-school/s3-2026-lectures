import marimo

__version__ = "0.8.0"
_narrative_ = ""

app = marimo.App()


@app.cell
def __():
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    import folium
    from folium.plugins import MarkerCluster, HeatMap
    import re
    import marimo as mo
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import io
    import base64
    from datetime import datetime
    
    return pd, np, go, px, make_subplots, folium, MarkerCluster, HeatMap, re, mo, WordCloud, plt, io, base64, datetime


@app.cell
def __(pd):
    # Load data
    file_path = '20260115_results-survey995216.csv'
    df = pd.read_csv(file_path, sep=',', encoding='utf-8')
    
    # Replace MacOS with iOS in operating system column
    os_col = [col for col in df.columns if 'G02Q01' in col and 'other' not in col.lower()]
    os_other_col = [col for col in df.columns if 'G02Q01' in col and 'other' in col.lower()]
    if os_col:
        df[os_col[0]] = df[os_col[0]].replace(['MacOS', 'macOS', 'Mac OS', 'macos'], 'iOS')
    if os_col and os_other_col:
        other_series = df[os_other_col[0]].fillna('').astype(str)
        mac_mask = other_series.str.contains(r"mac\s?os|macos|osx|mac", case=False, regex=True)
        df.loc[(df[os_col[0]] == 'Other') & mac_mask, os_col[0]] = 'iOS'
    
    return df, file_path


@app.cell
def __(mo):
    mo.md(f"""
    # 📊S3-School - Preschool Survey
    """)


@app.cell
def __(df, mo):
    # Dataset Overview
    mo.md(f"""    
    **Number of responses**: {len(df)}\n
    **Date of analysis**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n
    ---
    """)


@app.cell
def __(df):
    # Extract question columns
    question_cols = [col for col in df.columns if any(q in col for q in ['G01Q01', 'G01Q02', 'G01Q03', 'G01Q06', 'G01Q07', 'oscars', 'G02Q01', 'G02Q02',])]
    
    # Filter main questions
    main_questions = [col for col in question_cols if '[SQ' not in col and '[other]' not in col]
    
    # Remove duplicates
    seen = set()
    unique_questions = []
    for _col in main_questions:
        base_col = _col.split('[')[0]
        if base_col not in seen:
            seen.add(base_col)
            unique_questions.append(_col)
    
    return question_cols, main_questions, unique_questions


# @app.cell
# def __(mo):
#     mo.md("""
#     ## 📋 Questionnaire Visualizations
#     """)


@app.cell
def __(df, unique_questions, px, pd, go, mo):
    # Create plots for all questions
    plots = []
    palette = px.colors.qualitative.Set2
    sequential = px.colors.sequential.Blues
    
    for question_col in unique_questions:
        # Extract question text
        if '. ' in question_col:
            question_text = question_col.split('. ', 1)[1]
        else:
            question_text = question_col
        
        if '[' in question_text:
            question_text = question_text.split('[')[0]
        
        # Get data
        _data = df[question_col].dropna()
        
        if len(_data) > 0:
            n_unique = _data.nunique()
            is_numeric = pd.api.types.is_numeric_dtype(_data)
            is_python_level = 'Python' in question_text and ('level' in question_text.lower() or 'niveau' in question_text.lower())
            is_age_group = 'age group' in question_text.lower() or 'G01Q01' in question_col
            
            if is_numeric and n_unique > 10:
                # Histogram for continuous data
                fig = px.histogram(_data, nbins=30, title=question_text,
                                 labels={'value': 'Value', 'count': 'Frequency'},
                                 color_discrete_sequence=sequential)
                fig.update_traces(showlegend=False)
                fig.update_layout(hovermode='x unified', height=500)
                
            elif is_python_level and is_numeric:
                # Python level histogram (1-10)
                value_counts = _data.value_counts().reindex(range(1, 11), fill_value=0).sort_index()
                level_colors = [sequential[min(i, len(sequential)-1)] for i in range(len(value_counts))]
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=value_counts.index,
                    y=value_counts.values,
                    text=value_counts.values,
                    textposition='auto',
                    marker=dict(color=level_colors),
                    hovertemplate='<b>Niveau: %{x}</b><br>Réponses: %{y}<extra></extra>'
                ))
                
                fig.update_layout(
                    title=question_text,
                    xaxis_title='Python Level',
                    yaxis_title='Count',
                    height=500,
                    hovermode='x unified',
                    showlegend=False
                )
                
            elif is_age_group:
                # Age group bar chart with custom order
                age_order = ["< 21", "21 - 25", "26-30", "31-35", "36-40", "> 40"]
                value_counts = _data.value_counts()
                # Reindex to ensure proper order, filling missing categories with 0
                value_counts = value_counts.reindex([age for age in age_order if age in value_counts.index])
                bar_colors = [palette[i % len(palette)] for i in range(len(value_counts))]
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=value_counts.index,
                    y=value_counts.values,
                    marker_color=bar_colors,
                    text=value_counts.values,
                    textposition='auto',
                ))
                fig.update_layout(
                    title=question_text,
                    xaxis_title='Age Group',
                    yaxis_title='Count',
                    hovermode='x unified',
                    height=500,
                    showlegend=False
                )
                
            else:
                # Bar chart for categorical data
                value_counts = _data.value_counts().sort_values(ascending=False)
                bar_colors = [palette[i % len(palette)] for i in range(len(value_counts))]
                fig = go.Figure()
                fig.add_trace(go.Bar(
                    x=value_counts.index,
                    y=value_counts.values,
                    marker_color=bar_colors,
                    text=value_counts.values,
                    textposition='auto',
                ))
                fig.update_layout(
                    title=question_text,
                    xaxis_title='Response',
                    yaxis_title='Count',
                    hovermode='x unified',
                    height=500,
                    showlegend=False
                )
                fig.update_layout(hovermode='x unified', height=500)
                fig.update_xaxes(tickangle=45)
            
            fig.update_layout(
                font=dict(size=11),
                margin=dict(l=50, r=50, t=80, b=80),
                plot_bgcolor='#f8f9fa',
                paper_bgcolor='white',
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=True, gridwidth=1, gridcolor='#e0e0e0')
            )
            
            plots.append(fig)
    
    return plots


@app.cell
def __(plots, mo):
    mo.vstack(plots) if plots else mo.md("No plots to display")


@app.cell
def __(mo):
    mo.md("""
    ---
    
    ## ☁️ Science Domain Word Cloud
    """)


@app.cell
def __(df, WordCloud, plt, io, base64, mo):
    # Create word cloud for domain question
    domain_col = [col for col in df.columns if 'domain' in col.lower()][0]
    domain_data = df[domain_col].dropna()
    
    if len(domain_data) > 0:
        # Keep each full response intact by using frequencies rather than splitting words
        freq = domain_data.astype(str).str.strip().value_counts().to_dict()
        
        # Generate word cloud
        wordcloud = WordCloud(
            width=800, 
            height=400, 
            background_color='white',
            colormap='Blues',
            relative_scaling=0.5,
            min_font_size=10
        ).generate_from_frequencies(freq)
        
        # Create matplotlib figure
        fig_wc, ax = plt.subplots(figsize=(12, 6))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        # ax.set_title('Science Domains Word Cloud', fontsize=16, pad=20)
        
        # Convert to base64 image for display in marimo
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig_wc)
        
        wordcloud_html = f'<img src="data:image/png;base64,{img_base64}" style="max-width: 100%; height: auto;"/>'
    else:
        wordcloud_html = "<p>No domain data available</p>"
    
    return wordcloud_html, domain_col, domain_data


@app.cell
def __(wordcloud_html, mo):
    mo.Html(wordcloud_html)


@app.cell
def __(mo):
    mo.md("""
    ---
    
    ## 🗺️ Location Map
    """)


@app.cell
def __(df, pd, re, folium, MarkerCluster, HeatMap):
    # Map of locations
    location_col = df.columns[15]  # Your location column
    
    def extract_coords(loc_str):
        try:
            if pd.isna(loc_str):
                return None, None
            coords = re.findall(r'-?\d+\.?\d*', str(loc_str))
            if len(coords) >= 2:
                return float(coords[0]), float(coords[1])
        except Exception:
            pass
        return None, None
    
    df['latitude'], df['longitude'] = zip(*df[location_col].apply(extract_coords))
    df_map = df.dropna(subset=['latitude', 'longitude'])
    
    if len(df_map) > 0:
        center_lat = df_map['latitude'].mean()
        center_lon = df_map['longitude'].mean()
        
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=3,
            tiles='OpenStreetMap'
        )
        
        # Add markers
        for idx, row in df_map.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=8,
                popup=f"Location: {row[location_col]}",
                color='#2E86AB',
                fill=True,
                fillColor='#2E86AB',
                fillOpacity=0.7,
                weight=2
            ).add_to(m)
        
        # Add heatmap
        heat_data = [[row['latitude'], row['longitude']] for idx, row in df_map.iterrows()]
        HeatMap(heat_data, radius=20, blur=15, max_zoom=1, opacity=0.5).add_to(m)
        
        map_html = m._repr_html_()
    else:
        map_html = "<p>No valid GPS coordinates</p>"
    
    return map_html, df_map


@app.cell
def __(map_html, mo):
    mo.Html(map_html)


@app.cell
def __(df_map, mo):
    mo.md(f"""
    **Valid GPS points: {len(df_map)}**
    """)


# @app.cell
# def __(mo):
#     mo.md("""
#     ---
    
#     ## 📊 Statistical Summary
#     """)


# @app.cell
# def __(df, mo, np):
#     # Calculate summary statistics
#     numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
#     summary_text = "### Numeric Columns:\n\n"
#     if numeric_cols:
#         for _col in numeric_cols[:5]:  # Show first 5
#             if _col not in ['latitude', 'longitude']:
#                 _data = df[_col].dropna()
#                 if len(_data) > 0:
#                     summary_text += f"**{_col}**: Mean={_data.mean():.2f}, Median={_data.median():.2f}\n\n"
    
#     mo.md(summary_text)


@app.cell
def __(mo):
    mo.md("""
    ---
    
    ## ℹ️ About
    
    This dashboard was generated with:
    - **Marimo** - Framework for interactive notebooks
    - **Plotly** - Interactive visualizations
    - **Folium** - Geospatial maps
    - **Pandas** - Data analysis
    
    """)


if __name__ == "__main__":
    app.run()
