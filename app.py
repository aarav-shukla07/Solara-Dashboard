import solara
import plotly.graph_objs as go
import numpy as np

# Reactive state
function_selector = solara.reactive("sin")
frequency_slider = solara.reactive(1.0)

# 🎨 Chart Theme Settings
def get_plotly_figure(func_name: str, freq: float):
    x = np.linspace(0, 10, 500)

    if func_name == "sin":
        y = np.sin(freq * x)
    elif func_name == "cos":
        y = np.cos(freq * x)
    elif func_name == "tan":
        y = np.tan(freq * x)
        y[np.abs(y) > 10] = np.nan  # avoid extreme spikes

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y, mode='lines',
        line=dict(color='#00BFFF', width=3),
        name=func_name
    ))
    fig.update_layout(
        title=dict(text=f"{func_name}(x) with Frequency {freq}", x=0.5, font=dict(size=20)),
        plot_bgcolor="#f5f5f5",
        paper_bgcolor="#f5f5f5",
        font=dict(color="#333", size=14),
        margin=dict(t=60, l=40, r=40, b=40),
        xaxis=dict(title="x"),
        yaxis=dict(title=f"{func_name}(x)")
    )
    return fig

# 📊 Plot Component
@solara.component
def FunctionPlot():
    fig = get_plotly_figure(function_selector.value, frequency_slider.value)
    solara.FigurePlotly(fig)


# 🌟 UI Component
@solara.component
def Page():
    with solara.Column(style={"padding": "2rem", "gap": "2rem"}):
        solara.Markdown("## ✨ Function Visualizer\nCustomize and explore different trigonometric functions interactively.")

        with solara.Card(title="⚙️ Controls", style={"width": "100%", "maxWidth": "600px"}):
            solara.Select(label="Choose a function", value=function_selector, values=["sin", "cos", "tan"])
            solara.SliderFloat(label="Frequency", value=frequency_slider, min=0.1, max=5.0, step=0.1)

        with solara.Card(title="📈 Plot Output", style={"width": "100%", "maxWidth": "900px"}):
            FunctionPlot()
