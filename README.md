# AOs-PowerToys
PowerToys/Extentions for [AOs](https://github.com/SrijanSriv211/AOs) to extend its capabilities.


## How to Install
1. Copy-Paste the `Files.x72` directory from this repo inside the `AOs` directory where the executable is stored.
2. Open `cmd_schema.json` and copy all its contents:

```diff
"cmd_schema": [
-   {
-       "cmd_names": ["export"],
-       "help_message": "Export text from the console",
-       "usage": [
-           "export [filepath (STRING)]",
-           "Note: AOs follows the same string handling conventions as in C#.\n",
-           "Example usage:",
-           "export Test.txt                         # Save the terminal text to \"Test.txt\"",
-           "export \"MyFolder\\Text.txt\"           # Save the terminal text to \"MyFolder\\Text.txt\""
-       ],
-       "supported_args": null,
-       "default_values": [""],
-       "is_flag": false,
-       "min_arg_len": 1,
-       "max_arg_len": 1,
-       "method": "D:\\Dev Projects\\AOs\\AOs-2.6\\AOs\\Files.x72\\etc\\PowerToys\\Export\\Export.bat",
-       "location": "external",
-       "do_index": true
-   },
-   {
-       "cmd_names": ["py"],
-       "help_message": "Python build system",
-       "usage": null,
-       "supported_args": [
-           {
-               "args": ["install"],
-               "help_message": "Install pip packages in the current virtual environment"
-           },
-           {
-               "args": ["freeze"],
-               "help_message": "Create \"requirements.txt\" for current virtual environment"
-           },
-           {
-               "args": ["list"],
-               "help_message": "List all installed pip packages from the current virtual environment"
-           }
-       ],
-       "default_values": [""],
-       "is_flag": false,
-       "min_arg_len": 0,
-       "max_arg_len": 0,
-       "method": "D:\\Dev Projects\\AOs\\AOs-2.6\\AOs\\Files.x72\\etc\\PowerToys\\Py\\Py.bat",
-       "location": "external",
-       "do_index": true
-   }
]
```

3. Goto [`settings.json`](https://github.com/SrijanSriv211/AOs/blob/master/src/Files.x72/root/settings.json) in AOs directory and paste it all:

```diff
{
    "default_else_shell": "cmd.exe",
    "username": null,
    "startlist": [],
    "readline": {
        "color_coding": true,
        "auto_complete_suggestions": true
    },
    "search_index": {
        "extensions": [
            ".exe", ".msi", ".lnk"
        ],
        "search_paths": [
            "C:\\Users\\%username%\\Desktop",
            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
        ],
        "excluded_items": [""]
    },
    "cmd_schema": [
+		{
+		    "cmd_names": ["export"],
+		    "help_message": "Export text from the console",
+		    "usage": [
+		        "export [filepath (STRING)]",
+		        "Note: AOs follows the same string handling conventions as in C#.\n",
+		        "Example usage:",
+		        "export Test.txt                         # Save the terminal text to \"Test.txt\"",
+		        "export \"MyFolder\\Text.txt\"           # Save the terminal text to \"MyFolder\\Text.txt\""
+		    ],
+		    "supported_args": null,
+		    "default_values": [""],
+		    "is_flag": false,
+		    "min_arg_len": 1,
+		    "max_arg_len": 1,
+		    "method": "D:\\Dev Projects\\AOs\\AOs-2.6\\AOs\\Files.x72\\etc\\PowerToys\\Export\\Export.bat",
+		    "location": "external",
+		    "do_index": true
+		},
+		{
+		    "cmd_names": ["py"],
+		    "help_message": "Python build system",
+		    "usage": null,
+		    "supported_args": [
+		        {
+		            "args": ["install"],
+		            "help_message": "Install pip packages in the current virtual environment"
+		        },
+		        {
+		            "args": ["freeze"],
+		            "help_message": "Create \"requirements.txt\" for current virtual environment"
+		        },
+		        {
+		            "args": ["list"],
+		            "help_message": "List all installed pip packages from the current virtual environment"
+		        }
+		    ],
+		    "default_values": [""],
+		    "is_flag": false,
+		    "min_arg_len": 0,
+		    "max_arg_len": 0,
+		    "method": "D:\\Dev Projects\\AOs\\AOs-2.6\\AOs\\Files.x72\\etc\\PowerToys\\Py\\Py.bat",
+		    "location": "external",
+		    "do_index": true
+		},
        {
            "cmd_names": [":", "rij"],
            "help_message": "A quick search engine for files on your machines",
            "usage": null,
            "supported_args": null,
            "default_values": [""],
            "is_flag": false,
            "min_arg_len": 0,
            "max_arg_len": 0,
            "method": "Rij",
            "location": "internal",
            "do_index": true
        },
        ...
    ]
}
```

4. Save the file, launch AOs and done 👍
