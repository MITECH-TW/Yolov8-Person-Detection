import os

def extractClass(classid,foldername):
    # specify the directory path containing the txt file
    directory_path = './datasets/coco/labels/'+foldername  # Please replace this with your directory path
    new_label_directory_path = './datasets/coco/labels/'+foldername+'_person/'  # Please replace this with your directory path
    new_train_image_txt = './datasets\coco\labels/'+foldername+'.txt'

    count = 0
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):  # only process files ending with .txt
            # build the complete file path
            file_path = os.path.join(directory_path, filename)

            # get the file name part (including the extension) of the input file
            input_file_name = os.path.basename(file_path)

            # remove the extension and build the complete path of the output file
            output_file_name = os.path.splitext(input_file_name)[0] + ".txt"
            output_file_path = os.path.join(new_label_directory_path, output_file_name)
            if os.path.exists(new_label_directory_path) == False:
                os.makedirs(new_label_directory_path)

            # open the data file for reading
            with open(file_path, 'r',newline='') as file:
                data = file.read()

            # split the data using the newline character
            data_lines = data.split('\n')

            # create an empty list to store the data that meets the condition
            filtered_data = []

            # loop through each line of data and determine if the first number is 0
            for line in data_lines:
                parts = line.split()
                if len(parts) > 0 and float(parts[0]) == classid:
                    filtered_data.append(line)

            if len(filtered_data) > 0:
                with open(output_file_path, 'w',newline='') as output_file:
                    for line in filtered_data:
                        output_file.write(line + '\n')
                with open(new_train_image_txt, 'a',newline='') as train_image_txt:
                    train_image_txt.write('./images/'+foldername + os.path.splitext(input_file_name)[0] + '.jpg' + '\n')
                    count += 1
                print(f"The data that meets the conditions has been written to the file {output_file_path}.")
                print(f"The data that meets the conditions has been written to the files {new_train_image_txt}, {count}.")
def extractbg(foldername):
    #If the name of the image does not have the same name txt file in train2017_person, then save its path to bg.txt
    image_path = './datasets\coco\images/'+foldername
    txt_path = './datasets\coco\labels/'+foldername+'_person'
    bg_txt_path = './datasets\coco\labels/'+foldername+'_bg.txt'
    count = 0
    current = 0
    for filename in os.listdir(image_path):
        if filename.endswith('.jpg'):  # only process files ending with .txt
            # build the complete file path
            current += 1
            file_path = os.path.join(txt_path, filename.replace('.jpg','.txt'))
            if os.path.exists(file_path) == False:
                with open(bg_txt_path, 'a',newline='') as bg_txt:
                    bg_txt.write('./images/'+foldername+'/'+filename + '\n')
                    count += 1
                    print(f"{filename} has been written to bg.txt.")
            print(f"{current} images have been processed, and a total of {count} images have been written to bg.txt.")


if __name__ == "__main__":
    extractClass(0,'train2017')
    extractbg('train2017')
    extractClass(0,'val2017')
    extractbg('val2017')