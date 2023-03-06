import subprocess


_drive_info = {}


def get_disk_info():
    _powershell_cmd = 'Get-PhysicalDisk'
    _result = subprocess.run(['powershell.exe', '-Command', _powershell_cmd], capture_output=True, text=True)
    _lines = _result.stdout.split('\n')
    _lines = [_line.strip() for _line in _lines if _line.strip()]

    # Vrem doar ultima linie care contine informatiile despre drive
    _res = _lines.pop(-1).split()
    _drive_info['Number'] = _res[0]
    _drive_info['ModelName'] = _res[1]
    _drive_info['SerialNumber'] = _res[2]
    _drive_info['Type'] = _res[3]
    _drive_info['CanPool'] = _res[4]
    _drive_info['OperationalStatus'] = _res[5]
    _drive_info['HealthStatus'] = _res[6]
    return _drive_info
