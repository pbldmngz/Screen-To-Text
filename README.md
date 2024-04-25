# Screen To Text Data Trasfer: When data is completelly locked
Recover files from a computer with no wired or wireless conections using computer vision and notepad.

> This program was created to automatically transcribe .patch files (git "recovery" files) from a computer that was suddently unable to transmit data (wired or not) and the only output generated was the screen. ** I've only tested it on text based files. **

## Instructions
Manually replicate the python files on `/Remote` on the target isolated machine.
This will generate a text file that represents characters using N amount of dots, being N the number correlated to the character.

Using the program on `/Local/dot_based_text_transmission.py`, retrieve the information on the `/Remote` generated text file. When the file transmition is over, use the `/Local/fix_formatting.py` program to transform the generated file into the final result.

> You may make changes to the `/Remote/encrypt_characters_as_dots.py` to adapt it or your needs (and if you don't intend to copy ALL those characters), but you must ensure the order in both `/Local` and `/Remote` are the same.

Also, take into account that my algorithm verifies the duplicates using **鳳** and the end of a page using **端**. So, if you see some random chinese characters around, it's merely for control. Also, if you get **侶**, you better turn on the `SHOW_CAMERA_FEED` obtion on the `/Local/dot_based_text_transmission.py`, most common cause is to have too much brightness on the camera.
