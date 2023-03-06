#include <Windows.h>
#include <WinIoCtl.h>
#include <iostream>

int main()
{
    HANDLE hDevice = CreateFile("\\\\.\\PhysicalDrive0", GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE, nullptr, OPEN_EXISTING, 0, nullptr);
    if (hDevice == INVALID_HANDLE_VALUE)
    {
        std::cerr << "Failed to open device\n";
        return 1;
    }

    STORAGE_PROPERTY_QUERY query{};
    query.PropertyId = StorageDeviceMediaType;
    query.QueryType = PropertyStandardQuery;

    char outputBuffer[sizeof(STORAGE_PROPERTY_QUERY) + sizeof(STORAGE_MEDIA_TYPE)];
    DWORD bytesReturned;

    if (DeviceIoControl(hDevice, IOCTL_STORAGE_QUERY_PROPERTY, &query, sizeof(query), &outputBuffer, sizeof(outputBuffer), &bytesReturned, nullptr))
    {
        STORAGE_MEDIA_TYPE mediaType = *reinterpret_cast<STORAGE_MEDIA_TYPE*>(outputBuffer + sizeof(STORAGE_PROPERTY_QUERY));
        if (mediaType == FixedMedia)
        {
            std::cout << "Hard Disk Drive\n";
        }
        else if (mediaType == SSDMedia)
        {
            std::cout << "Solid State Drive\n";
        }
        else
        {
            std::cout << "Unknown media type\n";
        }
    }
    else
    {
        std::cerr << "Failed to query device property\n";
    }

    CloseHandle(hDevice);

    return 0;
}