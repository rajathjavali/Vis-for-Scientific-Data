from paraview.simple import *

# getting the loaded data from paraview
grandCanyonData = GetActiveSource() 
SetActiveSource(grandCanyonData)
view1 = GetActiveViewOrCreate('RenderView')
window1 = Show(grandCanyonData, view1)
window1.SetScalarBarVisibility(view1, True)
view1.ResetCamera()


layout = GetLayout()
layout.SplitHorizontal(0, 0.5)


plotOverLine = PlotOverLine(Input=grandCanyonData,
    Source='High Resolution Line Source')

plotOverLine.Source.Point2 = [4096.0, 2048.0, 0.0]

SetActiveSource(plotOverLine)

lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [600, 500]
lineChartView1.LeftAxisRangeMaximum = 6.66
lineChartView1.BottomAxisRangeMaximum = 6.66
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisRangeMaximum = 6.66

layout.AssignView(2, lineChartView1)

plotOverLine1Display = Show(plotOverLine, lineChartView1)
