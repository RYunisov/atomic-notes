# Libvirt

Linux virtualization tool

## Tips

List of domain

```bash

# virsh list --all

```

Update config of VM

```bash

# virsh edit <VM>

```

Clone VM

> Note: VM have to stopped

```bash

# virt-clone --original <name_of_vm> --name <name_of_vm> --file <new_path_to_image_vm>

```

Extend disk on the fly

> Shutdown VM isn't require

- Identify disk, which do you want to extend

```bash

# virsh domblklist <name_of_vm>
 Target   Source
--------------------------------
 vda      /volumes/disk01.qcow2

```

- Using name for `Target` and `VM name` define a new size.

> Usually `size` define in KB

```bash

# virsh blockresize <name_of_vm> vda 500G
Block device 'vda' is resized

```

- Check updated size

```bash

# qemu-img info /volumes/disk01.qcow2 --force-share

```
