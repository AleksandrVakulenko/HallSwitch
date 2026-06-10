Annotation
*тут нужно общее описание проекта

Software section:

Matlab R2021b:
	Depends on the 
	[Automation devices module](https://github.com/AleksandrVakulenko/Automation_device_class)
	of
	[Fern](https://github.com/AleksandrVakulenko/Fern)
	package manager.

	Usage:
	1) Setup Fern.
	2) Run Fern.load('aDevice') every time after launching MATLAB.
	3) Create device handle by class constructor:
		Box = Hall_box(COM_port);
	4) Run any possible commands:
		Box.set_relay('ABCD');

	Program example: TEST/Test_01.m, TEST/Test_02.m


Python:
	Depends on the pyserial.

	Usage:
	1) Install pyserial:
		python3 -m pip install pyserial
	2) Import python class:
		from Hall_box import HallBox
	3) Create device handle by class constructor:
		box = HallBox(com_port)
	4) Run any possible commands:
		err_status, err_no, err_comment = box.set_relay('ABCD')

	Program example: Test_02.py


LabView 17 64-bit:
	Usage:
	1) Download lib files from LabView folder of necessary version.
	2) Use Commutator_init vi to init connection.
	3) Use Commutator_query_CMD vi to send any command.
	4) Use Commutator_close vi to close connection.

	Program example: Demo_terminal.vi







Hardware section:

Gerber notation:

*тут нужна таблица
Обозначение - Полное название - Описание слоя
GTO	- Gerber Top Overlay - Верхняя шелкография / маркировка (Top Silkscreen / Overlay)
GTS	- Gerber Top Solder mask - Верхняя паяльная маска (Top Solder Mask)
GTL	- Gerber Top Layer - Верхний слой меди (Top Copper)
GBL	- Gerber Bottom Layer - Нижний слой меди (Bottom Copper)
GBS	- Gerber Bottom Solder mask - Нижняя паяльная маска (Bottom Solder Mask)
GBO	- Gerber Bottom Overlay - Нижняя шелкография (Bottom Silkscreen)

GKO	- Gerber Keep-Out  - Слой запретных зон и контура платы (Keep-Out Layer, Board Outline)
LXN - Layer X (eXtra) Notes - Слой металлизированных и не металлизированных отверстий (Layer of plated and non-plated holes)



Device assembly photo.
*тут вставить фото по этим ссылкам
Hardware/Photo/Photo_01.png
Hardware/Photo/Photo_02.png
Hardware/Photo/Photo_03.png
Hardware/Photo/Photo_04.png
