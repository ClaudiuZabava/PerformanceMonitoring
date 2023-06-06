#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    DIR *dirp;
    struct dirent *directory;

    dirp = opendir("/proc");
    if (dirp) {
        while ((directory = readdir(dirp)) != NULL) {
            if (directory->d_type == DT_DIR && strcmp(directory->d_name, ".") != 0 && strcmp(directory->d_name, "..") != 0 &&
                (directory->d_name[0] >= '0' && directory->d_name[0] <= '9')) {
                printf("PID: %s\n", directory->d_name);

                char cmdline_file[256] = {0};
                snprintf(cmdline_file, sizeof(cmdline_file), "/proc/%s/cmdline", directory->d_name);

                FILE *fp = fopen(cmdline_file, "r");
                if (fp) {
                    char cmdline[256];
                    if (fgets(cmdline, sizeof(cmdline), fp) != NULL) {
                        printf("Nume: %s\n", cmdline);
                    }
                    fclose(fp);
                }

                printf("\n");
            }
        }

        closedir(dirp);
    }

    return(0);
}

//#include <windows.h>
//#include <cstdio>
//#include <tchar.h>
//#include <psapi.h>
//#include <tlhelp32.h>
//#include <sddl.h>
//
//
//void PrintProcessInfo(DWORD processID) {
//    TCHAR szProcessName[MAX_PATH] = TEXT("<unknown>");
//    HANDLE hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, processID);
//
//    if (NULL != hProcess) {
//        HMODULE hMod;
//        DWORD cbNeeded;
//        if (EnumProcessModules(hProcess, &hMod, sizeof(hMod), &cbNeeded)) {
//            GetModuleBaseName(hProcess, hMod, szProcessName, sizeof(szProcessName) / sizeof(TCHAR));
//        }
//
//        PROCESS_MEMORY_COUNTERS pmc;
//        if (GetProcessMemoryInfo(hProcess, &pmc, sizeof(pmc))) {
//            printf("\nProcess ID: %u\n", processID);
//            _tprintf(TEXT("Process Name: %s\n"), szProcessName);
//            printf("Memory Usage: %u\n", pmc.WorkingSetSize);
//        }
//        CloseHandle(hProcess);
//    }
//}
//
//void ListProcesses() {
//    DWORD aProcesses[1024], cbNeeded, cProcesses;
//
//    if (!EnumProcesses(aProcesses, sizeof(aProcesses), &cbNeeded)) {
//        return;
//    }
//
//    cProcesses = cbNeeded / sizeof(DWORD);
//    for (unsigned int i = 0; i < cProcesses; i++) {
//        if (aProcesses[i] != 0) {
//            PrintProcessInfo(aProcesses[i]);
//        }
//    }
//}
//
//void TerminateProcessAndChildren(DWORD processID) {
//    HANDLE hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
//    PROCESSENTRY32 pe = { 0 };
//    pe.dwSize = sizeof(PROCESSENTRY32);
//
//    if (Process32First(hSnap, &pe)) {
//        do {
//            if (pe.th32ParentProcessID == processID) {
//                TerminateProcessAndChildren(pe.th32ProcessID);
//            }
//        } while (Process32Next(hSnap, &pe));
//    }
//
//    HANDLE hProcess = OpenProcess(PROCESS_TERMINATE, FALSE, processID);
//    if (hProcess != NULL) {
//        TerminateProcess(hProcess, 0);
//        CloseHandle(hProcess);
//    }
//    CloseHandle(hSnap);
//}
//
//int main() {
//    printf("Listing processes...\n");
//    ListProcesses();
//
////    DWORD pid;
////    printf("Enter PID to terminate: ");
////    scanf("%d", &pid);
////
////    printf("Terminating process %d and its children...\n", pid);
////    TerminateProcessAndChildren(pid);
//
//
//    return 0;
//}
