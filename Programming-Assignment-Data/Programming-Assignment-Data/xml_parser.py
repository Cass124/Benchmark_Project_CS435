from PIL import Image
from PIL import ImageDraw
import os
from bs4 import BeautifulSoup



def format_bounds(bounds):
    """ Extracts the individual coordinates for the bounds of the node and formats them into a list containing the top x, top y, bottom x, and bottom y coordinates """
    
    bounds=bounds.split('][')
    top= bounds[0].replace('[','').split(',')
    bttm= bounds[1].replace(']','').split(',')
    tx,ty=int(top[0]), int(top[1])
    bx,by=int(bttm[0]), int(bttm[1])
    coords=[tx,ty,bx,by]
    return coords



def markup(coords,image):
    """ Takes a list of coordinates cooresponding to the bounds of each leaf node and uses them to draw rectangles around each GUI feature. The new image is then saved in a new folder titled 'marked_pngs' with 'marked_' in front of the image name """
    
    img= Image.open(image)
    draw= ImageDraw.Draw(img) 
    for element in coords:
        draw.rectangle(element,outline='yellow',width=10)
    if  not os.path.exists('marked_pngs'):
        os.makedirs('marked_pngs')
    img.save(os.path.join('marked_pngs','marked_'+image))




def get_bounds(nodes):
    """ Retrieves the bounds of each leaf node """
    bounds=[]
    for i in nodes:
        if len(i)==0:
            bounds.append(format_bounds(i.attrs['bounds']))
        # if len(i)>0:
        #     for j in str(i).split('\n'):
        #         if j[-2:]=='/>':
        #             print(j)
    return bounds

def read_files(folder):
    """ Reads all the files in the current directory and sends all files with the 'xml' extension to the get_bounds function. Cooreseponding 'png' files are passed with the extracted bounds to the markup function. """

    for file in os.listdir(folder):
        if file.endswith('xml'):
           
            image_path=os.path.splitext(file)[0] + '.png'
            try:
                send=open(file, "r")
                contents=send.read()
                
                soup=BeautifulSoup(contents,'xml')
                
                nodes=soup.find_all('node')
                
                bounds=get_bounds(nodes)
    
                markup(bounds,image_path)
            except:
                print(file, 'threw an exception\n\n')

if __name__ == "__main__":
    
    read_files(os.getcwd())