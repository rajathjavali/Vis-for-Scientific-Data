from paraview.simple import *
arrow_list = []

for i in range(16):
	arrow = Arrow()
	arrow.TipResolution = 12
	arrow_list.append(arrow)

rv = GetActiveViewOrCreate('RenderView')

for i in range(16):
	display = Show(arrow_list[i], rv)
	display.Orientation = [0,0,i*22.5]
	Render()
