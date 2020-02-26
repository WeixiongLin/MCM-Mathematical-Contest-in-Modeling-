function [path] = dijistra_path(prev, s, v)
  % prev是最短路终点的前驱矩阵
  % path将输出源点s到终点v的路径
  path = v;
  if path(1)!=s
    path = [prev(path(1)), path];
  endif
  path = [s, path];
endfunction
