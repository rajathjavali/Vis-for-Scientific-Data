filename = 'data/NOAA-Temperatures.csv';
M = csvread(filename, 5,0);
year = M(:,1);
value = M(:,2);
%Convert to farehneit
value = 1.8.*value + 32;
bar(year, value)
ylim([28 34]);
xlabel('Year')
ylabel('F +/- from the average')
title('Bar Plot depicting temperature changes through years 1880 - 2017 ')