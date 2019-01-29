filename = 'data/us_birth.csv';
M = csvread(filename, 1,0);
newmap = containers.Map(uint32(31), 31);
for i = 1:31
    newmap(i) = 0;
end
for i = 1:size(M(:,1))
    newmap(M(i,3:3)) = newmap(M(i,3:3)) + M(i,5:5);
end
value = values(newmap);
a = cell2mat(value);

[out, idx] = max(a(:));
X = sprintf("The maximum number of births are on Day %d, and the number is %d", idx, out);
disp(X)

[out, idx] = min(a(:));
X = sprintf("The minimum number of births are on Day %d, and the number is %d", idx, out);
disp(X)

counter_summer = 0;
for i = 1:size(M(:,1))
    if M(i,2:2) == 5 || M(i,2:2) == 6 || M(i,2:2) == 7 || M(i,2:2) == 8
        counter_summer = counter_summer + M(i, 5:5);
    end
end
X = sprintf("Number of Births in Summers are %d", counter_summer);
disp(X)

counter_winter = 0;
for i = 1:size(M(:,1))
    if M(i,2:2) == 11 || M(i,2:2) == 12 || M(i,2:2) == 1 || M(i,2:2) == 2
        counter_winter = counter_winter + M(i, 5:5);
    end
end
X = sprintf("Number of Births in Winters are %d", counter_winter);
disp(X)

disp("It can be concluded that number of births in winter are less than the number of births in Summer")

counter = 0;

for i = 1:size(M(:,1))
    if M(i,3:3) == 13 && M(i,4:4) == 5
        counter = counter + M(i, 5:5);
    end
end
X = sprintf("The number of birthds are on Friday the 13th are %d", counter);
disp(X)

