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
`{`
`   .png: /home/<user>/Pictures,`
`   .md: /home/<user>/Documents`
`}`

> [!IMPORTANT]
> *extensions are only valid if they start with a . so you can't write png that won't be accepted write .png*
