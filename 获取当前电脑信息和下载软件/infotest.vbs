'���ű��Ĺ����Ǽ��Ӳ������Ϣ�� 
On Error Resume Next 
temp=0 
set wshshell=wscript.createobject("wscript.shell") 
'����WMI���� 
wshshell.run ("%comspec% /c regsvr32 /s scrrun.dll"),0,True 
wshshell.run ("%comspec% /c sc config winmgmt start= auto"),0,True 
wshshell.run ("%comspec% /c net start winmgmt"),0 

strComputer = "." 
Set objWMIService = Getobject("winmgmts:\\" & strComputer &"\root\cimv2") 

'��һ���ı�����¼Ӳ����Ϣ 
Set WshNetwork = WScript.Createobject("WScript.Network") 
computername=WshNetwork.ComputerName
username=WshNetwork.userName 

strTime=CStr(Year(Now()))&Right("0"&Month(Now()),2)&Right("0"&Day(Now()),2) & "_" & CStr(Right("0"&Hour(Now()),2)&Right("0"&Minute(Now()),2)&Right("0"&Second(Now()),2))
set fso=createobject("scripting.filesystemobject") 
tempfilerpath="c:\users\"& username & "desktop"
tempfilter=(tempfilepath & computername & "-" & strTime & ".txt") 
set tempfile=fso.createtextfile(tempfilter) 

systeminfo2="ʱ��: " & now 
tempfile.writeline(systeminfo2)

'�û���
'Dim oFSO,oNetwork 
'Set oNetwork=CreateObject("Wscript.Network")  
tempfile.writeline("��ǰ�û�����" & Username)
tempfile.writeline("��ǰ��������" & computername)

'���� 
'set board =objwmiservice.execQuery("select * from win32_baseboard") 
'for each item in board 
'board2="����: " & item.Product & " " & item.SerialNumber
'next 
'tempfile.writeline(board2) 
Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
Set colItems = objWMIService.ExecQuery("Select   SerialNumber   From   Win32_BIOS")
For Each objItem In colItems
tempfile.writeline("����ţ�" & objItem.SerialNumber)
    Exit For
Next
Set colItems = Nothing

'BIOS
'tempfile.writeline("BIOS��")
'Set WMI = GetObject("Winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")
'On Error Resume Next
'For Each TempObj In WMI.InstancesOf("Win32_BIOS")
'	With TempObj
'		tempfile.writeline( "	����:" & .Manufacturer)
'		tempfile.writeline( "	����:" & .ReleaseDate)
'		tempfile.writeline( "	OEM �汾:" & .Version)
'		tempfile.writeline( "	BIOS �汾:" & .SMBIOSBIOSVersion)
'	End With
'Next

'����ϵͳ
tempfile.write("����ϵͳ��")
Set WMI = GetObject("Winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")
For Each TempObj in WMI.InstancesOf("Win32_OperatingSystem")
	With TempObj
		tempfile.write( " " & .Caption)
		tempfile.Write( " " & X86orX64())
		tempfile.write( " " & .CSDVersion)
	End With
Next

Function X86orX64()
    On Error Resume Next
    strComputer = "."
    Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
    Set colItems = objWMIService.ExecQuery("Select * from Win32_ComputerSystem",,48)
    
    For Each objItem in colItems
        If InStr(objItem.SystemType, "86") <> 0 Then
            X86orX64 = "x86"
        ElseIf InStr(objItem.SystemType, "64") <> 0 Then
            X86orX64 = "x64"
        Else
            X86orX64 = objItem.SystemType
        End If
    Next    
End Function
	
tempfile.writeline( "")

'CPU 
set cpu =objwmiservice.execQuery("select * from win32_processor") 
for each item in cpu 
cpu2= "CPU : " & item.Name 
next 
tempfile.writeline(cpu2) 

'�ڴ� 
Set colItems = objWMIService.ExecQuery("Select * from Win32_PhysicalMemory",,48) 
For Each objItem in colItems 
a=objitem.capacity/1048576 
temp=temp+objitem.capacity 
n=n+1 
Next 
memory=temp/1048576 
if n=1 then 
memory2= "�ڴ�: " & n & "��" &a&"M" 
else 
memory2= "�ڴ�: " & n & "��" &a&"M"&" �ܼ�"&memory&"M" 
end if 
tempfile.writeline(memory2) 

