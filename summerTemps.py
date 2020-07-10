#!/usr/bin/python3
import plotly.graph_objects as go


def getInfo():
    with open("internalTemps.txt", "r") as f:
        internalData = f.read().split("|")
    with open("ambientTemps.txt", "r") as f:
        ambientData = f.read().split("|")
    internalData = returnData(internalData)
    ambientData = returnData(ambientData)
    drawChart(internalData, ambientData)


def returnData(textData):
    textData = [x.strip() for x in textData]
    dates = [textData[x] for x in range(len(textData)) if x % 2 == 0 and textData[x] != ""]
    temps = [textData[x] for x in range(len(textData)) if x % 2 != 0 and textData[x] != ""]
    return [dates, temps]


def drawChart(internalData, ambientData):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=internalData[0], y=internalData[1], name="GPU Internal Summer", line=dict(color="royalblue", width=4)))
    fig.add_trace(go.Scatter(x=ambientData[0], y=ambientData[1], name="Outside Temps Summer", line=dict(color="firebrick", width=4, dash="dot")))
    fig.update_layout(title="Average Temps for Summer | GPU Internal and Outside", xaxis_title="Month", yaxis_title="Temperature (C)")
    fig.show()


if __name__ == "__main__":
    getInfo()
    