V=niftiread('data\T2.nii.gz');
h = imshow(V(:,:,100),[]);
saveas (h,'test.jpg');