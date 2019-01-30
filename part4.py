import nibabel as nib
import matplotlib.pyplot as plt


def show_slices(slices):
	plt.suptitle("Center slices for EPI image")
	fig, axes = plt.subplots(1, len(slices))
	for i, slice in enumerate(slices):
		axes[i].imshow(slice.T, cmap="gray", origin="lower")
	# plt.show()
	plt.savefig("brain.png")


img_load = nib.load('./data/T2.nii')
img_data = img_load.get_fdata()
img_slice1 = img_data[:, 100, :]
img_slice2 = img_data[100, :, :]
img_slice3 = img_data[:, :, 100]
show_slices([img_slice1, img_slice2, img_slice3])
