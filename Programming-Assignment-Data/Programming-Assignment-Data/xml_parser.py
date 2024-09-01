import xml.etree.ElementTree as ET 
from lxml import etree
from PIL import Image
from PIL import ImageDraw
import os

def find_leaf_bounds(node,image_path):
        if len(node) ==0:
            # print(f"Leaf Node: resource-id={node.attrib.get('resource-id')} text={node.attrib.get('text')} bounds={node.attrib.get('bounds')}")
            bounds=node.attrib.get('bounds')
            
            bounds=bounds.replace('[','(').replace(']',')').split(')(')
            top= bounds[0].replace('(','').split(',')
            bttm= bounds[1].replace(')','').split(',')
            tx,ty=int(top[0]), int(top[1])
            bx,by=int(bttm[0]), int(bttm[1])
            print(tx,ty,bx,by)
            pic(tx,ty,bx,by,image_path)
            # print('BOUNDS:', bounds, type(bounds))
            return bounds
        else:
            for child in node:
                    find_leaf_bounds(child,image_path)



def read_files(folder):
    for file in os.listdir(folder):
        if file.endswith('xml'):
            print("\nFILENAME:",os.path.splitext(file)[0],'\n')
            image_path=os.path.splitext(file)[0]
            try:
                tree= ET.parse(file)
                root=tree.getroot()
                find_leaf_bounds(root,image_path)
                
            except:
                print(file, 'threw an exception\n\n')

def pic(tx,ty,bx,by,image):
    img= Image.open(image)
    draw= ImageDraw.Draw(img)
    # image_width, image_height=img.size
    # top_left_x = (image_width - 100) // 2
    # top_left_y = (image_height - 50) // 2
    # bottom_right_x = top_left_x + 100
    # bottom_right_y = top_left_y + 50
    
    # Draw the rectangle
    # draw.rectangle([top_left_x, top_left_y, bottom_right_x, bottom_right_y], outline='yellow', fill='yellow')
    draw.rectangle([tx,ty,bx,by],outline='yellow',fill='yellow')
    img.show()



if __name__ == "__main__":
    tree= ET.parse('com.giphy.messenger-1.xml')
    root=tree.getroot()
    find_leaf_bounds(root,'com.giphy.messenger-1.png')
    # read_files(os.getcwd())
    # pic()