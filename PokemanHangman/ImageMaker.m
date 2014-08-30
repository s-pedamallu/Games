src_dir = 'E:\Games\PokemanHangman\game_images\pokemon';
dest_dir = 'E:\Games\PokemanHangman\game_images\hidden_pokemon';
for t = 1:649
    tmp = strcat(src_dir,'\',num2str(t),'.png');
    [base_img,img_map] = imread(tmp);
    gray_img = ind2gray(base_img,img_map);
    [r,c] = size(gray_img);
    for i = 1:r
        for j = 1:c
            if gray_img(i,j) < 15
                gray_img(i,j) = 150;
            else
                gray_img(i,j) = 75;
            end
        end
    end
    tmp = strcat(dest_dir,'\',num2str(t),'.png');
    imwrite(gray_img,tmp);
end