# ECE411-Fall2020Practicum


### Raspberry Pi code (Python Script)


### Arduino Code

	==> if the code is not uploaded yet
		the file (411.ino) must be inside a folder named (411)
		Follow the ... for board connections
		complie and upload the programm to the ATMega chip
		
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
			Initiate a serial communication
			Initiate  SPI bus
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
				
				
				
				
				
				
