import base64


# 图片转base64
def to_base64(img):
    if img:
        img64 = str(base64.b64encode(img))[2:-1]
        return img64
    else:
        return 0


def to_img(img64):
    # base64转回图片
    img = base64.b64decode(img64)
    with open("ss.jpg", "wb") as fa:
        fa.write(img)
