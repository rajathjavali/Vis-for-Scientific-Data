import nibabel as nib
import matplotlib.pyplot as plt


def show_slices(slice):
    plt.suptitle("Center slices for EPI image")
    plt.imshow(slice.T, cmap="gray", origin="lower")
    # plt.show()
    plt.savefig("brain.png")


img_load = nib.load('data\T2.nii')
img_data = img_load.get_fdata()
img_slice = img_data[:, 160, :]
show_slices(img_slice)
