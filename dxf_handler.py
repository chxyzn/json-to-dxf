import math
import copy
from ezdxf.enums import TextEntityAlignment

DECREMENT_WIDTH = 0.01
WALL_HEIGHT = 5


def get_text_color(index):
    color_list = [250,250,250,250,250,250,250,250,0]
    return color_list[(index)]

def plot_lines(msp, lines):
    for line_segment in lines:
        start_point, end_point = line_segment
        msp.add_line(start_point, end_point, dxfattribs={"layer": "room_border"})




def plot_room(room,msp):
    corners = copy.deepcopy(room.corners)# added [:] so that it created a new copy to protect original room paramenters
    
    xmid = 0
    ymid = 0

    for i in range(len(corners)):
        xmid+=corners[i][0]
        ymid+=corners[i][1]
       
    xmid/=4
    ymid/=4

    for i in range(len(corners)):
        if corners[i][0] < xmid:
            corners[i][0]+=DECREMENT_WIDTH
        else:
            corners[i][0]-=DECREMENT_WIDTH
        if corners[i][1] < ymid:
            corners[i][1]+=DECREMENT_WIDTH
        else:
            corners[i][1]-=DECREMENT_WIDTH


    msp.add_lwpolyline(corners,close=True,dxfattribs={"layer":"room_border"})

    room_hatch = msp.add_hatch(color=room.index%9)
    room_hatch.paths.add_polyline_path(corners, is_closed=True)
    msp.add_text(str(room.index),
    height=1.3, dxfattribs={'color': get_text_color(room.index%9)}).set_placement(
    (xmid, ymid),
    align=TextEntityAlignment.CENTER,
    
    )
    return 


def plot_walls(msp,lines):
    for line in lines:
        start_point, end_point = line
        if(start_point[0]==end_point[0]):
            wall_hatch = msp.add_hatch(color=9)
            wall_hatch.paths.add_polyline_path([start_point,end_point,(end_point[0]+WALL_HEIGHT,end_point[1]),(start_point[0]+WALL_HEIGHT,start_point[1])], is_closed=True)
            wall_hatch.rotate_y(math.radians(-90))
            wall_hatch.transparency = 0.2
            wall_hatch.translate(dx=start_point[0],dy=0,dz=-start_point[0])
            # wall_hatch.rgb(211,211,211)
        else:
            wall_hatch = msp.add_hatch(color=9)
            wall_hatch.paths.add_polyline_path([start_point,end_point,(end_point[0],end_point[1]+WALL_HEIGHT),(start_point[0],start_point[1]+WALL_HEIGHT)], is_closed=True)
            wall_hatch.rotate_x(math.radians(90))
            wall_hatch.transparency = 0.2
            wall_hatch.translate(dx=0,dy=start_point[1],dz=-start_point[1])
            # wall_hatch.rgb(211,211,211)

