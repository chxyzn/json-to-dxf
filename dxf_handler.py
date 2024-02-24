import ezdxf
import math
from ezdxf.enums import TextEntityAlignment


def plot_room(room,msp):
    corners = room.corners
    msp.add_lwpolyline(corners,close=True,dxfattribs={"layer":"room_border"})

    room_hatch = msp.add_hatch(color=room.index)
    room_hatch.paths.add_polyline_path(corners, is_closed=True)
    msp.add_text("A Simple Text :"+ str(room.index),
    height=0.35,).set_placement(
    (room.width/2, room.height/2),
    align=TextEntityAlignment.CENTER
)
    return 

def sum_coords(coord1, coord2):

    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    
    sum_x = x1 + x2
    sum_y = y1 + y2
    sum_z = z1 + z2
    
    return (sum_x, sum_y, sum_z)

corners = [(0,0,0),(0,50,0),(90,50,0),(90,0,0),(0,0,0)]
wallHeight =70
height=50
width=90
corners2 = [(0,0),(0,50),(90,50),(90,0),(0,0)]

doc = ezdxf.new(setup=True)
msp = doc.modelspace()

floorLayer=doc.layers.add(name="floor",color=5)
floorLayer.on()

floorHatch = msp.add_hatch(color=2)
floorHatch.transparency=0.4
floorHatch.paths.add_polyline_path(corners2,is_closed=True)

ceilHatch = floorHatch.copy()
ceilHatch.translate(0,0,wallHeight)

widthWall = msp.add_hatch(9)
widthWall.transparency=0.3
widthWall.paths.add_polyline_path([(0,0),(90,0),(90,wallHeight),(0,wallHeight)])
widthWall.rotate_x(math.radians(90))

widthWallCopy = widthWall.copy()
widthWallCopy.translate(0,height,0)
msp.add_entity(widthWallCopy)

heightWall = msp.add_hatch(9)
heightWall.transparency-0.3
heightWall.paths.add_polyline_path([(0,0),(0,50),(wallHeight,50),(wallHeight,0)],is_closed=True)
heightWall.rotate_y(math.radians(270))

heightWallCopy = heightWall.copy()
heightWallCopy.translate(width,0,0)
msp.add_entity(heightWallCopy)

floor = doc.blocks.new(name='FLAG')
floor.add_lwpolyline(corners,dxfattribs={"layer":"floor"})



for element in corners[:-1]:
    floor.add_line(element,sum_coords(element,(0,0,70)))
    

msp.add_blockref('FLAG', (0,0),dxfattribs={'color':3})

# doc.saveas('okay2.pdf',)

