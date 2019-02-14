from paraview.simple import *
arrowList = []
shrinkList = []
extractEdgesList = []

for i in range(16):
	arrow = Arrow()
	arrow.TipResolution = 12
	arrowList.append(arrow)

rv = GetActiveViewOrCreate('RenderView')

for i in range(16):
	arrowShrinking = Shrink(Input = arrowList[i])
	shrinkList.append(arrowShrinking)
	shrinkDisplay = Show(shrinkList[i], rv)
	shrinkDisplay.Orientation = [0, 0, i*22.5]
	extractEdges = ExtractEdges(Input = arrowList[i])
	extractEdgesList.append(extractEdges)
	edgesDisplay = Show(extractEdgesList[i], rv)
	edgesDisplay.Orientation = [0,0,i*22.5]
	Render()
