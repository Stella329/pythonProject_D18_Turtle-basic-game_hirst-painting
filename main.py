import colorgram

colors = colorgram.extract('hirst.jpg',30)
    # colorgram.extract returns Color objects, which let you access: RGB, HSL, and what proportion of the image was that color.
    # Its properties are: Color.rgb - The color represented as a ‘namedtuple’ of RGB from 0 to 255


# ## TODO extract colors: METHOD 1
# color_list =[]
# for item in colors:
#     #color_list.append(item.rgb)  ## Color obj, rgb value
#     R=item.rgb.r ## using attributes
#     G = item.rgb.g
#     B = item.rgb.g
#     color_set = (R,G,B)
#     color_list.append(color_set)
#
#
# ## TODO METHOD 2
# turtle_color_list = []
# for item in color_list:
#     each_color = (item[0],item[1],item[2])  ## tuple
#     turtle_color_list.append(each_color)
# #print(turtle_color_list)

#TODO using the colors
color_list = [(199, 175, 175), (124, 36, 36), (210, 221, 221), (168, 106, 106), (222, 224, 224), (186, 158, 158), (6, 57, 57), (109, 67, 67), (113, 161, 161), (22, 122, 122), (64, 153, 153), (39, 36, 36), (76, 40, 40), (9, 67, 67), (90, 141, 141), (181, 96, 96), (132, 40, 40), (210, 200, 200), (141, 171, 171), (179, 201, 201), (172, 153, 153), (212, 183, 183), (176, 198, 198), (150, 115, 115), (202, 185, 185), (40, 72, 72), (46, 73, 73), (47, 66, 66)]
