# Encountered challanges during Ansible upgrade.

## Ansible-core 2.17.7 and Python 3.8 on Ubuntu18.04

Issue:

By default ubuntu18.04 has preinstalled python3.6. However Ansible 2.17.7 requires Python 3.7 or above on target host. 

(Link to Ansible Matrix)[https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix]

However, ansible 2.17.7 still uses `/usr/bin/python3` instead takes the defined `ansible_python_interpreter` variable.

Error in due execution:

    Traceback (most recent call last):
      File "<stdin>", line 107, in <module>
      File "<stdin>", line 99, in _ansiballz_main
      File "<stdin>", line 44, in invoke_module
      File "<frozen importlib._bootstrap>", line 971, in _find_and_load
      File "<frozen importlib._bootstrap>", line 951, in _find_and_load_unlocked
      File "<frozen importlib._bootstrap>", line 894, in _find_spec
      File "<frozen importlib._bootstrap_external>", line 1157, in find_spec
      File "<frozen importlib._bootstrap_external>", line 1131, in _get_spec
      File "<frozen importlib._bootstrap_external>", line 1112, in _legacy_get_spec
      File "<frozen importlib._bootstrap>", line 441, in spec_from_loader
      File "<frozen importlib._bootstrap_external>", line 544, in spec_from_file_location
      File "/tmp/ansible_setup_payload_gkarwtna/ansible_setup_payload.zip/ansible/module_utils/basic.py", line 5
    SyntaxError: future feature annotations is not defined

Solution #1:

To install python3.8 via apt and OS has two python versions python3.6 and python3.8.

    apt install python3.8

Install python3-apt

    apt install python3-apt

Update symlinks for packages

    cd /usr/lib/python3/dist-packages
    ln -s apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.so
    ln -s apt_inst.cpython-36m-x86_64-linux-gnu.so apt_inst.so

Solution #2: 

Update symlink for python3

    ln -s /usr/bin/python3.8 /usr/bin/python3

## Ansible-core 2.17.7 and Ubuntu24.04

Issue:

    ***********************************************************************************************
    fatal: [HOSTNAME]: FAILED! => changed=false 
      cmd:
      - /usr/bin/python3
      - -m
      - pip.__main__
      - install
      - stormssh
      - pyopenssl
      msg: |-
        stdout: Collecting stormssh
          Using cached stormssh-0.7.0-py3-none-any.whl
        Requirement already satisfied: pyopenssl in /usr/local/lib/python3.12/dist-packages (25.0.0)
        Collecting flask (from stormssh)
          Using cached flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
        Collecting paramiko (from stormssh)
          Using cached paramiko-3.5.0-py3-none-any.whl.metadata (4.4 kB)
        Requirement already satisfied: six in /usr/lib/python3/dist-packages (from stormssh) (1.16.0)
        Requirement already satisfied: termcolor in /usr/local/lib/python3.12/dist-packages (from stormssh) (2.5.0)
        Requirement already satisfied: cryptography<45,>=41.0.5 in /usr/lib/python3/dist-packages (from pyopenssl) (41.0.7)
        Requirement already satisfied: typing-extensions>=4.9 in /usr/local/lib/python3.12/dist-packages (from pyopenssl) (4.12.2)
        Requirement already satisfied: Werkzeug>=3.1 in /usr/local/lib/python3.12/dist-packages (from flask->stormssh) (3.1.3)
        Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.12/dist-packages (from flask->stormssh) (3.1.5)
        Requirement already satisfied: itsdangerous>=2.2 in /usr/local/lib/python3.12/dist-packages (from flask->stormssh) (2.2.0)
        Requirement already satisfied: click>=8.1.3 in /usr/lib/python3/dist-packages (from flask->stormssh) (8.1.6)
        Collecting blinker>=1.9 (from flask->stormssh)
          Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
        Requirement already satisfied: bcrypt>=3.2 in /usr/lib/python3/dist-packages (from paramiko->stormssh) (3.2.2)
        Requirement already satisfied: pynacl>=1.5 in /usr/lib/python3/dist-packages (from paramiko->stormssh) (1.5.0)
        Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from Jinja2>=3.1.2->flask->stormssh) (3.0.2)
        Requirement already satisfied: cffi>=1.4.1 in /usr/local/lib/python3.12/dist-packages (from pynacl>=1.5->paramiko->stormssh) (1.17.1)
        Requirement already satisfied: pycparser in /usr/local/lib/python3.12/dist-packages (from cffi>=1.4.1->pynacl>=1.5->paramiko->stormssh) (2.22)
        Using cached flask-3.1.0-py3-none-any.whl (102 kB)
        Using cached paramiko-3.5.0-py3-none-any.whl (227 kB)
        Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
        Installing collected packages: blinker, flask, paramiko, stormssh
          Attempting uninstall: blinker
            Found existing installation: blinker 1.7.0
  
        :stderr: ERROR: Cannot uninstall blinker 1.7.0, RECORD file not found. Hint: The package was installed by debian.

Cause:

The `blinker` package was installed via apt repository instead pip.

Solution #1: More safety way.

Determinate the package that is used as a dependency and try to install via `apt`. In our case, the `Flask` version 3.1.0 requires `blinker` version 1.9.0. However `blinker` package was installed via `apt` and python cannon overwrite it. If install `Flask` package via apt repository it will install `Flask` version 3.0.2 version which works with `blinker` version 1.7.0.

Solution #2: Less safety way.

Lets using directly execution `pip` with param as `--break-system-packages`

    pip install --force-reinstall blinker==1.9.0 --break-system-packages
