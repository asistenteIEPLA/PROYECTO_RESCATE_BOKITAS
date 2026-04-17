
SET TALK OFF
SET ECHO OFF
SET DATE DMY
SET CENTURY ON
SET DECIMALS TO 2
SET EXCLUSIVE OFF
SET DELETED ON
SET SAFETY OFF
SET NOTIFY OFF
SET MULTILOCKS ON
SET STATUS BAR OFF
SET SYSMENU OFF
OPEN DATABASE BaseDeDatos\bokitas.dbc SHARED


PUBLIC Inicio


*****  Chequea que  no se este ejecutando otra vez el programa ******
_Screen.WindowState = 2
_SCREEN.Caption="SISTEMA INTEGRAL DE CONTROL DE SALUD BOKITAS Ver 2.6"
IF YaEstaActivo()
	loLogo = .NULL.
	RETURN
ELSE

	_SCREEN.ADDOBJECT("oImg", "Image") 
	_screen.oImg.picture = 'C:\BOKITAS\BASEDEDATOS\BOKITAS.JPG' 
	_SCREEN.oImg.TOP = (_SCREEN.HEIGHT- _SCREEN.oImg.HEIGHT)/2 
	_SCREEN.oImg.LEFT = (_SCREEN.WIDTH - _SCREEN.oImg.WIDTH)/2 
	_SCREEN.oImg.anchor = 240
	_SCREEN.oImg.stretch = 1
	_SCREEN.oImg.VISIBLE = .T. 

	
		
	DO FORM c:\bokitas\formularios\frm_reg_inicio.scx
READ EVENTS

ENDIF

*********



*------------------------------------------------------
* FUNCTION YaEstaActivo()
* - - - - - - - - - - - - - - - - - - - - - - - - - - -
* Verifica si el programa ya está activo
* Retorna: .T. ó .F. si esta activo o no activo
*------------------------------------------------------
FUNCTION YaEstaActivo()
	LOCAL lcCaption, llRet
	DECLARE INTEGER FindWindow IN WIN32API ;
	STRING cNULL, STRING cWinName
	lcCaption = _SCREEN.CAPTION
	_SCREEN.CAPTION = '_' + lcCaption
	lnHWnd = FindWindow(0, lcCaption)
	IF lnHWnd # 0
		DECLARE INTEGER SetForegroundWindow IN user32;
		INTEGER hWindow
		DECLARE INTEGER ShowWindow IN user32;
		INTEGER HWND, ;
		INTEGER nCmdShow
		SetForegroundWindow(lnHWnd)
		ShowWindow(lnHWnd, 9)
		llRet = .T.
	ELSE
		llRet = .F.
	ENDIF
	_SCREEN.CAPTION = lcCaption
	RETURN llRet
ENDFUNC


