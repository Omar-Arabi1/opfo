# opfo
opfo **O**ver**P**owerd**F**ile**O**rganizer is an advanced file organizer implemented in python

## what it does:
opfo is a file organizer that organizes your file based on their extension and path set to in the config file located at
*~/.opfo/opfo.json* there are defaults when you first run the application for common file extensions and the paths they
may locate to

## default config:

| extension | default path |
| --------- | ------------ |
| .png      | ~/Pictures   |
| .jpg      | ~/Pictures   |
| .txt      | ~/Documents  |
| .mp4      | ~/Videos     |


> [!NOTE]
> *if any of these paths is not available it won't be added to your default config, and all these could be*
> *modified manually inside of the config file as discussed*

## configuration:
configuring this tool is very easy, but it has some simple rules to follow, first of all the config file is located 
*~/.opfo/opfo.json* the configuration is written like this:


`<.extension>: <path/to/extension/>`


for example:

    {
        .png: /home/<user>/Pictures,
        .md: /home/<user>/Documents
    }

> [!IMPORTANT]
> *extensions are only valid if they start with a . so you can't write png that won't be accepted, write .png*
> *its also important to write absolute paths not relative or ~ for home/user you have to write it yourself*

some things that may make your config invalid:
- you have the path pointing to a file not a directory `/home/<user>/Pictures/pic.png`
- the path you are pointing to doesn't exist `i/do/not/exist`

> [!TIP]
> *if you deleted or changed a path to a directory that was pointed to by an extension make sure to change it or that*
> *would result in an error that is why it is recommended to run --check whenever you changed something related to the*  > *config*

## the check option:
the `--check` option allows you to check the configuration on wether its valid or not, this option
runs automatically when you try to organize the fles, but you could run it alone without organizing the files

> [!TIP]
> *it is recommended to run this option before organizing the files, but it is not enforeced*

once the option is ran through


`opfo --check/-c`


it should log `[ INFO ] All Good!` if anything wrong with the config was encountered like a path doesn't exist
or is a file not a direcotry, it will log good info like the path and its extension to help you fix it
