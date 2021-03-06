# efi-monitor

A simple utility to handle efi dump files.  These variables look something like `/sys/firmware/efi/efivars/dump-type0-11-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0` and cause me to get a message on boot that "Non-volatile memory is almost full" and blocks directly booting.

## Usage

```bash
sudo su
pip install efi-monitor
efi-check  # will list dump files if they exist
efi-clear  # will delete dump files if they exist
```

### Usage Example

```bash
user@machine:~$ efi-check 
/sys/firmware/efi/efivars/dump-type0-11-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-10-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-9-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-8-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-7-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-6-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-5-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-4-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-3-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-2-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
/sys/firmware/efi/efivars/dump-type0-1-1-1645468022-C-cfc8fc79-be2e-4ddc-97f0-9f98bfe298a0
user@machine:~$ sudo su
[sudo] password for user: 
root@machine:~# efi-clear
```
