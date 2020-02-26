function [dist, index1, index2] = dijistra(adjMatrix, s)
% adjMatrix: n*n matrix a_ij (i,j=1..n)
%     a_ij is inf if i,j is blocked
% s: index of source node
% dist: 1*n vector
% index1 is the sequence of node absorbed into knowned map
% index2 is the sequence of prev of endpoint of each shortest path
% index2 help to print shortest path with recursive function

adjMatrix(find(adjMatrix==0)) = inf;
pb(1:length(adjMatrix))=0; pb(s) = 1;
index1 = s;
index2 = ones(1,length(adjMatrix)) * s;
d(1:length(adjMatrix))=inf; d(s)=0;
temp = s;

while sum(pb)<length(adjMatrix)
  tb = find(pb==0); % index of those outside s
  d(tb) = min(d(tb), d(temp)+adjMatrix(temp, tb)); % update the dist(s, tb)
  tmpb = find(d(tb)==min(d(tb))); % index of the minimum node in tb
  temp = tb(tmpb(1)); % there might be non-sigle minimum, take randomly
  pb(temp) = 1; % the minimum absorbed into s
  index1 = [index1, temp]; % update index1
  temp2 = find(d(index1)==d(temp)-adjMatrix(temp, index1)); % temp2 is prev of temp
  index2(temp) = index1(temp2(1)); % update index2
end

dist = d;

endfunction
