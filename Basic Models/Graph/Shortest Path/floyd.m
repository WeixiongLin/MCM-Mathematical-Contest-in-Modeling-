function [dist, prev] = floyd(a)
% a为邻接矩阵
% dist为距离矩阵
% prev为前驱矩阵

n = size(a, 1); % 节点个数
d = a; % 初始化距离矩阵
d(find(d==0)) = inf;
d(1:n+1:end) = 0;


prev = (ones(n, 1)*(1:n))'; % 初始化前驱向量

% Floyd算法开始
for k=1:n
    for i=1:n
        for j=1:n
            if d(i,k)+d(k,j)<d(i,j)
                d(i,j)=d(i,k)+d(k,j);
                prev(i,j) = prev(k,j); % 将路径 i→j 改为 i→k→j，因此路径（i→j）的前驱变为（k→j）的前驱
            end 
        end 
    end
end

dist = d;

endfunction
