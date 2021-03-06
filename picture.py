"""
picture.py
Author: David Wilson
Credit: None

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

# https://www.mathsisfun.com/numbers/hexadecimal-color-names.html

Size = float(input("Set Size"))
SkyWidth = Size*90
SkyHeight = Size*40
GroundHeight = SkyHeight/10
MountWidth = Size*20
MountHeight = MountWidth*1.6
OffSide = SkyWidth/20
SnowWidth = MountWidth/3
SnowHeight = SnowWidth*1.6
CloudWidth = SkyWidth/6
CloudHeight = SkyHeight/20

White = Color(0xFFFFFFF, 1.0)
Yellow = Color(0xFFFF00, 1.0)
Black = Color(0x000000, 1.0)
SkyBlue = Color(0x87CEFA, 1.0)
GroundCol = Color(0x556B2F, 1.0)
MountCol = Color(0xD2B48C, 1.0)
BirdCol = Color(0xF4A460, 1.0)
Orange = Color(0xFFA500, 1.0)

ThinLine = LineStyle(1, Black)

Back = RectangleAsset(SkyWidth, SkyHeight, ThinLine, SkyBlue)
Ground = RectangleAsset(SkyWidth, GroundHeight, ThinLine, GroundCol)
Sun = CircleAsset(SkyWidth/15, ThinLine, Yellow)
Mount = PolygonAsset([(SkyWidth-(MountWidth/2)-OffSide, SkyHeight-MountHeight), (SkyWidth-MountWidth-OffSide, SkyHeight), (SkyWidth-OffSide, SkyHeight)], ThinLine, MountCol)
Snow = PolygonAsset([(SnowWidth/2, 0), (0, SnowHeight), (SnowWidth, SnowHeight)], ThinLine, White)
Cloud1 = EllipseAsset(CloudWidth, CloudHeight, ThinLine, White)
Cloud2 = EllipseAsset(CloudWidth/2, CloudHeight, ThinLine, White)
Cloud3 = EllipseAsset(CloudWidth*0.75, CloudHeight*1.5, ThinLine, White)
BirdBody = PolygonAsset([(0, 0), (SkyWidth/20, SkyHeight/30), (0, SkyHeight/15)], ThinLine, BirdCol)
BirdHead = CircleAsset(SkyHeight/30, ThinLine, BirdCol)
BirdBeak = PolygonAsset([(0, 0), (SkyWidth/100, SkyHeight/150), (0, SkyHeight/75)], ThinLine, Orange)
BirdEye = CircleAsset(SkyHeight/250, ThinLine, Black)

Sprite(Back)
Sprite(Ground, (0, SkyHeight))
Sprite(Sun, (SkyWidth-3*OffSide, SkyHeight-MountHeight))
Sprite(Mount)
Sprite(Snow, (SkyWidth-(MountWidth/2)-(SnowWidth/2)-OffSide, SkyHeight-MountHeight))
Sprite(Cloud1, (CloudWidth*1.25, CloudHeight*2))
Sprite(Cloud2, (CloudWidth*2.5, CloudHeight*4))
Sprite(Cloud3, (CloudWidth*3.75, CloudHeight*2))
Sprite(BirdBody, (SkyWidth/3, SkyHeight/3))
Sprite(BirdBeak, (SkyWidth/3+SkyWidth/20+SkyWidth/100, SkyHeight/3+SkyHeight/30-SkyHeight/150))
Sprite(BirdHead, (SkyWidth/3+SkyWidth/20, SkyHeight/3+SkyHeight/30))
Sprite(BirdEye, (SkyWidth/3+SkyWidth/19, SkyHeight/3+SkyHeight/30))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
