# Writeblock USB in Windows OS

import _winreg as wreg

key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Control\\StorageDevicePolicies")

# prints 'testsubkey'
# Create new value
wreg.SetValueEx(key, 'WriteProtect', 0, wreg.REG_DWORD, 1)
print wreg.QueryValueEx(key,'WriteProtect')
# prints (u'testvalue', 1)
key.Close()

# HKLM\System\CurrentControlSet\Control\StorageDevicePolicies" 
# /t Reg_dword /v WriteProtect /f /d 1