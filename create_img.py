from PIL import Image

base_img = Image.open('myself.jpg')
f_img = Image.open('head1.png')
f_img = f_img.resize(base_img.size, Image.ANTIALIAS)

base_img = base_img.convert('RGBA')
f_img = f_img.convert('RGBA')

out_img = Image.new('RGBA', base_img.size)
out_img = Image.alpha_composite(out_img, base_img)
out_img = Image.alpha_composite(out_img, f_img)
out_img = out_img.convert('RGB')
out_img.save('new_avatar.jpg', quality=95)