'本脚本的功能是检测硬件的信息。 
On Error Resume Next 
temp=0 
set wshshell=wscript.createobject("wscript.shell") 
'启动WMI服务 
wshshell.run ("%comspec% /c regsvr32 /s scrrun.dll"),0,True 
wshshell.run ("%comspec% /c sc config winmgmt start= auto"),0,True 
wshshell.run ("%comspec% /c net start winmgmt"),0 

strComputer = "." 
Set objWMIService = Getobject("winmgmts:\\" & strComputer &"\root\cimv2") 

'用一个文本来记录硬件信息 
Set WshNetwork = WScript.Createobject("WScript.Network") 
computername=WshNetwork.ComputerName
username=WshNetwork.userName 

strTime=CStr(Year(Now()))&Right("0"&Month(Now()),2)&Right("0"&Day(Now()),2) & "_" & CStr(Right("0"&Hour(Now()),2)&Right("0"&Minute(Now()),2)&Right("0"&Second(Now()),2))
set fso=createobject("scripting.filesystemobject") 
tempfilerpath="c:\users\"& username & "desktop"
tempfilter=(tempfilepath & computername & "-" & strTime & ".txt") 
set tempfile=fso.createtextfile(tempfilter) 

systeminfo2="时间: " & now 
tempfile.writeline(systeminfo2)

'用户名
'Dim oFSO,oNetwork 
'Set oNetwork=CreateObject("Wscript.Network")  
tempfile.writeline("当前用户名：" & Username)
tempfile.writeline("当前机器名：" & computername)

'主板 
'set board =objwmiservice.execQuery("select * from win32_baseboard") 
'for each item in board 
'board2="主板: " & item.Product & " " & item.SerialNumber
'next 
'tempfile.writeline(board2) 
Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
Set colItems = objWMIService.ExecQuery("Select   SerialNumber   From   Win32_BIOS")
For Each objItem In colItems
tempfile.writeline("服务号：" & objItem.SerialNumber)
    Exit For
Next
Set colItems = Nothing

'BIOS
'tempfile.writeline("BIOS：")
'Set WMI = GetObject("Winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")
'On Error Resume Next
'For Each TempObj In WMI.InstancesOf("Win32_BIOS")
'	With TempObj
'		tempfile.writeline( "	厂商:" & .Manufacturer)
'		tempfile.writeline( "	日期:" & .ReleaseDate)
'		tempfile.writeline( "	OEM 版本:" & .Version)
'		tempfile.writeline( "	BIOS 版本:" & .SMBIOSBIOSVersion)
'	End With
'Next

'操作系统
tempfile.write("操作系统：")
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

'内存 
Set colItems = objWMIService.ExecQuery("Select * from Win32_PhysicalMemory",,48) 
For Each objItem in colItems 
a=objitem.capacity/1048576 
temp=temp+objitem.capacity 
n=n+1 
Next 
memory=temp/1048576 
if n=1 then 
memory2= "内存: " & n & "条" &a&"M" 
else 
memory2= "内存: " & n & "条" &a&"M"&" 总计"&memory&"M" 
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


'硬盘 
tempfile.writeline("硬盘: ")
set disk =objwmiservice.execQuery("select * from win32_diskdrive") 
for each item in disk 
tempfile.writeline("	" & item.model & "	" & FormatNumber(item.Size / 1000000000, 2, True) & "GB" & "	" & item.SerialNumber & "	" & item.Manufacturer)
next 

'tempfile.writeline("分区情况: ")
'Set objFSO = CreateObject("Scripting.FileSystemObject")  
'Set colDrives = objFSO.Drives    
'For Each objDrive in colDrives    
 '   'If objDrive.IsReady = True Then 
'	    If objDrive.DriveType = 2 Then
 '       tempfile.write( "	盘符:" & objDrive.DriveLetter  & "	")  
  '      tempfile.write( "序列号:" & objDrive.SerialNumber   & "	" )   
'		tempfile.write( "容量:" & Round(objDrive.TotalSize/1024/1024/1024,2) & "GB")
'		tempfile.writeline( ""  )  
'		End If	      
    'End If   
'Next   



'显卡 
set video =objwmiservice.execQuery("select * from win32_videocontroller",,48) 
for each item in video 
video2= "显卡: " & item.AdapterCompatibility & "/" & item.Description 
next 

tempfile.writeline(video2) 

'网卡 
tempfile.writeline("网卡：")
Dim mac_adss, mac_16
Dim i, mac_len
Dim oAdapters, oAdapter
Set oAdapters = GetObject("winmgmts:").ExecQuery("SELECT * FROM Win32_NetworkAdapterConfiguration WHERE (MACAddress Is Not NULL)")
For Each oAdapter In oAdapters
If InStr(oAdapter.Description,"Virtual")=0 Then 
		If InStr(oAdapter.Description,"Teredo")=0 Then
			If InStr(oAdapter.Description,"Ethernet")<>0 Then 
				tempfile.writeline("	有线网卡：" & Replace(oAdapter.MACAddress, ":", "-") & " " & oAdapter.Description )
			ElseIf InStr(oAdapter.Description,"Wireless")<>0 Then
				tempfile.writeline("	无线网卡：" & Replace(oAdapter.MACAddress, ":", "-") & " " & oAdapter.Description )
			Else
				tempfile.writeline("	其他网卡：" & Replace(oAdapter.MACAddress, ":", "-") & " " & oAdapter.Description )
		End if
	End If
End If
next
mac=mac_adss
tempfile.writeline(GetIPMAC("."))




'获取软件信息
'tempfile.writeline("软件列表：") 

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