import os
import cv2

def resize_images(base_path):
    post_path = os.path.join(base_path, 'files')
    if not os.path.exists(post_path):
        print(f"The directory {post_path} does not exist.")
        return
    
    for image in os.listdir(post_path):
        img_g = cv2.imread(post_path + f"/{image}",0);
        resized_image = cv2.resize(img_g, (100,100))
        cv2.imwrite(os.path.join(post_path, f"resized_{image}"), resized_image)


if __name__ == "__main__":
    base_path = './exercises/batch-image-resizing'
    resize_images(base_path)