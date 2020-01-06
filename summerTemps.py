#!/usr/bin/python3
import plotly.graph_objects as go

def summer():
    with open("internalTemps.txt", "r") as f:
        internalData = f.read().split("|")
    internalData = [x.strip() for x in internalData]
    dates = [internalData[x] for x in range(len(internalData)) if x % 2 == 0 and internalData[x] != ""]
    temps = [internalData[x] for x in range(len(internalData)) if x % 2 != 0 and internalData[x] != ""]
    
    with open("ambientTemps.txt", "r") as f:
        ambientData = f.read().split("|")
    ambientData = [x.strip() for x in ambientData]
    ambDates = [ambientData[x] for x in range(len(ambientData)) if x % 2 == 0 and ambientData[x] != ""]
    ambTemps = [ambientData[x] for x in range(len(ambientData)) if x % 2 != 0 and ambientData[x] != ""]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=temps, name="GPU Internal Summer", line=dict(color="royalblue", width=4)))
    fig.add_trace(go.Scatter(x=ambDates, y=ambTemps, name="Outside Temps Summer", line=dict(color="firebrick", width=4, dash="dot")))
    fig.update_layout(title="Average Temps for Summer | GPU Internal and Outside", xaxis_title="Month", yaxis_title="Temperature (C)")
    fig.show()


if __name__ == "__main__":
    summer()