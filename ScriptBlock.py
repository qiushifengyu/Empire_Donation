from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Bypass Script_Block',

            'Author': ['@Homjxie:>' 'Ryan_Cobb',],

            'Description': ("@Ryan Cobb @Homjxie"
                            "Most companies only realize the need to enable script block logging after it is too late. To provide some recourse in this situation, PowerShell automatically logs script blocks when they have content often used by malicious scripts."),
            'Background' : True,

            'OutputExtension' : None,
            
            'NeedsAdmin' : True,

            'Language' : 'powershell',

            'MinLanguageVersion' : '2',
            
            'Comments': [
                'https://twitter.com/cobbr_io',
                'https://twitter.com/GihadAlkmaty',
            ]
        }

         
        self.options = {
            # format:
            #   value_name : {description, required, default_value}
            'Agent' : {
                'Description'   :   'Agent to run module on.',
                'Required'      :   True,
                'Value'         :   ''
            }
        }

        
        self.mainMenu = mainMenu
        
        for param in params:
             
            option, value = param
            if option in self.options:
                self.options[option]['Value'] = value


def generate(self):

        moduleName = self.info["Name"]

         
        moduleSource = self.mainMenu.installPath + "/data/module_source/management/Bypass-ScriptBlock.ps1"

        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode

        script += "\nwio.sh"

        for option,values in self.options.iteritems():
            if option.lower() != "agent":
                if values['Value'] and values['Value'] != '':
                    if values['Value'].lower() == "true":
                        
                        script += " -" + str(option)
                    else:
                        script += " -" + str(option) + " " + str(values['Value'])
	script += ' | Out-String | %{$_ + \"`n\"};"`n'+str(moduleName)+' completed!"'
   		    
        return script
