from paraview.simple import *

# getting the loaded data from paraview
gradCanyonData = GetActiveSource() 
SetActiveSource(gradCanyonData)

# create a new 'Warp By Scalar'
warpByScalar = WarpByScalar(Input=gradCanyonData)
warpByScalar.Scalars = ['POINTS', 'Scalars_']

view = GetActiveViewOrCreate('RenderView')
view.ViewSize = [2048, 753]
view.AxesGrid = 'GridAxes3DActor'
view.StereoType = 0
view.Background = [0.32, 0.34, 0.43]

# show data in view
warpByScalarDisplay = Show(warpByScalar, view)

view.ResetCamera()