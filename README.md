# witness-demo

You need to install [witness](https://github.com/in-toto/witness) before try this demo.

## Create a Keypair

```
openssl genpkey -algorithm ed25519 -outform PEM -out witness-demo-key.pem
openssl pkey -in witness-demo-key.pem -pubout > witness-demo-pub.pem
```

## Create a Witness configuration

My .witness.yaml 

```
run:
    signer-file-key-path: witness-demo-key.pem
    trace: false
verify:
    attestations:
        - "witness-demo-att.json"
    policy: policy-signed.json
    publickey: witness-demo-pub.pem
```

## Record attestations for a build step

```
witness run --step build -o witness-demo-att.json -- python3 -m pip wheel --no-deps -w dist .
INFO    Using config file: .witness.yaml             
INFO    Starting environment attestor...             
INFO    Starting git attestor...                     
INFO    Starting material attestor...                
INFO    Starting command-run attestor...             
Processing /home/sxp/repos/witness-demo
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Building wheels for collected packages: witness-demo
  Building wheel for witness-demo (pyproject.toml): started
  Building wheel for witness-demo (pyproject.toml): finished with status 'done'
  Created wheel for witness-demo: filename=witness_demo-1.0.0-py3-none-any.whl size=1610 sha256=4561d6472108c331a6e103289d4c4f84f6cfbc37b7e9ac1e549daf20c8cef1c8
  Stored in directory: /home/sxp/.cache/pip/wheels/fe/5f/32/50e3d6d64ea6b8d52df092e797dab9017663331d4db3080ef5
Successfully built witness-demo
```

## View the attestation data in the signed DSSE Envelope

```
cat witness-demo-att.json | jq -r .payload | base64 -d | jq
```

<details>

<summary>More output can be found here</summary>

```
{
  "_type": "https://in-toto.io/Statement/v0.1",
  "subject": [
    {
      "name": "https://witness.dev/attestations/product/v0.1/file:witness_demo.egg-info/SOURCES.txt",
      "digest": {
        "gitoid:sha1": "gitoid:blob:sha1:0f3903d312df981e40bcd395d666624dd678bfed",
        "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
        "sha256": "293655a12e7707c98ccb75f16a48b4c082edc9932c055b885c6674cd65fcc9d9"
      }
    },
    {
      "name": "https://witness.dev/attestations/product/v0.1/file:witness_demo.egg-info/dependency_links.txt",
      "digest": {
        "gitoid:sha1": "gitoid:blob:sha1:8b137891791fe96927ad78e64b0aad7bded08bdc",
        "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
        "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
      }
    },
    {
      "name": "https://witness.dev/attestations/product/v0.1/file:witness_demo.egg-info/top_level.txt",
      "digest": {
        "gitoid:sha1": "gitoid:blob:sha1:ba2906d0666cf726c7eaadd2cd3db615dedfdf3a",
        "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
        "sha256": "6403203dd5a0867eb14d104ee8a73730bd72dd9ad92e78d996a6dba0a5dcfc01"
      }
    },
    {
      "name": "https://witness.dev/attestations/git/v0.1/commithash:",
      "digest": {
        "sha1": ""
      }
    },
    {
      "name": "https://witness.dev/attestations/git/v0.1/committeremail:",
      "digest": {
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
      }
    },
    {
      "name": "https://witness.dev/attestations/product/v0.1/file:witness_demo.egg-info/PKG-INFO",
      "digest": {
        "gitoid:sha1": "gitoid:blob:sha1:ec96d66beb84ac1915fc021e820b432d523b95b6",
        "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
        "sha256": "fce3ca38c0ed1a28068b649979d0461437cf5900839004e9b67bde0cabc00f9f"
      }
    },
    {
      "name": "https://witness.dev/attestations/git/v0.1/authoremail:",
      "digest": {
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
      }
    },
    {
      "name": "https://witness.dev/attestations/product/v0.1/file:build/lib/main.py",
      "digest": {
        "gitoid:sha1": "gitoid:blob:sha1:5b8dc5a0dbc7c44e96e4ec461998a312f45e7696",
        "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
        "sha256": "97e056598e144eb6ef7dfcb7c419edfdbefc8318a1ca5cca17379608974eeb66"
      }
    },
    {
      "name": "https://witness.dev/attestations/product/v0.1/file:dist/witness_demo-1.0.0-py3-none-any.whl",
      "digest": {
        "gitoid:sha1": "gitoid:blob:sha1:76ff9ae03ef9336117decb31af14ea2dfa46b2d9",
        "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
        "sha256": "4561d6472108c331a6e103289d4c4f84f6cfbc37b7e9ac1e549daf20c8cef1c8"
      }
    }
  ],
  "predicateType": "https://witness.testifysec.com/attestation-collection/v0.1",
  "predicate": {
    "name": "build",
    "attestations": [
      {
        "type": "https://witness.dev/attestations/environment/v0.1",
        "attestation": {
          "os": "linux",
          "hostname": "PF4AY3A5",
          "username": "sxp",
          "variables": {
            " IFS": "$_mlIFS;\n else\n unset IFS;\n fi;\n unset _mlre _mlv _mlrv _mlIFS;\n if [ -n \"${_mlshdbg:-}\" ]; then\n set -$_mlshdbg;\n fi;\n unset _mlshdbg;\n return $_mlstatus\n}",
            " MODULES_USE_COMPAT_VERSION": "1;\n export MODULES_USE_COMPAT_VERSION;\n fi;\n fi;\n if [ $swfound -eq 0 ]; then\n echo \"Switching to Modules $swname version\";\n source /usr/share/Modules/init/bash;\n else\n echo \"Cannot switch to Modules $swname version, command not found\";\n return 1;\n fi\n}",
            " _mlIFS": "$IFS;\n fi;",
            " _mlre": "\"${_mlre:-}${_mlv}='`eval 'echo ${'$_mlrv':-}'`' \";\n fi;\n done;\n if [ -n \"${_mlre:-}\" ]; then\n eval `eval ${_mlre} /usr/bin/tclsh /usr/share/Modules/libexec/modulecmd.tcl bash '\"$@\"'`;\n else\n eval `/usr/bin/tclsh /usr/share/Modules/libexec/modulecmd.tcl bash \"$@\"`;\n fi;",
            " _mlrv": "\"MODULES_RUNENV_${_mlv}\";",
            " _mlshdbg": "''\n ;;\n esac;\n fi;\n unset _mlre _mlIFS;\n if [ -n \"${IFS+x}\" ]; then",
            " _mlstatus": "$?;\n if [ -n \"${_mlIFS+x}\" ]; then",
            " if [ \"${MODULES_SILENT_SHELL_DEBUG:-0}\" ": " '1' ]; then\n case \"$-\" in \n *v*x*)\n set +vx;",
            " if [ \"${MODULES_USE_COMPAT_VERSION:-0}\" ": " '1' ]; then",
            " if [ \"${_mlv}\" ": " \"${_mlv##*[!A-Za-z0-9_]}\" -a \"${_mlv}\" = \"${_mlv#[0-9]}\" ]; then\n if [ -n \"`eval 'echo ${'$_mlv'+x}'`\" ]; then",
            " typeset swfound": "0;",
            " typeset swname": "'compatibility';\n if [ -e /usr/share/Modules/libexec/modulecmd-compat ]; then",
            "BASH_FUNC__module_raw%%": "() {  unset _mlshdbg;",
            "BASH_FUNC_ml%%": "() {  module ml \"$@\"\n}",
            "BASH_FUNC_module%%": "() {  _module_raw \"$@\" 2>&1\n}",
            "BASH_FUNC_scl%%": "() {  if [ \"$1\" = \"load\" -o \"$1\" = \"unload\" ]; then\n eval \"module $@\";\n else\n /usr/bin/scl \"$@\";\n fi\n}",
            "BASH_FUNC_switchml%%": "() {  typeset swfound=1;",
            "COLORTERM": "truecolor",
            "DISPLAY": ":0",
            "GIT_ASKPASS": "/home/sxp/.vscode-server/bin/1a5daa3a0231a0fbba4f14db7ec463cf99d7768e/extensions/git/dist/askpass.sh",
            "HISTCONTROL": "ignoredups",
            "HISTSIZE": "1000",
            "HOME": "/home/sxp",
            "HOSTNAME": "RS-PF4AY3A5",
            "HOSTTYPE": "x86_64",
            "LANG": "C.utf8",
            "LESSOPEN": "||/usr/bin/lesspipe.sh %s",
            "LOADEDMODULES": "",
            "LOGNAME": "sxp",
            "LS_COLORS": "rs=0:di=38;5;33:ln=38;5;51:mh=00:pi=40;38;5;11:so=38;5;13:do=38;5;5:bd=48;5;232;38;5;11:cd=48;5;232;38;5;3:or=48;5;232;38;5;9:mi=01;05;37;41:su=48;5;196;38;5;15:sg=48;5;11;38;5;16:ca=48;5;196;38;5;226:tw=48;5;10;38;5;16:ow=48;5;10;38;5;21:st=48;5;21;38;5;15:ex=38;5;40:*.tar=38;5;9:*.tgz=38;5;9:*.arc=38;5;9:*.arj=38;5;9:*.taz=38;5;9:*.lha=38;5;9:*.lz4=38;5;9:*.lzh=38;5;9:*.lzma=38;5;9:*.tlz=38;5;9:*.txz=38;5;9:*.tzo=38;5;9:*.t7z=38;5;9:*.zip=38;5;9:*.z=38;5;9:*.dz=38;5;9:*.gz=38;5;9:*.lrz=38;5;9:*.lz=38;5;9:*.lzo=38;5;9:*.xz=38;5;9:*.zst=38;5;9:*.tzst=38;5;9:*.bz2=38;5;9:*.bz=38;5;9:*.tbz=38;5;9:*.tbz2=38;5;9:*.tz=38;5;9:*.deb=38;5;9:*.rpm=38;5;9:*.jar=38;5;9:*.war=38;5;9:*.ear=38;5;9:*.sar=38;5;9:*.rar=38;5;9:*.alz=38;5;9:*.ace=38;5;9:*.zoo=38;5;9:*.cpio=38;5;9:*.7z=38;5;9:*.rz=38;5;9:*.cab=38;5;9:*.wim=38;5;9:*.swm=38;5;9:*.dwm=38;5;9:*.esd=38;5;9:*.jpg=38;5;13:*.jpeg=38;5;13:*.mjpg=38;5;13:*.mjpeg=38;5;13:*.gif=38;5;13:*.bmp=38;5;13:*.pbm=38;5;13:*.pgm=38;5;13:*.ppm=38;5;13:*.tga=38;5;13:*.xbm=38;5;13:*.xpm=38;5;13:*.tif=38;5;13:*.tiff=38;5;13:*.png=38;5;13:*.svg=38;5;13:*.svgz=38;5;13:*.mng=38;5;13:*.pcx=38;5;13:*.mov=38;5;13:*.mpg=38;5;13:*.mpeg=38;5;13:*.m2v=38;5;13:*.mkv=38;5;13:*.webm=38;5;13:*.ogm=38;5;13:*.mp4=38;5;13:*.m4v=38;5;13:*.mp4v=38;5;13:*.vob=38;5;13:*.qt=38;5;13:*.nuv=38;5;13:*.wmv=38;5;13:*.asf=38;5;13:*.rm=38;5;13:*.rmvb=38;5;13:*.flc=38;5;13:*.avi=38;5;13:*.fli=38;5;13:*.flv=38;5;13:*.gl=38;5;13:*.dl=38;5;13:*.xcf=38;5;13:*.xwd=38;5;13:*.yuv=38;5;13:*.cgm=38;5;13:*.emf=38;5;13:*.ogv=38;5;13:*.ogx=38;5;13:*.aac=38;5;45:*.au=38;5;45:*.flac=38;5;45:*.m4a=38;5;45:*.mid=38;5;45:*.midi=38;5;45:*.mka=38;5;45:*.mp3=38;5;45:*.mpc=38;5;45:*.ogg=38;5;45:*.ra=38;5;45:*.wav=38;5;45:*.oga=38;5;45:*.opus=38;5;45:*.spx=38;5;45:*.xspf=38;5;45:",
            "MAIL": "/var/spool/mail/sxp",
            "MANPATH": "/home/sxp/.nvm/versions/node/v20.6.0/share/man::",
            "MODULEPATH": "/etc/scl/modulefiles:/usr/share/Modules/modulefiles:/etc/modulefiles:/usr/share/modulefiles",
            "MODULEPATH_modshare": "/usr/share/Modules/modulefiles:2:/etc/modulefiles:2:/usr/share/modulefiles:2",
            "MODULESHOME": "/usr/share/Modules",
            "MODULES_CMD": "/usr/share/Modules/libexec/modulecmd.tcl",
            "MODULES_RUN_QUARANTINE": "LD_LIBRARY_PATH LD_PRELOAD",
            "NAME": "Code",
            "NVM_BIN": "/home/sxp/.nvm/versions/node/v20.6.0/bin",
            "NVM_CD_FLAGS": "",
            "NVM_DIR": "/home/sxp/.nvm",
            "NVM_INC": "/home/sxp/.nvm/versions/node/v20.6.0/include/node",
            "PATH": "/home/sxp/.fzf/bin:/home/sxp/.vscode-server/bin/1a5daa3a0231a0fbba4f14db7ec463cf99d7768e/bin/remote-cli:/home/sxp/.nvm/versions/node/v20.6.0/bin:/home/sxp/.local/bin:/home/sxp/bin:/usr/share/Modules/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/Python39/Scripts/:/mnt/c/Python39/:/mnt/c/Windows/system32:/mnt/c/Windows:/mnt/c/Windows/System32/Wbem:/mnt/c/Windows/System32/WindowsPowerShell/v1.0/:/mnt/c/Windows/System32/OpenSSH/:/mnt/c/cygwin64/bin:/mnt/c/ProgramData/chocolatey/bin:/mnt/c/U2/UV/BIN:/mnt/c/Program Files/PuTTY/:/mnt/c/Program Files/Git/cmd:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/c/Program Files/PowerShell/7/:/mnt/c/Users/sxp/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/sxp/AppData/Local/Programs/Microsoft VS Code/bin",
            "PULSE_SERVER": "unix:/mnt/wslg/PulseServer",
            "PWD": "/home/sxp/repos/witness-demo",
            "SHELL": "/bin/bash",
            "SHLVL": "4",
            "TERM": "xterm-256color",
            "TERM_PROGRAM": "vscode",
            "TERM_PROGRAM_VERSION": "1.84.2",
            "USER": "sxp",
            "VSCODE_GIT_ASKPASS_EXTRA_ARGS": "",
            "VSCODE_GIT_ASKPASS_MAIN": "/home/sxp/.vscode-server/bin/1a5daa3a0231a0fbba4f14db7ec463cf99d7768e/extensions/git/dist/askpass-main.js",
            "VSCODE_GIT_ASKPASS_NODE": "/home/sxp/.vscode-server/bin/1a5daa3a0231a0fbba4f14db7ec463cf99d7768e/node",
            "VSCODE_GIT_IPC_HANDLE": "/mnt/wslg/runtime-dir/vscode-git-7ab40e3bfa.sock",
            "VSCODE_INJECTION": "1",
            "VSCODE_IPC_HOOK_CLI": "/mnt/wslg/runtime-dir/vscode-ipc-4a86bfcb-7a74-443b-acf7-4eecdad4b3d9.sock",
            "WAYLAND_DISPLAY": "wayland-0",
            "WSL2_GUI_APPS_ENABLED": "1",
            "WSLENV": "ELECTRON_RUN_AS_NODE/w:WT_SESSION:WT_PROFILE_ID:",
            "WSL_DISTRO_NAME": "AlmaLinux-8",
            "WSL_INTEROP": "/run/WSL/347_interop",
            "WSL_PAC_URL": "http://proxy.rocketsoftware.com:8081/proxy.pac",
            "WT_PROFILE_ID": "{809c0a51-3bb6-5c2b-93d9-741099225673}",
            "WT_SESSION": "c87acd8b-9f82-48eb-b99d-3410b013536a",
            "XDG_DATA_DIRS": "/usr/local/share:/usr/share:/home/sxp/.vscode-server/bin/1a5daa3a0231a0fbba4f14db7ec463cf99d7768e/out/vs/workbench/contrib/terminal/browser/media/fish_xdg_data",
            "XDG_RUNTIME_DIR": "/mnt/wslg/runtime-dir",
            "which_declare": "declare -f"
          }
        },
        "starttime": "2023-11-23T17:33:50.275765903+08:00",
        "endtime": "2023-11-23T17:33:50.275836135+08:00"
      },
      {
        "type": "https://witness.dev/attestations/git/v0.1",
        "attestation": {
          "commithash": "",
          "author": "",
          "authoremail": "",
          "committername": "",
          "committeremail": "",
          "commitdate": "",
          "commitmessage": ""
        },
        "starttime": "2023-11-23T17:33:50.275880975+08:00",
        "endtime": "2023-11-23T17:33:50.275957049+08:00"
      },
      {
        "type": "https://witness.dev/attestations/material/v0.1",
        "attestation": {
          ".git/HEAD": {
            "gitoid:sha1": "gitoid:blob:sha1:b870d82622c1a9ca6bcaf5df639680424a1904b0",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "28d25bf82af4c0e2b72f50959b2beb859e3e60b9630a5e8c603dad4ddb2b6e80"
          },
          ".git/config": {
            "gitoid:sha1": "gitoid:blob:sha1:c59e861ab315b8b0da04c5d075c7c5584af2a799",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "420ce663dc162c13dc2abca166dfb3c1ef7aaa6a28d2ed1b273955a92a2e3fb1"
          },
          ".git/description": {
            "gitoid:sha1": "gitoid:blob:sha1:498b267a8c7812490d6479839c5577eaaec79d62",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "85ab6c163d43a17ea9cf7788308bca1466f1b0a8d1cc92e26e9bf63da4062aee"
          },
          ".git/hooks/applypatch-msg.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:a5d7b84a673458d14d9aab082183a1968c2c7492",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "0223497a0b8b033aa58a3a521b8629869386cf7ab0e2f101963d328aa62193f7"
          },
          ".git/hooks/commit-msg.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:b58d1184a9d43a39c0d95f32453efc78581877d6",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "1f74d5e9292979b573ebd59741d46cb93ff391acdd083d340b94370753d92437"
          },
          ".git/hooks/fsmonitor-watchman.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:23e856f5deeb7f564afc22f2beed54449c2d3afb",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "e0549964e93897b519bd8e333c037e51fff0f88ba13e086a331592bf801fa1d0"
          },
          ".git/hooks/post-update.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:ec17ec1939b7c3e86b7cb6c0c4de6b0818a7e75e",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "81765af2daef323061dcbc5e61fc16481cb74b3bac9ad8a174b186523586f6c5"
          },
          ".git/hooks/pre-applypatch.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:4142082bcb939bbc17985a69ba748491ac6b62a5",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "e15c5b469ea3e0a695bea6f2c82bcf8e62821074939ddd85b77e0007ff165475"
          },
          ".git/hooks/pre-commit.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:e144712c85c055bcf3248ab342592b440a477062",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "f9af7d95eb1231ecf2eba9770fedfa8d4797a12b02d7240e98d568201251244a"
          },
          ".git/hooks/pre-merge-commit.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:399eab1924e39da570b389b0bef1ca713b3b05c3",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "d3825a70337940ebbd0a5c072984e13245920cdf8898bd225c8d27a6dfc9cb53"
          },
          ".git/hooks/pre-push.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:4ce688d32b7532862767345f2b991ae856f7d4a8",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "ecce9c7e04d3f5dd9d8ada81753dd1d549a9634b26770042b58dda00217d086a"
          },
          ".git/hooks/pre-rebase.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:6cbef5c370d8c3486ca85423dd70440c5e0a2aa2",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "4febce867790052338076f4e66cc47efb14879d18097d1d61c8261859eaaa7b3"
          },
          ".git/hooks/pre-receive.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:a1fd29ec14823d8bc4a8d1a2cfe35451580f5118",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "a4c3d2b9c7bb3fd8d1441c31bd4ee71a595d66b44fcf49ddb310252320169989"
          },
          ".git/hooks/prepare-commit-msg.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:10fa14c5ab0134436e2ae435138bf921eb477c60",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "e9ddcaa4189fddd25ed97fc8c789eca7b6ca16390b2392ae3276f0c8e1aa4619"
          },
          ".git/hooks/push-to-checkout.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:af5a0c0018b5e9c04b56ac52f21b4d28f48d99ea",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "a53d0741798b287c6dd7afa64aee473f305e65d3f49463bb9d7408ec3b12bf5f"
          },
          ".git/hooks/update.sample": {
            "gitoid:sha1": "gitoid:blob:sha1:c4d426bc6ee9430ee7813263ce6d5da7ec78c3c6",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "8d5f2fa83e103cf08b57eaa67521df9194f45cbdbcb37da52ad586097a14d106"
          },
          ".git/info/exclude": {
            "gitoid:sha1": "gitoid:blob:sha1:a5196d1be8fb59edf8062bef36d3a602e0812139",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "6671fe83b7a07c8932ee89164d1f2793b2318058eb8b98dc5c06ee0a5a3b0ec1"
          },
          ".witness.yaml": {
            "gitoid:sha1": "gitoid:blob:sha1:adbdb0e9685cc0f4482e945000e68cb4be30bc48",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "3eeeeff859035dfc0565badd08acf2af3c099518ca56ea3f211b85dabe25635a"
          },
          "README.md": {
            "gitoid:sha1": "gitoid:blob:sha1:60929910bf95093cd21ba3497d619f689adb6f14",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "bada78eb03d04a7d4ff9548127fb3dca16415b557e67d80a90323d06566ceb7c"
          },
          "main.py": {
            "gitoid:sha1": "gitoid:blob:sha1:5b8dc5a0dbc7c44e96e4ec461998a312f45e7696",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "97e056598e144eb6ef7dfcb7c419edfdbefc8318a1ca5cca17379608974eeb66"
          },
          "setup.py": {
            "gitoid:sha1": "gitoid:blob:sha1:f6940284ffc870f13e0fb3cf49cdc4a5ce28c9ff",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "bdcedf7ddbccf941f31317732539725c36b098be493472bc70a154e2c1ef4787"
          },
          "witness-demo-att.json": {
            "gitoid:sha1": "gitoid:blob:sha1:e69de29bb2d1d6434b8b29ae775ad8c2e48c5391",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
          },
          "witness-demo-key.pem": {
            "gitoid:sha1": "gitoid:blob:sha1:8774e79f81b161298ec28af0ad4f844664d25b0a",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "fec44741506dae5fda49dfded95101b1e63e3a183737aacc7978cc953b486568"
          },
          "witness-demo-pub.pem": {
            "gitoid:sha1": "gitoid:blob:sha1:2fd180080f30e64a6cee8a6ed66cc835d2a4c9c7",
            "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
            "sha256": "5b7bd1c47cacd91d649e925e3a778c28c1320172f49bca724d88dab504f8bd2d"
          }
        },
        "starttime": "2023-11-23T17:33:50.275982932+08:00",
        "endtime": "2023-11-23T17:33:50.280586581+08:00"
      },
      {
        "type": "https://witness.dev/attestations/command-run/v0.1",
        "attestation": {
          "cmd": [
            "python3",
            "-m",
            "pip",
            "wheel",
            "--no-deps",
            "-w",
            "dist",
            "."
          ],
          "stdout": "Processing /home/sxp/repos/witness-demo\n  Installing build dependencies: started\n  Installing build dependencies: finished with status 'done'\n  Getting requirements to build wheel: started\n  Getting requirements to build wheel: finished with status 'done'\n  Preparing metadata (pyproject.toml): started\n  Preparing metadata (pyproject.toml): finished with status 'done'\nBuilding wheels for collected packages: witness-demo\n  Building wheel for witness-demo (pyproject.toml): started\n  Building wheel for witness-demo (pyproject.toml): finished with status 'done'\n  Created wheel for witness-demo: filename=witness_demo-1.0.0-py3-none-any.whl size=1610 sha256=4561d6472108c331a6e103289d4c4f84f6cfbc37b7e9ac1e549daf20c8cef1c8\n  Stored in directory: /home/sxp/.cache/pip/wheels/fe/5f/32/50e3d6d64ea6b8d52df092e797dab9017663331d4db3080ef5\nSuccessfully built witness-demo\n",
          "exitcode": 0
        },
        "starttime": "2023-11-23T17:33:50.280988377+08:00",
        "endtime": "2023-11-23T17:33:54.738961303+08:00"
      },
      {
        "type": "https://witness.dev/attestations/product/v0.1",
        "attestation": {
          "build/lib/main.py": {
            "mime_type": "text/x-python; charset=utf-8",
            "digest": {
              "gitoid:sha1": "gitoid:blob:sha1:5b8dc5a0dbc7c44e96e4ec461998a312f45e7696",
              "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
              "sha256": "97e056598e144eb6ef7dfcb7c419edfdbefc8318a1ca5cca17379608974eeb66"
            }
          },
          "dist/witness_demo-1.0.0-py3-none-any.whl": {
            "mime_type": "application/zip",
            "digest": {
              "gitoid:sha1": "gitoid:blob:sha1:76ff9ae03ef9336117decb31af14ea2dfa46b2d9",
              "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
              "sha256": "4561d6472108c331a6e103289d4c4f84f6cfbc37b7e9ac1e549daf20c8cef1c8"
            }
          },
          "witness_demo.egg-info/PKG-INFO": {
            "mime_type": "text/plain; charset=utf-8",
            "digest": {
              "gitoid:sha1": "gitoid:blob:sha1:ec96d66beb84ac1915fc021e820b432d523b95b6",
              "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
              "sha256": "fce3ca38c0ed1a28068b649979d0461437cf5900839004e9b67bde0cabc00f9f"
            }
          },
          "witness_demo.egg-info/SOURCES.txt": {
            "mime_type": "text/plain; charset=utf-8",
            "digest": {
              "gitoid:sha1": "gitoid:blob:sha1:0f3903d312df981e40bcd395d666624dd678bfed",
              "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
              "sha256": "293655a12e7707c98ccb75f16a48b4c082edc9932c055b885c6674cd65fcc9d9"
            }
          },
          "witness_demo.egg-info/dependency_links.txt": {
            "mime_type": "text/plain; charset=utf-8",
            "digest": {
              "gitoid:sha1": "gitoid:blob:sha1:8b137891791fe96927ad78e64b0aad7bded08bdc",
              "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
              "sha256": "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"
            }
          },
          "witness_demo.egg-info/top_level.txt": {
            "mime_type": "text/plain; charset=utf-8",
            "digest": {
              "gitoid:sha1": "gitoid:blob:sha1:ba2906d0666cf726c7eaadd2cd3db615dedfdf3a",
              "gitoid:sha256": "gitoid:blob:sha256:473a0f4c3be8a93681a267e3b1e9a7dcda1185436fe141f7749120a303721813",
              "sha256": "6403203dd5a0867eb14d104ee8a73730bd72dd9ad92e78d996a6dba0a5dcfc01"
            }
          }
        },
        "starttime": "2023-11-23T17:33:54.7390385+08:00",
        "endtime": "2023-11-23T17:33:54.747139335+08:00"
      }
    ]
  }
}
```
</details>

## Create a Policy File

See ![](policy.json)

## Replace the variables in the policy

```
id=`sha256sum witness-demo-pub.pem | awk '{print $1}'` && sed -i "s/{{PUBLIC_KEY_ID}}/$id/g" policy.json

pubb64=`cat witness-demo-pub.pem | base64 -w 0` && sed -i "s/{{B64_PUBLIC_KEY}}/$pubb64/g" policy.json

```

## Sign The Policy File

```
witness sign -f policy.json --signer-file-key-path witness-demo-key.pem --outfile policy-signed.json
INFO    Using config file: .witness.yaml
```

## Verify the Binary Meets Policy Requirements

```
witness verify -f dist/witness_demo-1.0.0-py3-none-any.whl -a witness-demo-att.json -p policy-signed.json -k witness-demo-pub.pem 
INFO    Using config file: .witness.yaml             
INFO    Verification succeeded                       
INFO    Evidence:                                    
INFO    0: witness-demo-att.json 
```
