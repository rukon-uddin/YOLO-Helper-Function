# YOLO Helper Function

This repository is created to help people who are working with yolo. This are some functions which I had to write to solve my problems. If you face the below problems you can you my repo.

### YOLO_ConvertAndDrawBox.py
**Why to Use:** To denormalize the coordinates, and draw bounding box and label on the object. The labels color and size adapts with the bounding box size. Which give you a proper bounding box drawing on the image. In the images below, notice the color of the label, its dynamic!!.

**Input:** image, title/label, bounding box coordinates <br>
**Output:** an image with bounding box and label drawn.

<table>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/rukon-uddin/YOLO-Helper-Function/main/assets/bike1.jpg" alt="Image 1" width="350" height="200">
    </td>
    <td>
      <img src="https://raw.githubusercontent.com/rukon-uddin/YOLO-Helper-Function/main/assets/bike2.jpg" alt="Image 2" width="350" height="200">
    </td>
  </tr>
</table>


### YOLO_ClassCountPlot.py
**Why to Use:** This is class count. If you have the images and txt annotations, this function will automatically count the number of objects in the whole dataset.

**Input:** text file directory, classes.txt <br>
**Output:** A bar plot 

<table>
  <tr>
    <td>
      <img src="https://raw.githubusercontent.com/rukon-uddin/YOLO-Helper-Function/main/assets/classVis.png" alt="Image 1" width="350" height="300">
    </td>
  </tr>
</table>


### YOLO_SwapClassIndex.py
**Why to Use:** This can be helpful when you want to change the annotated index to some other index. For example you have annotated the car images as index 0, now you want to change the index to 2 becuase you have trained the model for car as index 2, then you can use this function. 

If you dont face this problem, its really hard to explain.