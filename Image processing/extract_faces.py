import cv2
import re
import shutil
import os 
import argparse

path_given = False # argument is passed or not

def get_faces(imgs_dir, box_faces = False):

    # given dir
    if path_given: 
        if not os.path.isdir(imgs_dir + 'extracted_faces/'):
            os.mkdir(imgs_dir + 'extracted_faces/')
        ext_fld = imgs_dir + 'extracted_faces/'

    # current dir    
    else: 
        if not os.path.isdir('extracted_faces/'):
            os.mkdir('extracted_faces/')
        ext_fld = 'extracted_faces/'

    imgs = os.listdir(imgs_dir)
    for img in imgs:  
        pat = r'(\w+)\.jpg'
        pat_str = re.search(pat, img)
        if not pat_str:
            continue
        img =  pat_str.group(1)
        if not path_given:
            image = cv2.imread(img + '.jpg')
        else:
            image = cv2.imread(imgs_dir + img + '.jpg')    
        # create a faceCascade object that will load the Haar Cascade file
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        # apply detectMultiScale() method on the faceCascade object. This generates list of rectangles for all faces in image.
        # this returns list co-ordinates of rectangles
        faces = faceCascade.detectMultiScale(
                image,
                scaleFactor=1.3,
                minNeighbors=3,
                minSize=(30, 30)
        )
        print("Found {0} Faces!".format(len(faces)))  
        i = 0

        # draw rectangle around the face with co-ordinates found, also extract the faces found
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 0), 1)
            roi_color = image[y:y + h, x:x + w] 
            i+=1
            face_name = img +'_face'+str(i)+'.jpg'    
            cv2.imwrite(face_name, roi_color)
            save_loc = os.path.realpath(ext_fld + face_name)

            if path_given:
                from_loc = os.path.realpath(imgs_dir + face_name)
            else:
                from_loc = os.path.realpath(face_name)    

            shutil.move(from_loc,save_loc) 

        if box_faces:
            # save the image
            obj_img_name = img +'_labeled_faces.jpg'
            cv2.imwrite(obj_img_name, image)
            save_loc = os.path.realpath(ext_fld + obj_img_name)
            if path_given:
                from_loc = os.path.realpath('/content/'+ obj_img_name)
            else:
                from_loc = os.path.realpath(obj_img_name)    
            shutil.move(from_loc,save_loc)

    print('DONE')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--imgs_path", help="string path to image directory")
    # parser.add_argument("--boxes", help="add boxes to images")
    args = parser.parse_args()
    if args.imgs_path:
        get_faces(args.imgs_path)
        path_given = True
    else:
        get_faces(os.curdir)    

