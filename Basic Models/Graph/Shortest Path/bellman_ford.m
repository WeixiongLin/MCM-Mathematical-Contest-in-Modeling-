function bellman_ford(d, n, s)
%d为已知图的邻接矩阵，n为顶点数（各顶点标号为1,2,...,n），s为源点标号

for i=1:n %初始化dist，pre
    dist(i)=inf; %dist(i)为s，i之间的最短路的长度
    pre(i)=NaN; %pre(i)为s到i的最短路上i的前一个顶点
end

dist(s)=0;

for k=1:n-1
    for i=1:n 
        for j=1:n
            if d(i,j)~=inf
                if dist(j)>dist(i)+d(i,j)
                    dist(j)=dist(i)+d(i,j);
                    pre(j)=i;
                end
            end
        end
    end
end

for i=1:n
    for j=1:n
        if d(i,j)~=inf
            if dist(i)+d(i,j)<dist(j) %判断有无负权回路
                error('Negetive WeightCircut');
            end
        end
    end
end
dist
pre
end
