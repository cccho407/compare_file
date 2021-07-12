import os

if __name__=='__main__':
    path_1 = "./image/"
    path_2 = './xml/'

    xml_list = []
    image_list = []

    for i in os.listdir(path_2):
        name = i[:-4]
        xml_list.append(name)
    
    for i in os.listdir(path_1):
        name = i[:-4]
        image_list.append(name)
    xml_list = set(sorted(xml_list))
    image_list = set(sorted(image_list))
    result = image_list -xml_list

    for i in result:
        i = i + '.jpg'
        os.remove(path_1+i)
    
    