TempArr = Split("Unknown Other DRAM Synchronous-DRAM Cache-DRAM EDO EDRAM VRAM SRAM RAM ROM Flash EEPROM FEPROM EPROM CDRAM 3DRAM SDRAM SGRAM RDRAM DDR DDR-2")
For Each TempObj In WMI.InstancesOf("Win32_PhysicalMemory")
	With TempObj
		tempfile.write( "	" & .DeviceLocator)
		tempfile.write( "	" & .Capacity / 1048576 & "MB")
		tempfile.write( "	" & .Speed & "MHz")
		tempfile.write( "	" & .Manufacturer)
		tempfile.write( "	" & .PartNumber)
		tempfile.WriteLine("")
	End With
Next


'Ӳ�� 
tempfile.writeline("Ӳ��: ")
set disk =objwmiservice.execQuery("select * from win32_diskdrive") 
for each item in disk 
tempfile.writeline("	" & item.model & "	" & FormatNumber(item.Size / 1000000000, 2, True) & "GB" & "	" & item.SerialNumber & "	" & item.Manufacturer)
next 

'tempfile.writeline("�������: ")
'Set objFSO = CreateObject("Scripting.FileSystemObject")  
'Set colDrives = objFSO.Drives    
'For Each objDrive in colDrives    
 '   'If objDrive.IsReady = True Then 
'	    If objDrive.DriveType = 2 Then
 '       tempfile.write( "	�̷�:" & objDrive.DriveLetter  & "	")  
  '      tempfile.write( "���к�:" & objDrive.SerialNumber   & "	" )   
'		tempfile.write( "����:" & Round(objDrive.TotalSize/1024/1024/1024,2) & "GB")
'		tempfile.writeline( ""  )  
'		End If	      
    'End If   
'Next   



'�Կ� 
set video =objwmiservice.execQuery("select * from win32_videocontroller",,48) 
for each item in video 
video2= "�Կ�: " & item.AdapterCompatibility & "/" & item.Description 
next 

tempfile.writeline(video2) 

'���� 
tempfile.writeline("������")
Dim mac_adss, mac_16
Dim i, mac_len
Dim oAdapters, oAdapter
Set oAdapters = GetObject("winmgmts:").ExecQuery("SELECT * FROM Win32_NetworkAdapterConfiguration WHERE (MACAddress Is Not NULL)")
For Each oAdapter In oAdapters
If InStr(oAdapter.Description,"Virtual")=0 Then 
		If InStr(oAdapter.Description,"Teredo")=0 Then
			If InStr(oAdapter.Description,"Ethernet")<>0 Then 
				tempfile.writeline("	����������" & Replace(oAdapter.MACAddress, ":", "-") & " " & oAdapter.Description )
			ElseIf InStr(oAdapter.Description,"Wireless")<>0 Then
				tempfile.writeline("	����������" & Replace(oAdapter.MACAddress, ":", "-") & " " & oAdapter.Description )
			Else
				tempfile.writeline("	����������" & Replace(oAdapter.MACAddress, ":", "-") & " " & oAdapter.Description )
		End if
	End If
End If
next
mac=mac_adss
tempfile.writeline(GetIPMAC("."))




'��ȡ�����Ϣ
'tempfile.writeline("����б�") 

'On Error Resume Next       

'Const HKLM         = &H80000002   
'Const strKeyPath   = "Software\Microsoft\Windows\CurrentVersion\Uninstall\"
'Const ForReading   = 1   
'Const ForAppending = 8

'Dim WshNetwork
'Set WshNetwork = WScript.CreateObject("WScript.Network")
'strComputer = WshNetwork.ComputerName 

'Do      
'Set objReg  = GetObject("winmgmts://" & strComputer & "/root/default:StdRegProv")   
'objReg.EnumKey HKLM, strKeyPath,arrSubKeys    

'  For Each strSubKey In arrSubKeys        
 '   intRet = objReg.GetStringValue(HKLM, strKeyPath & strSubKey,"DisplayName",strValue)                               
'
 '       If strValue <> "" And intRet = 0 And inStr(1,strValue,"windows",1)<=0 Then
  '              tempfile.writeline("	" & strValue)
   '          End If                  

        
'         If strValue <> "" And intRet = 0 And inStr(1,strValue,"Java",1) >0 Then
 '               tempfile.writeline("	" & strValue)
  '           End If                  
'
 'Next

'Loop Until objFile.AtEndOfStream       
'textWriteFile.Close   
'objFile.Close