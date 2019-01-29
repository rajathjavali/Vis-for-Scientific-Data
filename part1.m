array1 = 1:1:200;
disp(array1)
boxplot(array1)
ylabel("Values 1-200")
title('Viz 1 - BoxPlot')

array2 = rand(1,10000);
disp(array2)
histogram(array2, 20)
xlabel('Bins (Automatic Binning)')
ylabel('Random Values')
title('Histogram of 10000 Random numbers from Uniform Distribution')

a = 1;
b = 100;
r = (b-a).*rand(1, 100) + a;
array = 1:1:100;
f = fopen('guassian_matlab.bin', 'w');
fwrite(f, r, 'float');
plot(array,r)
xlabel('Instances 1-100')
ylabel('Random numbers - Guassian Distribution')
title('Line Graph of Guassian distribution')
fclose(f);


input_file = fopen('guassian_matlab.bin');
r = fread(input_file, 'float');
histogram(r, [0,14,28,42,56,70,84,100])
xticks([0,14,28,42,56,70,84,100])
ylabel('Frequency')
xlabel('Bins')
title('Histogram -Guassian - divided into 7 bins')
fclose(input_file);