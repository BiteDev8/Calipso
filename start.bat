ECHO OFF
:q
mode con cols=100 lines=25
cls
color c                                                                                  
echo CALIPSO discord fun tools                                                                                      
echo by Opale
echo. 
echo		[1] calipso
echo.
echo		[2] crypt decrypt 		
echo.
echo		[3] setup 	
echo.
echo		[0] exit		
echo.
SET /P ANSWER=choix du numero  :
if /i {%ANSWER%}=={0} (goto :exit)
if /i {%ANSWER%}=={1} (goto :listen)
if /i {%ANSWER%}=={2} (goto :crypt)
if /i {%ANSWER%}=={3} (goto :set)
goto :q
:listen
start listenner.bat
goto :q
:crypt
start decrypt.bat
goto :q
:set
start setup.bat
goto :q
:exit
cls
exit