# ECE411-Fall2020Practicum
This project is based in adding security and ease of access trough a door using Facial Recognition and RFID technologies. The implementation of keeping track of how many (Authorized) user go inside/out of a building is an extra feature that can aid with companies enforcing distancing strategies for COVID purposes. 

### TEAM 8: Hamed AlSaegui, Anthony Warner, Josh Pradera and Tamar Stigler-Flores.


### Arduino Code

	==> if the code is not uploaded yet
		the file (411.ino) must be inside a folder named (411)
		Follow the ... for board connections
		compile and upload the programm to the ATMega chip.
		
	==> used libraries
		SPI.h
		MFRC522.h
		LiquidCrystal_I2C.h
		Wire.h
	==> High Level Diagram Code
		set the LCD address to 0x27 for a 16 chars and 2 line display
		initialize the lcd
		initialize counter
		initialize receiveEvent function
			receive byte as a character
		VOID SETUP
			Initiate I2C communication
			Initiate  address bus designated to I2C with Raspberry Pi
			Initiate each MFRC522 card
			Join I2C bus as slave with address 8
				Call receiveEvent when data received 
			initialize output pins
		VOID LOOP
			be ready to scan a tag
				if scanned to ENTER (RFID1)
					If Tag is Valid
						AUTHORIZED
					If Tag is Not Valid
						UNAUTHORIZED
				if scanned to EXIT (RFID2)
					If Tag is Valid
						AUTHORIZED
					If Tag is Not Valid
						UNAUTHORIZED
						
						
						
### Raspberry Pi Code (Python Script)

	==> The sequence of the Face Recognition code goes as follow:
		1 - Collect the data set of pictures from each user.
		==> Used libraries: 
		    cv2 (openCV)
		    numpy
		 ==> Use the CascadeClassifier and load haarcascade_frontal_default.xml (used for the detection of faces)
		     Setup the raspberry pi camera
		     Setup input variable to assign an specific User ID (as a number)
		     WHILE TRUE
		     		Read from the raspberry pi camera.
				Set a onvertion for the photos from RGB to Gray Scale.
				Detect the face from the user.
				Increase the sampleNum variable by 1 as the picture samples are taken.
				Open window with video feed and also draw a rectangle on the detected face.
				Save 20 pictures in a folder named dataSet.
				When done break the LOOP.
		    Release the camera.
		    Destroy all the windows opened by the program.
		    
		    2- Train the data and create a file named trainingData.yml that will be used to recognize an user.
		       The .yml file contains  the serialized data for specific users.
		   ==> Used libraries:
		       os 
		       cv2
		       numpy
		       from PIL import Image (for manipulation of Images)
		       Create variable recognizer and call the function to create a Local Binary Operator.
		       	-  LBPH is used to extract features from an input image and match them with the faces in system's database.
		       Set the dataSet path.
		       Create  two arrays. One name faces and another names IDs.
		      		 Execute a for loop that will loop as many times as the amount of images that we have in the dataSet folder.
		      		 Convert images in monochromo format.
		      		 Convert images into a numpy array with name faceImg.
		      		 Extract ID from the name of the image and add it to the array IDs and add the data to the array faces.
		       Train the data set.
		       Save the .yml file inside recognizer folder.
		       Destroy all the windows opened by the program.
		       
		    3- Recognize a face an open the door.
		    ==> Used libraries:
		        numpy
			cv2
			time
			from smbus import SMBus (I2C communication)
		        Specify bus address used for I2C.
			Setup the CascadeClassifier function with the haarcascade_frontalface_default.xml
			Setup Raspberry Pi camera.
			Create a variable named rec and use the Local Binary Operator function.
			Load the trained data present in the .yml file.
			Initiate id to 0
			Create a solenoid function for the I2C communication between Raspberry Pi and Arduino.
				Write a byte 0x1 using bus address 0x8 to unlock the door.
				Wait for 5 seconds.
				Write a byte 0x0 using the same bus address  to Lock the door.
				
			While True
				Read from Raspberry Pi camera.
				Convert pictures from Color to Gray Scale.
				Set a Multiscale to compensate from faces closer and far away from the camera.
			        For LOOP 
					Start the prediction of the user based in the trained data and the face detected using the haar cascade file.
					Compare faces detected to IDs .
					If the ID and face detected match, release the camera and set the camera again for stability issues with the time library.
						Print the user Name in the terminal for testing purposes.
						Call the solenoid function and send  a 0x1 bit to the Arduino over I2C to unlock door.
						Wait for 5 seconds. 
						Send  a 0x0 bit to the Arduino to lock the door.
					ELSE IF ID dosnt match the trained data set.
						Print Unauthorized user in the terminal for testing purposes.
						Release the camera.
						Setup the camera. 
						
				Brake out of the program with cntrl+C. 
				Release the camera.
				Destroy all the windows created by the program.
						
					
					
					
					
				
			
		       
				
				
				
				
				
				
